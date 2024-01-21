#Preprocessing
import pandas as pd

data = []

file = open("abstract-alzheimers-set.txt", "r")
raw = file.read()

#split into publications
publications = raw.split("\n\n\n")
print(len(publications))

for pub in publications:
    #split into elements
    element_list = pub.split("\n\n")

    #get title 
    title = element_list[1]

    #get abstract
    element_list = [item for item in element_list if "Author information:" not in item]
    abstract = max(element_list, key=len)

    #get doi
    identifier = next((item for item in element_list if "DOI:" in item), None)

    #save data in list
    data.append([title, abstract, identifier])
    
# Convert list to DataFrame
publications_df = pd.DataFrame(data, columns=['Title', 'Abstract', 'Identifier'])
publications_df.head()

