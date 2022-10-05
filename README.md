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
(tuto source : https://pereprogramming.com/) </br>

├── app/                   <-- répertoire contenant le code Python</br>
│   ├── core/              <-- fichiers partagés (config, exceptions, …)</br>
│   │   └── __init__.py</br>
│   ├── crud/              <-- création, récupération, mises à jour des données</br>
│   │   └── __init__.py</br>
│   ├── __init__.py</br>
│   ├── main.py            <-- point d'entrée de notre programme FastAPI</br>
│   ├── models/            <-- les modèles de notre base de données</br>
│   │   └── __init__.py</br>
│   ├── schemas/           <-- les schémas de validation des modèles</br>
│   │   └── __init__.py</br>
│   ├── templates/         <-- fichiers html/jinja</br>
│   ├── tests/             <-- tests</br>
│   │   └── __init__.py</br>
│   └── views/             <-- fonctions gérant les requêtes HTTP</br>
│       └── __init__.py</br>
├── public/                <-- fichiers CSS, Javascript et fichiers statiques</br>
└── venv/                  

***Next step : Deploy Deep Learning Models With FastAPI***
