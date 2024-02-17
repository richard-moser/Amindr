#Adapted from paper https://arxiv.org/abs/2401.07059

categories_explained = """
(F) NOT RELEVANT
We are interested in peer-reviewed publications of primary research articles or 5b-analyses that help us understand the pathology and progression of AD, diagnose it, prevent it, or develop treatments against it. If the publication does not fulfill these criteria, please classify it as NOT RELEVENT. Not relevant are publications on treatments non-specific to AD, on patient care, quality of life and caregivers (except papers that mention quality of life as an outcome of a treatment), papers that only mention AD in the dataset name and papers that focus on other neurodegenerative diseases: PD, FTD etc., with little comparison to AD.
(A) Disease Mechanisms
The goal of this topic is to better understand how AD develops and progresses. This includes papers that aim to understand the genetics, neuropathology, and cellular/molecular mechanisms underlying Alzheimer’s disease and its progression. It can include in silico papers (modelling protein folding/binding), preclinical papers (in vitro/animal models), clinical studies looking at neuropathology (topography, associations, etc.), and development of new methods or models (animal or in vitro) for studying AD. The paper should not be directly related to treatment (except of concluding sentences may say that the work gives insight into new treatment avenues), in which case it would fall under category C, or measures of disease status or progression, in which case it would fall under category C. 
(C) Diagnostic/Prognostic Tools
The goal of this topic is to diagnose or stratify patients with AD and mild cognitive impairment (MCI) or distinguish them from other diseases. This includes papers focused on using tools for prognosis (looking at disease trajectory or progression from MCI to AD), or diagnosis (differentiating AD from other neurodegenerative diseases, or AD from cognitively normal controls/MCI) of AD/MCI. It also includes papers that seem focused on a different neurodegenerative disease, but provide insight into how AD may be distinct (Dementia with Lewy Bodies, Vascular Dementia), papers focused on diagnostic tools for MCI/subjective MCI and papers on post-mortem studies if they fit the other criteria.
(D) Treatment Avenues
The goal of this topic is to treat or prevent AD
"""

def get_prompt_main (title, body, categories_explained=categories_explained) :
    prompt = """
The following is a publication related to Alzheimer's Disease (AD). Please analyze the following title and abstract of the publication and classify it using the categories and their explanations that are listed afterwards.
TITLE: {title}.
ABSTRACT: {body}.
ABSTRACT END
You can ONLY choose from the following curated categories:
Categoriy shortcuts: [F, A, B, C]
Explanations: {categories_explained}
Use the following JSON template to answer
Replace y with the most suitable category shortcut and z with a reasoning for your choice. 
ALWAYS ONLY respond with a valid json for python with the following structure:
{{
"most_relevant_category": y, 
"clear_reasoning": z
}}
Dont't wrap ```json ``` around!
""".format(title=title, body=body, categories_explained=categories_explained)
    return prompt



A_subcategory_descriptions = """
Genetics (A1a)
This topic includes new variants, genetic and transcriptomics insights such as genome-wide association studies.
APOE (A1b) 
This topic is about apolipoprotein E (APOE). 
Familial AD mutations (A1c) 
This topic is about familial AD mutations, such as APP, presenilin 1/2, BACE
Autophagy/Proteostasis (A2) 
This topic includes endosomal/lysosomal dysfunction, protein uptake/trafficking, general protein aggregation, post-translational modifications, and proteomics. It does not include tau and amyloid-beta, as it belongs to a different topic.
Metabolism and Mitochondrial Dysfunction/Oxidative Stress (A3) 
This topic includes metabolic changes, nutrition/diet, stress, mitochondria, oxidative stress, changes in glucose/insulin. 
Neural Excitability, Synapses, and Brain Connectivity (A4) 
This topic is on synaptic transmission and neurotransmitters, including cholinergic and dopaminergic systems. It also includes brain connectivity and structural integrity.
Amyloid Pathology (A5) 
This topic includes APP processing/secretases, amyloid-beta aggregation, and amyloid-beta function and amyloid-mediated toxicity/pathology. Check if another subcategory fits before labelling with this one.
Tau Pathology (A6) 
This topic includes tau post-translational modifications/aggregations, and tau seeding and pathology.
The Immune System and Glial Cells (A7) 
This topic includes the gut/brain axis, inflammation, TREM2. Also, it includes studies that focus on astrocytes, microglia, or oligodendrocytes.
Cognitive and Behavioural Changes (A8) 
This topic focuses on cognitive and behavioral changes. It includes sensory processing, depression, sleep, smell, auditory, visual functioning. 
Vascular Contributions (A9) 
This topic includes arterial stiffness, atherosclerosis, cerebral amyloid angiopathy, microbleeds, white matter hyperintensities, blood-brain barrier, endothelial cells, lipoproteins interacting with vessels, angiogenesis, and platelet aggregation.
Epidemiological Studies (A10) 
This topic includes non-genetic factors or comorbidities that put people at risk of developing AD or decrease the risk. It includes incidence/prevalence studies in specific populations, genetic predisposition to a risk factor, comorbidities such as cardiovascular disease/diabetes/depression, nutrition/vitamin deficiencies, socioeconomic background, air pollution, etc. Note: Mechanistic studies relating to HOW these non-genetic factors/comorbidities put people at risk belong to the other categories depending on their fit.
Miscallaneous (AX)
Comprehensive umbrella for all publications that do not fit clearly to any of the other categories.
"""

def get_prompt_A (title, body, categories_explained=A_subcategory_descriptions) :
    prompt = """
The following is a publication related to Alzheimer's Disease (AD). Please analyze the following title and abstract of the publication and classify it using the categories and their explanations that are listed afterwards.
TITLE: {title}.
ABSTRACT: {body}.
ABSTRACT END
You can ONLY choose from the following curated categories:
Categoriy shortcuts: [A1a, A1b, A1c, A2, A3, A4, A5, A6, A7, A8, A9, A10, AX]
Explanations: {categories_explained}
Use the following JSON template to answer.
Add all suitable categories to the categories list, starting with the most suitable one.
For each category, replace y with the category shortcut and z with a reasoning for your choice. 
ALWAYS ONLY respond with a valid json for python with the following structure:
{{
categories: [
{{"category": y, "clear_reasoning": z}},
]
}}
Dont't wrap ```json ``` around!
""".format(title=title, body=body, categories_explained=categories_explained)
    return prompt




C_subcategory_descriptions = """
(C1) title
descpription 



"""



D_subcategory_descriptions = """
(D1)



"""