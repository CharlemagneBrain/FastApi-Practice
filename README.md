## FastApi-Practice
- Restructuration du Code
- Configuration 
- Vues
- Tests automatisés
- Tortoise ORM
- Pydantic
- Documentation auto-généré
- Vues htmls
- CRUD

### Structure du projet: 
(tuto source : https://pereprogramming.com/)

├── app/                   <-- répertoire contenant le code Python
│   ├── core/              <-- fichiers partagés (config, exceptions, …)
│   │   └── __init__.py
│   ├── crud/              <-- création, récupération, mises à jour des données
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main.py            <-- point d'entrée de notre programme FastAPI
│   ├── models/            <-- les modèles de notre base de données
│   │   └── __init__.py
│   ├── schemas/           <-- les schémas de validation des modèles
│   │   └── __init__.py
│   ├── templates/         <-- fichiers html/jinja
│   ├── tests/             <-- tests
│   │   └── __init__.py
│   └── views/             <-- fonctions gérant les requêtes HTTP
│       └── __init__.py
├── public/                <-- fichiers CSS, Javascript et fichiers statiques
└── venv/                  <-- environnement virtuel créé à la partie 1

***Next step : Deploy Deep Learning Models With FastAPI***
