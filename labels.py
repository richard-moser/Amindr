# main categories
A = "Disease Mechanisms: genetics, neuropathology, and cellular/molecular mechanisms underlying Alzheimer’s disease and its progression"
C = "Diagnostic/Prognostic Tools such as biomarkers for prognosis or diagnosis of Alzheimer’s disease"
D = "Treatment Development: approach to Alzheimer’s disease treatment, new or repurposed drugs and compounds with potential therapeutic use"
F = "care, disease, treatment"
main_labels = [A,C,D,F]

main_labels_dict = {
    "A": A,
    "C": C,
    "D": D,
    "F": F,
}

#sub-categories for A
A1a = "the primary foucs is understanding genetic factors relating to or different variants of AD"
A1b = "the primary focus is understanding APOE"
A1c = "the primary focus are familial mutations such as APP, PSEN1, BACE"
A2 =	"the primary focus are autophagy or proteostasis, e.g. endosomal/lysosomal dysfunction, protein uptake/trafficking, mitophagy, general protein aggregation, non-tau/A-beta post-translational modifications & proteomics"
A3 = "the primary focus are mitochondria, oxidative stress and metabolism"
A4 = "the primary focus are synaptic transmission and functional connectivity, e.g. axonal transport, neurotransmitter systems, brain connectivity and structural integrity"
A5 = "the primary focus are synaptic amyloid-beta pathology & treatments targeting this, e.g. APP processing/secretases, Amyloid-beta aggregation, Amyloid-beta function & Amyloid-mediated toxicity/pathology"
A6	= "the primary focus is tau"
A7 = "the primary focus are glia & the immune system, e.g. gut/brain axis, peripheral and neuroinflammation, TREM2, astrocyte/microglia, oligodendrocyte"
A8 = "the primary focus are cognitive and behavioural change, e.g. depression, sleep, smell, auditory/visual processing"
A9 = "the primary focus are vascular changes in AD, e.g. arterial stiffness, atherosclerosis, cerebral amyloid angiopathy, microbleeds, white matter hyperintensities, blood-brain barrier, endothelial cells, lipoproteins interacting with vessels, angiogenesis, platelet aggregation"
A10 = "the primary focus are risk factors for AD, e.g. epidemiological studies, incidence/prevalence studies in specific populations, non-genetic factors and comorbidities such as cardiovascular disease/diabetes/depression, nutrition/vitamin deficiencies, socioeconomic background, air pollution, etc. which affect risk"
A_labels = [A1a, A1b, A1c, A2, A3, A4, A5, A6, A7, A8, A9, A10]

A_labels_dict = {
    "A1a": A1a, 
    "A1b": A1b,
    "A1c": A1c, 
    "A2": A2, 
    "A3": A3, 
    "A4": A4, 
    "A5": A5, 
    "A6": A6, 
    "A7": A7, 
    "A8": A8, 
    "A9": A9, 
    "A10": A10
}

def get_sublabel(main_label):
    if main_label == "A":
        return A_labels_dict
    elif main_label == "C":
        return 
    elif main_label == "D":
        return 
    elif main_label == "F":
        return 
    else:
        raise ValueError("only accepts A,C,D or F")