# 📦 My Library

## Objectif du projet

Développer une application web avec Flask, basée sur l’architecture MVT, permettant de gérer
un catalogue de livres, leurs auteurs, et leurs catégories. L’objectif est de manipuler les relations
entre entités en base de données, d'afficher les données de façon dynamique.

---

## 🚀 Fonctionnalités

- ✅ Gérer un catalogues de livres
- ✅ Gérer les auteurs
- ✅ Gérer les catégories

---

## 🛠️ Technologies utilisées

Commande pour tout installer => pip install -r requirements.txt

- Python 3.12.7
- Flask
- SQLAlchemy
- TailwindCSS + DaisyUI

---

## ⚙️ Installation

```bash
git clone https://github.com/ton-user/ton-projet.git
cd ton-projet
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sur Windows
pip install -r requirements.txt
```

---

## 🛠️ Configuration de la base PostgreSQL (config.py ==> ajouter vous même)

Avec pgAdmin 4: Créer une database

Ensuie dans un fichier config.py, renseignez vos informations de connexion PostgreSQL :

Paramètres de connexion:

scheme         = "postgresql+psycopg2"
username       = "votre_utilisateur"
password       = "votre_mot_de_passe"
hostname       = "localhost"
port           = "5432"
database_name  = "nom_de_votre_base"

Construction de l'URL de connexion:

URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"

SQLALCHEMY_DATABASE_URI = URL_DB

---

## 📁 Structure du projet

📦 MyLibrary/
├── 📂 app/ # Dossier principal de l'application
│ ├── 📂 models/ # Modèles (ex : SQLAlchemy)
│ │ └── 📄 base.py
│ ├── 📂 routes/ # Routes Flask
│ │ ├── 📄 author.py
│ │ ├── 📄 book.py
│ │ └── 📄 index.py
│ ├── 📂 templates/ # Templates HTML (Jinja2)
│ │ └── 📄 index.html
│ ├── 📂 tools/ # Fonctions utilitaires ou helpers
│
│ ├── 📄 init.py # Initialisation de l'app Flask
│ └── 📄 config.py # Configuration de l'application
│
├── 📄 .gitignore # Fichiers à exclure du contrôle de version
├── 📄 main.py # Point d’entrée de l'application Flask
├── 📄 README.md # Documentation du projet
├── 📄 requirements.txt # Dépendances Python du projet
