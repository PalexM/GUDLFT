# GUDLFT
Organisateur des compétitions pour les clubs locaux

## Installation

### Prérequis
- Python 
- pip

1. **Cloner le dépôt**
```bash
git clone https://github.com/PalexM/GUDLFT.git
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

5. **Lancer le serveur** :
 ```
$env:FLASK_ENV = "development"
$env:FLASK_APP = "server.py"
flask --app server.py --debug run
 ```

## Utilisation
Après avoir lancé le serveur, vous pouvez accéder à l'application en ouvrant votre navigateur et en allant à l'adresse `http://localhost:5000`.

## Contribution
Les contributions à ce projet sont les bienvenues. N'hésitez pas à proposer des améliorations ou à signaler des problèmes via les issues ou les pull requests sur GitHub.
