# Plateforme-d-Orchestration-IA-Backend




## Objectif du projet


Le backend sert de cœur d'orchestration pour l'analyse d'articles. Il fournit une API sécurisée (JWT) qui gère l'enchaînement des services d'Intelligence Artificielle : la Classification Zero-Shot (Hugging Face) pour la catégorisation, suivi de la Synthèse Contextuelle (Gemini API). Il est le garant de la sécurité, de la fiabilité et de la structure des données retournées au frontend.





## Structure du projet

```

backend/

│

├── models/

│   └── model.py      

│

├── tests/

│   └── test_endpoint.py  

│

├── .env            

├── .gitignore      

├── auth.py        

├── translate.py      

├── config.py        

├── database.py      

├── main.py        

│

├── Dockerfile            

├── docker-compose.yml    

│

├── requirements.txt      

└── README.md            



```





---



## Installation



1. Cloner le dépôt GitHub :  



```shell

    git clone https://github.com/elhidarinouhayla/Plateforme-d-Orchestration-IA-Backend.git

    cd project

```



2. Créer un environnement virtuel :



 - Linux / Mac :

```shell

    python -m venv venv

    source venv/bin/activate

```

 - Windows :

```shell

    python -m venv venv

    venv\Scripts\activate

```



3. Installer les dépendances :



```shell

    pip install -r requirements.txt

```



4. Lancer l’API en mode développement :



```shell

    uvicorn main:app --reload

```



 - L’API sera accessible à l’adresse : http://127.0.0.1:8000



 - Documentation interactive Swagger : http://127.0.0.1:8000/docs



Astuce : Le paramètre --reload permet à l’API de se mettre à jour automatiquement à chaque modification du code, très pratique pour le développement.





## Configuration



```shell

# Secrets de l'API (à remplacer par de vraies valeurs)
SECRET_KEY=votre_clef_secrete_jwt
ALGORITHM=HS256

# Configuration Gemini
GEMINI_API_KEY=votre_clef_api_gemini

# Configuration Hugging Face
HF_TOKEN=votre_token_huggingface

# Configuration Base de Données PostgreSQL
USER=user
PASSWORD=password
DATABASE=analyzer_db
HOST=localhost 
PORT=5432

```


## Endpoint:/register et /login

Méthode |  Endpoint   | Description                                                       |
------------------------------------------------------------------------------------------|
POST    | /register   | Enregistre un nouvel utilisateur (stockage du mot de passe hashe).|
------------------------------------------------------------------------------------------|
POST    | /login      | Authentifie l'utilisateur et renvoie un token JWT.                | 


## Endpoint Principal : /analyze

Cet endpoint est protégé par JWT. Il déclenche l'orchestration complète de l'analyse IA.

# POST /analyze

- Header requis: Authorization: Bearer <JWT>

- Body JSON (pour analyse):

```shell
{
  "text": "L'équipe a dominé le match grâce à une possession de balle remarquable et un pressing constant"
  }
```

- Reponce JSON :
```shell
{
  "category": "Sport",
  "score": 0.985,
  "summary": "L'équipe a dominé le match ",
  "tone": "Positif"
}
```

## Tests Unitaires
Les tests sont cruciaux pour garantir la fiabilité du chaînage des services d'IA. Ils incluent un mocking complet des appels externes à Hugging Face et Gemini pour des tests rapides et isolés.

- Mock Hugging Face
- Mock Gemini


### Commande pour lancer les tests :



```shell

pytest

```



## Dockerfile



Le Dockerfile permet de construire une image Docker pour le backend FastAPI.


Il fait les étapes suivantes :


  1. Utilise Python 3.11 comme base

  2. Définit le dossier de travail /app

  3. Copie le fichier requirements.txt et installe les dépendances Python

  4. Copie tout le code du backend dans l’image

  5. Expose le port 8000 pour l’API

  6. Lance le serveur Uvicorn à l’intérieur du conteneur


=> Cela permet de déployer facilement l’API sur n’importe quelle machine sans config supplémentaire





