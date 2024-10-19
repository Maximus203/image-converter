# 🖼️ Convertisseur d'images en WebP

Bienvenue dans le projet de conversion d'images en WebP ! Ce projet vous permet de convertir facilement des images aux formats PNG, JPG et JPEG en WebP via une interface web conviviale.

## 🌐 Fonctionnalités

- **Interface web simple** : Fournit une interface pour sélectionner les répertoires d'entrée et de sortie.
- **Conversion rapide** : Convertit rapidement les images en WebP.
- **Dockerisé** : Facile à déployer avec Docker.

## 🛠️ Technologies utilisées

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
   git clone https://github.com/Maximus203/image-converter.git
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

Pour toute question ou suggestion, vous pouvez me contacter à [printf0cherif@gmail.com](mailto:printf0cherif@gmail.com).

## 🔑 Licence

Ce projet est sous licence MIT.

---

Merci d'avoir visité ce projet ! J'espère qu'il vous sera utile. 😊
