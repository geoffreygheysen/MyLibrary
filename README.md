# 📦 My Library

## 🎯 Objectif du projet

Développer une application web avec **Flask**, basée sur l’architecture **MVT**, permettant de gérer
un **catalogue de livres**, leurs **auteurs** et leurs **catégories**.  
L’objectif est de manipuler les relations entre entités en base de données, et d'afficher les données dynamiquement.

---

## 🚀 Fonctionnalités

- ✅ Gérer un catalogue de livres (Afficher, créer, modifier, supprimer)
- ✅ Gérer les auteurs (Afficher, créer, modifier, supprimer)
- ✅ Gérer les catégories (Afficher, créer, modifier, supprimer)

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
# récuperer le repository sur sa machine
git clone https://github.com/ton-user/ton-projet.git
# se positiner sur le projet
cd ton-projet
# créer l'environnement virtuel
python -m venv venv
# activer l'environnement virtuel
.\.venv\Scripts\activate
# installer le repertoires de technologies utilisées
pip install -r requirements.txt
```

---

## 🛠️ Configuration de la base PostgreSQL

Créer une base de données via **pgAdmin 4** ou autre, puis renseignez les informations dans `app/config.py` :

La clé secrète est utilisée par Flask pour sécuriser les sessions, les cookies, et la protection CSRF. (ex de site: https://djecrety.ir/)

```python
# Clé secrète Flask (`SECRET_KEY`)
SECRET_KEY = 'votre clé secrète ici'

# Paramètres de connexion
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
├── 📂 app/                         # Dossier principal de l'application Flask
│   ├── 📂 models/                  # Contient les modèles et formulaires
│   │   ├── 📂 db/                  # Modèles de base de données (SQLAlchemy)
│   │   │   ├── 📄 author.py           # Modèle Author (auteur)
│   │   │   ├── 📄 base.py             # Classe de base pour les modèles (Base SQLAlchemy)
│   │   │   ├── 📄 book_category.py    # Modèle pour la relation livre/catégorie (many-to-many)
│   │   │   ├── 📄 book.py             # Modèle Book (livre)
│   │   │   ├── 📄 category.py         # Modèle Category (catégorie)
│   │   ├── 📂 forms/               # Formulaires Flask-WTF pour validation/formulaire web
│   │   │   ├── 📄 author_form.py       # Formulaire pour créer/modifier un auteur
│   │   │   ├── 📄 book_form.py         # Formulaire pour créer/modifier un livre
│   │   │   └── 📄 category_form.py     # Formulaire pour créer/modifier une catégorie
│   │   │
│   ├── 📂 routes/                  # Définition des routes Flask (Blueprints)
│   │   ├── 📄 author.py              # Routes liées aux auteurs (CRUD)
│   │   ├── 📄 book.py                # Routes liées aux livres (CRUD)
│   │   ├── 📄 category.py            # Routes liées aux catégories (CRUD)
│   │   └── 📄 index.py               # Route(s) pour la page d'accueil ou générale
│   │
│   ├── 📂 templates/               # Templates HTML Jinja2 pour rendre les pages web
│   │   ├── 📂 author/
│   │   │   ├── 📄 author.html            # Liste des auteurs
│   │   │   └── 📄 create_author.html     # Formulaire création auteur
│   │   ├── 📂 book/
│   │   │   ├── 📄 books.html              # Liste des livres
│   │   │   ├── 📄 create_book.html        # Formulaire création livre
│   │   │   └── 📄 update_book.html        # Formulaire modification livre
│   │   ├── 📂 category/
│   │   │   ├── 📄 categories.html         # Liste des catégories
│   │   │   ├── 📄 create_category.html    # Formulaire création catégorie
│   │   │   └── 📄 update_category.html    # Formulaire modification catégorie
│   │   └── 📄 index.html                   # Template de la page d'accueil générale
│   │
│   ├── 📂 tools/                   # Modules utilitaires / helpers
│   │   └── 📄 session_scope.py        # Gestionnaire de contexte pour session SQLAlchemy
│   │
│   ├── 📄 __init__.py              # Initialise l'application Flask, extensions, Blueprints
│   └── 📄 config.py                # Configuration (clé secrète, base de données, etc.)
│
├── 📄 .gitignore                   # Liste des fichiers/dossiers à ignorer par Git
├── 📄 main.py                      # Point d'entrée principal qui lance l'application Flask
├── 📄 README.md                    # Documentation générale du projet
└── 📄 requirements.txt             # Liste des dépendances Python à installer
```

---

## 📄 Licence

Ce projet est libre et open-source.
