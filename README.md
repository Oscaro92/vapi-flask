# VAPI flask
![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) ![Google Calendar](https://img.shields.io/badge/Google_Calendar-4285F4?style=flat&logo=googlecalendar&logoColor=white) ![ngrok](https://img.shields.io/badge/ngrok-1F1E37?style=flat&logo=ngrok&logoColor=white)

Serveur d'API pour les webhook [VAPI](https://vapi.ai/).

## 🔧 Installation

```shell
# Clone the repository
git clone https://github.com/<your-username>/vapi-flask.git
cd vapi-flask

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

##### Configuration localhost

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
mail-agent/
├── app.py              # Serveur d'api 
├── function.py         # Fonction de Google calendar 
├── requirements.txt    # Dependences
└── README.md           # Documentation
```

## 📝 License

This project is licensed under the MIT License.