from app.services.classification import classifier

def test_hugging_face(mocker):
    fake_output = [
        {
            "labels": ["sport", "sante", "nouriture"],
            "scores": [0.56, 0.93, 0.03]
        }
    ]


    fake_response = mocker.Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = fake_output

    mocker.patch(
        "app.services.classification.requests.post",
        return_value=fake_response
    )

    result = classifier(
        "L'équipe a dominé le match grâce à une possession de balle remarquable et un pressing constant.", 
        ["sport","sante","nouriture"]
    )


    assert result == fake_output[0]