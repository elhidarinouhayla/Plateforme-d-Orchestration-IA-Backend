from pydantic import BaseModel

class output_gemini(BaseModel):
    resume : str
    ton : str