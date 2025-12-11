from .classification import classifier
from .gemini_service import analyze_with_gemini
import json
from pydantic import BaseModel


class AnalyzeSchema(BaseModel):
    resume : str
    ton : str
    categorie : str
    score : float


def classifier_and_analyze(text,categorie):
    HF_output = classifier(text, categorie)

   
    categorie = HF_output["label"]
    score = HF_output["score"]
   
  
    prompt = f"""
text_original = "{text}"

Catégorie détectée par Hugging Face : "{categorie}"
Score : {score}

Donne moi :
- un resume tres court
- un ton general : positif , negatif ou neutre
- retourne exactement le JSON suivant :
{{
    "resume": "...",
    "resume": "...",
    "ton": "...",
    "categorie": "{categorie}",
    "score": {score}
    
    }}
"""
    
    gemini_result = analyze_with_gemini(prompt)

    output = AnalyzeSchema(
        resume=gemini_result.resume,
        ton=gemini_result.ton,
        categorie=categorie,
        score=score
    )

    return output

text = "L'équipe a dominé le match grâce à une possession de balle remarquable et un pressing constant."
categorie = ["sante", "nouriture", "sport", "beaute", "fashion", "technologie"]

result = classifier_and_analyze(text,categorie)

# print(result.model_dump_json())