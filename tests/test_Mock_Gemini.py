import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.gemini_service import analyze_with_gemini


def test_gemini(mocker):
    fake_output = {
            "resume": "resume simule",
            "ton": "positif"      
              } 
    
    fake_response = mocker.Mock()
    fake_response.text = json.dumps(fake_output) 

    fake_response.status_code = 200
    fake_response.json.return_value = fake_output

    mock_client_instance = mocker.Mock()
    mock_client_instance.models.generate_content.return_value = fake_response

    mocker.patch(
        "app.services.gemini_service.genai.Client",
        return_value = mock_client_instance
    )

    result = analyze_with_gemini("L'équipe a dominé le match grâce à une possession de balle remarquable et un pressing constant.")


    assert result.resume == "resume simule"
    assert result.ton == "positif"
