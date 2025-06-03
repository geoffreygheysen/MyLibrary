# 📦 My Library

## 🎯 Objectif du projet

Développer une application web avec **Flask**, basée sur l’architecture **MVT**, permettant de gérer
un **catalogue de livres**, leurs **auteurs** et leurs **catégories**.  
L’objectif est de manipuler les relations entre entités en base de données, et d'afficher les données dynamiquement.

---

## 🚀 Fonctionnalités

- ✅ Gérer un catalogue de livres  
- ✅ Gérer les auteurs  
- ✅ Gérer les catégories  

---

## 🛠️ Technologies utilisées

Commande pour tout installer :  
```bash
pip install -r requirements.txt
```

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

## 🛠️ Configuration de la base PostgreSQL

Créer une base de données via **pgAdmin 4** ou autre, puis renseignez les informations dans `app/config.py` :

```python
scheme         = "postgresql+psycopg2"
username       = "votre_utilisateur"
password       = "votre_mot_de_passe"
hostname       = "localhost"
port           = "5432"
database_name  = "nom_de_votre_base"

# Construction de l'URL de connexion
URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"

# Configuration SQLAlchemy
SQLALCHEMY_DATABASE_URI = URL_DB
```

---

## 📁 Structure du projet

```
📦 MyLibrary/
├── 📂 app/                         # Dossier principal de l'application
│   ├── 📂 models/                  # Modèles (ex : SQLAlchemy)
│   │   ├── 📂 db/                  # Base de données et modèles
│   │   │   ├── 📄 author.py
│   │   │   ├── 📄 base.py
│   │   │   ├── 📄 book_category.py
│   │   │   ├── 📄 book.py
│   │   │   └── 📄 category.py
│   │   ├── 📂 forms/               # Formulaires Flask-WTF
│   │   │   ├── 📄 author_form.py
│   │   │   ├── 📄 book_form.py
│   │   │   ├── 📄 category_form.py
│   ├── 📂 routes/                  # Routes Flask
│   │   ├── 📄 author.py
│   │   ├── 📄 book.py
│   │   └── 📄 index.py
│   ├── 📂 templates/               # Templates HTML (Jinja2)
│   │   └── 📄 index.html
│   ├── 📂 tools/                   # Fonctions utilitaires ou helpers
│   ├── 📄 __init__.py              # Initialisation de l'app Flask
│   └── 📄 config.py                # Configuration de l'application
├── 📄 .gitignore                   # Fichiers à exclure du contrôle de version
├── 📄 main.py                      # Point d’entrée de l'application Flask
├── 📄 README.md                    # Documentation du projet
└── 📄 requirements.txt             # Dépendances Python du projet
```

---

## 📄 Licence

Ce projet est libre et open-source.