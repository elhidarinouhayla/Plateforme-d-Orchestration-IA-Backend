from classification import classifier
from gemini_service import analyze_with_gemini
import json

def classifier_and_analyze(text,categorie):
    HF_output = classifier(text, categorie)

    HF_json = json.dumps(HF_output)

    prompt = f"""
text_original = "{text}"

Analyse le JSON suivant produit par Haggimg Face:

{HF_json}

Donne moi :
- un resume tres court
- un ton general : positif , negatif ou neutre
"""
    
    return analyze_with_gemini(prompt)

text = "L'équipe a dominé le match grâce à une possession de balle remarquable et un pressing constant."
categorie = ["sante", "nouriture", "sport", "beaute", "fashion"]

result = classifier_and_analyze(text,categorie)

print(result.model_dump_json())