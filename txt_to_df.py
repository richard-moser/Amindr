import re

def find_doi(text):
    # This regex looks for 'doi' and captures everything that follows it
    pattern = r'doi: (.*?)($|\s)'
    match = re.search(pattern, text, re.IGNORECASE)

    # Return the matched group if found, else return None
    return match.group(1).strip() if match else None



def txt_to_df(filename):   

 import pandas as pd
 data = []
 file = open(filename, "r")
 raw = file.read()
 
	#split into publications
 publications = raw.split("\n\n\n")
 #print(len(publications))

 for pub in publications:
  #split into elements
  element_list = pub.split("\n\n")

  #get info from first line
  doi = find_doi(element_list[0])
  if not doi: #discard if first line doesn't have proper format
    continue
  doi = doi[:len(doi)-1]

  split = element_list[0].split(".",3)
  index = split[0]
  journal = split[1]

  #get title 
  title = element_list[1]
  title = title.replace("\n", "")

  #get abstract
  element_list = [item for item in element_list if "Author information:" not in item and "Conflict of interest statement:" not in item]
  abstract = max(element_list, key=len)
  abstract = abstract.replace("\n", " ")

  #save data in list
  data.append([index, title, abstract, journal, doi])
    
	# Convert list to DataFrame
 publications_df = pd.DataFrame(data, columns=['Index','Title', 'Abstract', 'Journal', 'DOI'])
 #publications_df.head()
 return publications_df

# txt_to_df("abstract-alzheimers-set.txt").to_csv('out.csv', index=False)