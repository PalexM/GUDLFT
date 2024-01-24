# GUDLFT
Organisateur des compétitions pour les clubs locaux

## Installation

### Prérequis
- Python 
- pip

1. **Cloner le dépôt**
```bash
git clone https://github.com/PalexM/softdesk.git)https://github.com/PalexM/softdesk.git
cd softdesk
```
2. **Créer et activer un environnement virtuel** :
- Sous Windows :
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- Sous Unix ou MacOS :
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Installer les dépendances** :
 ```
pip install -r requirements.txt
 ```
4. **Initialiser la base de données** :
 ```
python manage.py migrate
 ```

5. **Lancer le serveur** :
 ```
python manage.py runserver 8000
 ```

## Utilisation
Après avoir lancé le serveur, vous pouvez accéder à l'application en ouvrant votre navigateur et en allant à l'adresse `http://localhost:8000`.

## Contribution
Les contributions à ce projet sont les bienvenues. N'hésitez pas à proposer des améliorations ou à signaler des problèmes via les issues ou les pull requests sur GitHub.
