from labels import main_labels, get_sublabel
from txt_to_df import txt_to_df
from dotenv import load_dotenv
import os, pickle, asyncio
from openai import OpenAI
load_dotenv(".env")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_KEY)


filename = "abstract-alzheimers-set.txt"

pub_df = txt_to_df(filename)

#get main categories 
pub_df["main_category"] = pub_df["doc"].apply(lambda doc: get_category(get_prompt(main_labels, doc)))

#get sub categories 
#pub_df["sub_category"] = pub_df["doc"].apply(lambda doc: get_category(get_prompt(get_sublabel(pub_df["main_category"]), doc)))
pub_df["sub_category"] = pub_df.apply(lambda row: get_category(get_prompt(get_sublabel(row["main_category"]), row["doc"])), axis=1)

with open("df.pkl", "wb") as fp: 
 pickle.dump(pub_df, fp)

#example_A7 = "Peripheral β-amyloid (Aβ), including those contained in the gut, may contribute to the formation of Aβ plaques in the brain, and gut microbiota appears to exert an impact on Alzheimer's disease (AD) via the gut-brain axis, although detailed mechanisms are not clearly defined. The current study focused on uncovering the potential interactions among gut-derived Aβ in aging, gut microbiota, and AD pathogenesis. To achieve this goal, the expression levels of Aβ and several key proteins involved in Aβ metabolism were initially assessed in mouse gut, with key results confirmed in human tissue. The results demonstrated that a high level of Aβ was detected throughout the gut in bothmice and human, and gut Aβ42increased with age in wild type and mutant amyloid precursor protein/presenilin 1 (APP/PS1) mice. Next, the gut microbiome of mice was characterized by 16S rRNA sequencing, and we found the gut microbiome altered significantly in aged APP/PS1 mice and fecal microbiota transplantation (FMT) of aged APP/PS1 mice increased gut BACE1 and Aβ42 levels. Intra-intestinal injection of isotope or fluorescence labeled Aβ combined with vagotomy was also performed to investigate the transmission of Aβ from gut to brain. The data showed that, in aged mice,  the gut Aβ42 was transported to the brain mainly via blood rather than the vagal nerve. Furthermore, FMT of APP/PS1 mice induced neuroinflammation, a phenotype that mimics early AD pathology. Taken together, this study suggests that the gut is likely a critical source of Aβ in the brain, and gut microbiota can further upregulate gut Aβ production, thereby potentially contributing to AD pathogenesis."


def get_prompt (labels, doc):
   prompt = "I have an abstract and a set of labels.\
          Please give me the most suitable label. The labels are: {labels}. \
          Here is the abstract: {doc}"\
         .format(labels = labels, doc = doc)
   return prompt


def get_category (prompt):
   response = client.chat.completions.create(
   model="gpt-3.5-turbo-1106",
   temperature=1,
   response_format={ "type": "json_object" },
   messages=[
        {"role": "system", "content": "You are a useful assistant designed to output JSON"},
        {"role": "user", "content": prompt}
    ]
   )
   return response.choices[0].message.content

