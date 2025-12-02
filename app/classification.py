import os
import requests
from config import HF_TOKEN


def classifier(input_text, categories):
    API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": input_text,
        "parameters": {"candidate_labels": categories},
    })

    return output

# print(classifier("L'équipe a dominé le match grâce à une possession de balle remarquable et un pressing constant.", ["sport","sante","nouriture"]))