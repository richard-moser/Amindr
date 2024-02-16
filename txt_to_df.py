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

  #get title 
  title = element_list[1]

  #get abstract
  element_list = [item for item in element_list if "Author information:" not in item]
  abstract = max(element_list, key=len)

  #get doi
  identifier = next((item for item in element_list if "DOI:" in item), None)
  
  doc = title+abstract

  #save data in list
  data.append([title, abstract, identifier, doc])
    
	# Convert list to DataFrame
 publications_df = pd.DataFrame(data, columns=['Title', 'Abstract', 'Identifier', 'doc'])
 #publications_df.head()
 return publications_df

#txt_to_df("abstract-alzheimers-set.txt").to_csv('out.csv', index=False)