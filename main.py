from labels import main_labels, get_sublabel, A_labels_dict, find_key_by_value
from txt_to_df import txt_to_df
from test import get_test_df
from dotenv import load_dotenv
import os, asyncio, json
from openai import OpenAI
load_dotenv(".env")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_KEY)

def get_prompt (labels, doc):
   prompt = "I have an abstract and a set of labels.\
          Please give the most suitable label. The label descriptions are: {labels}\
          Here is the abstract: {doc}"\
         .format(labels = labels, doc = doc)
   return prompt


def get_category (prompt):
   response = client.chat.completions.create(
   model="gpt-3.5-turbo-1106",
   temperature=1,
   response_format={ "type": "json_object" },
   messages=[
        {"role": "system", "content": "You are a useful assistant designed to output the the correct label as JSON."},
        {"role": "user", "content": prompt}
    ]
   )
   res = json.loads(response.choices[0].message.content)
   label_desc = res["label"]
   label = find_key_by_value(A_labels_dict, label_desc)
   print(label)
   return label


#filename = "publications.txt"
#pub_df = txt_to_df(filename)
pub_df = get_test_df()

#get main categories 
#pub_df["main_category"] = pub_df["doc"].apply(lambda doc: get_category(get_prompt(main_labels, doc)))

#get sub categories 
#pub_df["sub_category"] = pub_df["doc"].apply(lambda doc: get_category(get_prompt(get_sublabel(pub_df["main_category"]), doc)))
#pub_df["sub_category"] = pub_df.apply(lambda row: get_category(get_prompt(get_sublabel(row["main_category"]), row["doc"])), axis=1)
pub_df["sub_category"] = pub_df.apply(lambda row: get_category(get_prompt(get_sublabel("A"), row["doc"])), axis=1)

pub_df.to_csv('sorted.csv', index=False)

