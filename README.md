# VAPI flask
![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) ![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat&logo=googlecloud&logoColor=white) ![ngrok](https://img.shields.io/badge/ngrok-1F1E37?style=flat&logo=ngrok&logoColor=white)

Serveur d'API pour les webhook [VAPI](https://vapi.ai/).

## 🔧 Installation

Clone projet
```shell
git clone https://github.com/Oscaro92/vapi-flask.git
cd vapi-flask
```

Création d'un environment virtuel
```shell
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

Installation des dépendances
```shell
pip install -r requirements.txt
```

Configuration ngrok

Lancement d'un serveur [ngrok](https://ngrok.com/) afin d'obtenir un lien public auquel vous pouvez accéder depuis n'importe où sur internet, comme si votre application était hébergée en ligne.
```shell
ngrok http 5000

# windows
./ngrok.exe http 5000
```

## 🚀 Utilisation

```shell
python app.py
```

## 📁 Structure du projet

```
vapi-flask/
├── app.py              # Serveur d'api 
├── function.py         # Fonction de Google calendar 
├── requirements.txt    # Dépendences
└── README.md           # Documentation
```

## 📝 License

This project is licensed under the MIT License.
