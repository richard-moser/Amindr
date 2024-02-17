categories_explained = """

### NOT RELEVANT ###
====================
(F) NOT RELEVANT
We are interested in peer-reviewed publications of primary research articles or 5b-analyses that help us understand the pathology and progression of AD, diagnose it, prevent it, or develop treatments against it. If the publication does not fulfill these criteria, please classify it as NOT RELEVANT. Not relevant are publications on treatments non-specific to AD, on patient care, quality of life and caregivers (except papers that mention quality of life as an outcome of a treatment), papers that only mention AD in the dataset name and papers that focus on other neurodegenerative diseases: PD, FTD etc., with little comparison to AD.

### A - Disease Mechanisms ###
==============================
The goal of this main topic is to better understand how AD develops and progresses. This includes papers that aim to understand the genetics, neuropathology, and cellular/molecular mechanisms underlying Alzheimer’s disease and its progression. It can include in silico papers (modelling protein folding/binding), preclinical papers (in vitro/animal models), clinical studies looking at neuropathology (topography, associations, etc.), and development of new methods or models (animal or in vitro) for studying AD. The paper should not be directly related to treatment (except of concluding sentences may say that the work gives insight into new treatment avenues), in which case it would fall under category C, or measures of disease status or progression, in which case it would fall under category C. 
(A1a) Genetics: This topic includes new variants, genetic and transcriptomics insights such as genome-wide association studies.
(A1b) APOE: his topic is about apolipoprotein E
(A1c) Familial AD mutations: This topic is about familial AD mutations, such as APP, presenilin 1/2, BACE
(A2) Autophagy/Proteostasis: This topic includes endosomal/lysosomal dysfunction, protein uptake/trafficking, general protein aggregation, post-translational modifications, and proteomics. It does not include tau and amyloid-beta, as it belongs to a different topic.
(A3) Metabolism and Mitochondrial Dysfunction/Oxidative Stress: This topic includes metabolic changes, nutrition/diet, stress, mitochondria, oxidative stress, changes in glucose/insulin. 
(A4) Neural Excitability, Synapses, and Brain Connectivity: This topic is on synaptic transmission and neurotransmitters, including cholinergic and dopaminergic systems. It also includes brain connectivity and structural integrity.
(A5) Amyloid Pathology: This topic includes APP processing/secretases, amyloid-beta aggregation, and amyloid-beta function and amyloid-mediated toxicity/pathology. Check if another subcategory fits before labelling with this one.
(A6) Tau Pathology: This topic includes tau post-translational modifications/aggregations, and tau seeding and pathology.
(A7) The Immune System and Glial Cells: This topic includes the gut/brain axis, inflammation, TREM2. Also, it includes studies that focus on astrocytes, microglia, or oligodendrocytes.
(A8) Cognitive and Behavioural Changes: This topic focuses on cognitive and behavioural changes. It includes sensory processing, depression, sleep, smell, auditory, visual functioning. 
(A9) Vascular Contributions: This topic includes arterial stiffness, atherosclerosis, cerebral amyloid angiopathy, microbleeds, white matter hyperintensities, blood-brain barrier, endothelial cells, lipoproteins interacting with vessels, angiogenesis, and platelet aggregation.
(A10) Epidemiological Studies: This topic includes non-genetic factors or comorbidities that put people at risk of developing AD or decrease the risk. It includes incidence/prevalence studies in specific populations, genetic predisposition to a risk factor, comorbidities such as cardiovascular disease/diabetes/depression, nutrition/vitamin deficiencies, socioeconomic background, air pollution, etc. Note: Mechanistic studies relating to HOW these non-genetic factors/comorbidities put people at risk belong to the other categories depending on their fit.

### C - Diagnostic/Prognostic Tools ###
=======================================
The goal of this main topic is to diagnose or stratify patients with AD and mild cognitive impairment (MCI) or distinguish them from other diseases. This includes papers focused on using tools for prognosis (looking at disease trajectory or progression from MCI to AD), or diagnosis (differentiating AD from other neurodegenerative diseases, or AD from cognitively normal controls/MCI) of AD/MCI. It also includes papers that seem focused on a different neurodegenerative disease, but provide insight into how AD may be distinct (Dementia with Lewy Bodies, Vascular Dementia), papers focused on diagnostic tools for MCI/subjective MCI and papers on post-mortem studies if they fit the other criteria.
(C1) Cognitive or Clinical Indicators: This topic can be assessing cognitive domains including attention, executive function, learning, memory, language, motor function, social skills, and other activities of daily living. It can also include psychological, behavioural, or psychiatric changes. Sensory processing is also included. It also includes physiological measurements such as body temperature or mass.
(C2a) Structural changes: This topic includes neuroimaging to detect structural changes in the brain. This is often magnetic resonance imaging (MRI) or diffusion tensor imaging (DTI). It also includes retinal imaging done with optical coherence topography (OCT).
(C2b) Amyloid/tau-based detection: This topic includes imaging techniques, usually positron emission tomography (PET), to detect amyloid or tau levels.
(C2c) Metabolic/connectivity changes: This topic includes detection of changes in brain metabolism, hemodynamics, or connectivity. Techniques used can be functional MRI or FDG-PET. It also includes electroencephalography (EEG) and magnetoencephalography (MEG) studies measuring electrical activity in the brain.
(C2d) Other image-detected targets: This topic includes neuroimaging studies detecting proteins other than amyloid or tau.
(C3) Fluid biomarkers: This topic includes biomarkers collected in plasma, serum, cerebrospinal fluid (CSF), saliva, urine, or blood. This can be detection of amyloid-beta, tau, neurofilament light chains, or other proteins, lipids, and metabolites.
(C4) Precision modelling: This topic includes data-driven studies with a strong computational focus such as creating statistical models or using machine learning. 
(C5) Human brain histology: This topic includes looking at samples from post-mortem studies.

### D - Treatment Avenues ###
=============================
The goal of this main topic is to treat or prevent AD
(D1a) Multiple targets: This includes compounds with multi-target activity. 
(D1b) Gene therapy: This topic includes targeting miRNA or the cell cycle. It includes the use of stem cells.
(D2) Proteostasis/Autophagy: This topic includes compounds targeting proteins other than amyloid-beta or tau. It includes endosomes and lysosomes.
(D3) Metabolism, Mitochondria, Oxidative stress: This topic includes antioxidants and other compounds targeting mitochondria or metabolism.
(D4a) Neuroprotection: This topic includes treatments for neurogenesis and protection against amyloid-mediated toxicity.
(D4b) Neurotransmission: This topic includes regulating synaptic transmission relating to glutamate or GABA. It includes compounds to inhibit cholinesterases (AChE or BChE).
(D5) Amyloid-beta: This topic includes compounds inhibiting amyloid aggregation or formation by secretases.
(D6) Tau: This topic includes kinases and phosphatases, such as GSK3B, that mediate tau phosphorylation. 
(D7) Immune system and glial cells: This topic includes compounds that target the gut-brain axis, neuroinflammation, or glia.
(D8) Cognitive and psychiatric changes: This topic includes compounds that alleviate AD symptoms or enhance cognition.
(D9) Vasculature: This topic includes antihypertensives and blood-brain modulators.
(D10) Non-pharmacological: This topic includes any prevention or intervention method that is not a drug. For example, it includes lifestyle changes in diet, exercise, sleep. It also includes deep brain stimulation (DBS) with electrodes or non-invasive transcranial magnetic stimulation (TMS).

"""



def get_prompt (title, body, categories_explained=categories_explained) : #title and #TITLE: {title}.
    prompt = """
The following is a publication related to Alzheimer's Disease (AD). Please analyze the following abstract of the publication and classify it using the categories and their explanations that are listed afterwards.
ABSTRACT: {body}.
ABSTRACT END
You can ONLY choose from the following curated categories:
Category shortcuts: [F, A1a, A1b, A1c, A2, A3, A4, A5, A6, A7, A8, A9, A10, C1, C2a, C2b, C2c, C2d, C3, C4, C5, D1a, D1b, D2, D3, D4a, D4b, D5, D6, D7, D8, D9, D10]
Explanations: {categories_explained}
Use the following JSON template to answer.
Add all suitable categories to the categories list, starting with the most suitable one. 
Replace y with the category shortcut and z with a reasoning for your choice. 
ALWAYS ONLY respond with a valid json for python with the following structure:
{{
categories: [
{{"category": y, "clear_reasoning": z}}, 
]
}}
Don't wrap ```json ``` around!
""".format(title=title, body=body, categories_explained=categories_explained)
    return prompt
