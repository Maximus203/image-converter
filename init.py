import os

# Définition de la structure du projet
project_structure = {
    'app': {
        '__init__.py': """from flask import Flask

app = Flask(__name__)

from app import routes
""",
        'routes.py': """from flask import render_template, request, redirect, url_for
from app import app
from app.converter import batch_convert
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        input_dir = request.form.get('input_dir')
        output_dir = request.form.get('output_dir')
        if os.path.isdir(input_dir) and os.path.isdir(output_dir):
            batch_convert(input_dir, output_dir)
            message = 'Conversion terminée avec succès.'
        else:
            message = 'Veuillez entrer des répertoires valides.'
        return render_template('index.html', message=message)
    return render_template('index.html', message=message)
""",
        'converter.py': """import os
from PIL import Image

def convert_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, 'webp')
            print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def batch_convert(input_dir, output_dir):
    supported_formats = ('.png', '.jpg', '.jpeg')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_dir, output_filename)
            convert_image(input_path, output_path)
"""
    },
    'templates': {
        'index.html': """<!DOCTYPE html>
<html>
<head>
    <title>Convertisseur d'Images en WebP</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Convertisseur d'Images en WebP</h1>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
    <form method="post">
        <label for="input_dir">Répertoire d'entrée :</label>
        <input type="text" id="input_dir" name="input_dir" required>
        <br><br>
        <label for="output_dir">Répertoire de sortie :</label>
        <input type="text" id="output_dir" name="output_dir" required>
        <br><br>
        <button type="submit">Convertir</button>
    </form>
</body>
</html>
"""
    },
    'static': {
        'style.css': """body {
    font-family: Arial, sans-serif;
    margin: 50px;
}

h1 {
    color: #333;
}

label {
    display: inline-block;
    width: 150px;
}

input {
    padding: 5px;
    width: 300px;
}

button {
    padding: 10px 20px;
    background-color: #5CB85C;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #4CAE4C;
}

p {
    color: red;
}
"""
    },
    'images': {},
    'output': {},
    '.': {
        'app.py': """from app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
""",
        'requirements.txt': """Flask
Pillow
""",
        'Dockerfile': """# Utiliser une image Python officielle
FROM python:3.9-slim

# Installer libwebp pour le support WebP
RUN apt-get update && apt-get install -y libwebp-dev

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 4444
EXPOSE 4444

# Démarrer l'application
CMD ["python", "app.py"]
""",
        'README.md': """# 🖼️ Convertisseur d'Images en WebP

Bienvenue dans le projet de conversion d'images en WebP ! Ce projet vous permet de convertir facilement des images aux formats PNG, JPG et JPEG en WebP via une interface web conviviale.

## 🌐 Fonctionnalités

- **Interface Web Simple** : Fournit une interface pour sélectionner les répertoires d'entrée et de sortie.
- **Conversion Rapide** : Convertit rapidement les images en WebP.
- **Dockerisé** : Facile à déployer avec Docker.

## 🛠️ Technologies Utilisées

- Python
- Flask
- Pillow
- Docker

## 📦 Installation

### Prérequis

- Python 3.9+
- Anaconda ou Miniconda
- Docker (pour la dockerisation)

### Étapes

1. Clonez le dépôt :

   ```sh
   git clone https://github.com/votre-utilisateur/image-converter.git
   cd image-converter
   ```

2. Activez l'environnement conda existant :

   ```sh
   conda activate convertion-webp
   ```

3. Installez les dépendances Python :

   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Utilisation

1. Lancez l'application :

   ```sh
   python app.py
   ```

2. Ouvrez votre navigateur et accédez à `http://localhost:4444`.

3. Entrez les répertoires d'entrée et de sortie, puis cliquez sur "Convertir".

## 🐳 Dockerisation

Pour exécuter l'application avec Docker :

1. Construisez l'image Docker :

   ```sh
   docker build -t image-converter .
   ```

2. Exécutez le conteneur Docker :

   ```sh
   docker run -p 4444:4444 -v $(pwd)/images:/app/images -v $(pwd)/output:/app/output image-converter
   ```

3. Accédez à `http://localhost:4444` dans votre navigateur.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 📧 Contact

Pour toute question ou suggestion, vous pouvez me contacter à [votre-email@example.com](mailto:votre-email@example.com).

## 🔑 Licence

Ce projet est sous licence MIT.

---

Merci d'avoir visité ce projet ! J'espère qu'il vous sera utile. 😊
""",
        '.gitignore': """__pycache__/
*.pyc
.env
.vscode/
.idea/
.DS_Store
*.log
"""
    }
}

# Fonction pour créer les répertoires et fichiers
def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # C'est un répertoire
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            # C'est un fichier
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

# Point d'entrée du script
if __name__ == '__main__':
    base_project_path = os.path.abspath('.')
    create_project_structure(base_project_path, project_structure)
    print('Structure du projet créée avec succès.')