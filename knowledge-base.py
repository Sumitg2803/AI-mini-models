# Simple Medical Diagnosis using Knowledge Base (Beginner Level)

# Knowledge Base: symptoms (key) → disease (value)
rules = {
    ("fever",): "Viral Infection",
    ("cough", "fever"): "Corona",
    ("headache", "fever"): "Dengue",
    ("cold", "sneezing"): "Common Cold",
    ("chest_pain", "breathlessness"): "Asthma",
    ("joint_pain", "rash", "fever"): "Chikungunya",
    ("fever", "chills", "sweating"): "Malaria",
    ("weight_loss", "night_sweats", "cough"): "Tuberculosis (TB)",
    ("abdominal_pain", "vomiting"): "Food Poisoning",
    ("runny_nose", "watery_eyes", "sneezing"): "Allergy",
    ("sore_throat", "fever", "swollen_glands"): "Tonsillitis",

    # Some cancers
    ("persistent_cough", "chest_pain", "weight_loss"): "Lung Cancer",
    ("lump_in_breast", "breast_pain", "nipple_discharge"): "Breast Cancer",
    ("blood_in_stool", "abdominal_pain", "weight_loss"): "Colon Cancer",
    ("frequent_headaches", "vision_problems", "nausea"): "Brain Cancer",
    ("difficulty_swallowing", "chest_pain", "hoarseness"): "Throat Cancer",
    ("frequent_urination", "blood_in_urine", "pelvic_pain"): "Bladder Cancer",
    ("yellow_skin", "abdominal_swelling", "loss_of_appetite"): "Liver Cancer",
}

# Take user input
print("Enter your symptoms (comma separated):")
user_input = input().lower().replace(" ", "")
symptoms = tuple(user_input.split(","))

# Inference (check KB)
diagnosis = "Unknown Disease"
for rule_symptoms, disease in rules.items():
    if all(s in symptoms for s in rule_symptoms):
        diagnosis = disease
        break

# Output
print(f"Diagnosis: {diagnosis}")
