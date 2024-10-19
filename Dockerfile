# Utiliser une image Python officielle
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
