

col =['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing',
       'shivering', 'chills', 'joint_pain', 'stomach_pain', 'vomiting',
       'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_loss',
       'restlessness', 'lethargy', 'irregular_sugar_level', 'cough',
       'high_fever', 'sweating', 'headache', 'yellowish_skin', 'dark_urine',
       'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain',
       'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever',
       'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
       'blurred_and_distorted_vision', 'phlegm', 'chest_pain', 'obesity',
       'loss_of_smell', 'toxic_look_(typhos)', 'muscle_pain',
       'red_spots_over_body', 'scurring']

def len_col():
    return len(col)

def col2():
    return col

def get_symptoms(disease):
    st={
    "Acne": [
        "Blackheads, whiteheads, and pimples on the skin",
        "Oily skin and/or skin that feels tender to the touch",
        "Redness and inflammation around the affected area",
        "Scarring or hyperpigmentation (darkening of the skin) after the acne has healed",
        "Painful cysts or nodules under the skin"
    ],
    "Alcoholic hepatitis": [
        "Abdominal pain and tenderness",
        "Jaundice (yellowing of the skin and eyes)",
        "Nausea and vomiting",
        "Loss of appetite",
        "Fatigue and weakness"
    ],
    "Allergy": [
        "Itchy, watery eyes",
        "Runny or stuffy nose",
        "Sneezing and coughing",
        "Skin rash or hives",
        "Swelling of the face, lips, or tongue"
    ],
    "Chicken pox": [
        "Red, itchy rash that turns into fluid-filled blisters",
        "Fatigue and weakness",
        "Fever",
        "Headache",
        "Loss of appetite"
    ],
    "Common Cold": [
        "Runny or stuffy nose",
        "Sore throat",
        "Coughing",
        "Sneezing",
        "Fatigue and weakness"
    ],
    "Dengue": [
        "High fever",
        "Severe headache",
        "Pain behind the eyes",
        "Joint and muscle pain",
        "Rash"
    ],
    "Diabetes": [
        "Excessive thirst and hunger",
        "Frequent urination",
        "Fatigue and weakness",
        "Blurred vision",
        "Slow-healing cuts or wounds"
    ],
    "Malaria": [
        "Fever",
        "Chills",
        "Headache",
        "Fatigue",
        "Muscle pain or body aches"
    ],
    "Typhoid": [
        "High fever (over 100.4°F or 38°C)",
        "Weakness and fatigue",
        "Abdominal pain and cramps",
        "Headache",
        "Diarrhea or constipation"
    ],
    "Diabetes ": [
        "Excessive thirst and hunger",
        "Frequent urination",
        "Fatigue and weakness",
        "Blurred vision",
        "Slow-healing cuts or wounds"
    ],
    "Drug Reaction": [
        "Skin rash or hives",
        "Itching",
        "Swelling of the face, lips, or tongue",
        "Difficulty breathing",
        "Abdominal pain and vomiting"
    ],
    "Fungal infection": [
        "Itchy, red, and/or scaly skin rash",
        "Skin lesions or blisters",
        "Nail discoloration or thickening",
        "Hair loss or bald patches"
    ],
    "Jaundice": [
        "Yellowing of the skin and eyes",
        "Dark urine",
        "Pale stools",
        "Fatigue or weakness",
        "Abdominal pain"
    ]

}
    
    if disease in st:
        return st[disease]
    else:
        return "Sorry, we don't have information on that disease."


