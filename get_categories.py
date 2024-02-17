import pandas as pd
from sqlalchemy import create_engine, update, Table, MetaData
from dotenv import load_dotenv
import os, json, threading, time 
import google.generativeai as genai
from labels_all import get_prompt, labels


class Categorizer():
    def __init__(self):
        load_dotenv(".env")
        GEMINI_KEY = os.environ.get("GEMINI_KEY")
        genai.configure(api_key=GEMINI_KEY)
        # Gemini API # currently need VPN to outside Europe
        self.model = genai.GenerativeModel('gemini-pro')
        self.generation_config = genai.types.GenerationConfig(temperature=0) #default: 1.0
        # Database
        self.engine = create_engine('sqlite:///publications.db')
        self.publications = pd.read_sql_query("SELECT * FROM publications", self.engine)
        self.publications_table = Table('publications', MetaData(), autoload_with=self.engine)


    def get_categories(self):
        threads = []
        for i in range(self.publications.shape[0]):
            thread = threading.Thread(target=self.get_category, args=(i,))
            threads.append(thread)
            thread.start()
            time.sleep(1.01) # current rate limit 60 requests/minute
        if (i%10==0) :
            print("# running threads: " + str(threading.active_count()))

        for thread in threads:
            thread.join()


    def get_unlabeled_publications(self):
        publications = pd.read_sql_query("SELECT * FROM publications", self.engine)
        #remove hallucinated labels
        publications['category1'] = publications['category1'].apply(lambda x: x if x in labels else None)
        publications['category2'] = publications['category2'].apply(lambda x: x if x in labels else None)
        # filter for proposals that do not have a label yet
        publications = publications[publications['category1'].isnull()]
        publications = publications.reset_index()
        self.publications = publications
        return publications.shape[0]


    def get_category(self, i):
        try:
            print(i)
            #get data from gemini api
            doi = self.publications["DOI"][i]
            title = self.publications["Title"][i]
            abstract = self.publications["Abstract"][i]
            prompt = get_prompt(title, abstract)
            res = self.model.generate_content(prompt, generation_config=self.generation_config) #generation_config=generation_config
            json_res = json.loads(res.text)
            categories = json_res["categories"]
            category1 = categories[0]["category"]
            reasoning1 = categories[0]["clear_reasoning"]
            if len(categories) > 1:
                category2 = json_res["categories"][1]["category"]
                reasoning2 = json_res["categories"][1]["clear_reasoning"]
            else:
                category2 = None
                reasoning2 = None
            print(i, category1, category2)
            #save in database
            stmt = (
            update(self.publications_table)
            .where(self.publications_table.c.DOI == doi)
            .values(category1=category1, reasoning1=reasoning1, category2=category2, reasoning2=reasoning2)
            )
            with self.engine.connect() as conn:
                result = conn.execute(stmt)
                conn.commit()  
        except Exception as e:
            print(e)
            print(str(i)+"returned with err")









