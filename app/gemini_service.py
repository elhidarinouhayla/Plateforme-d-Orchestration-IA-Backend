from google import genai
from google.genai import types
from schemas_output_gemini import output_gemini
from config import GEMINI_API_KEY



def analyze_with_gemini(prompt):


    client = genai.Client(api_key=GEMINI_API_KEY)

    instruction = f"""
    Analyse ce texte : "{prompt}"

    Donne-moi :
    - un résumé très court
    - le ton général : positif, négatif ou neutre
    """
    
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=instruction,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": output_gemini.model_json_schema()
    }
)
    

    output = output_gemini.model_validate_json(response.text)
 
    return  output 

prompt = "Le match a été catastrophique : l'équipe a manqué toutes ses occasions, a encaissé plusieurs buts évitables et n'a montré aucune organisation sur le terrain."
print(analyze_with_gemini(prompt))



