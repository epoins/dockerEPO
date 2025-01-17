# Utiliser une image de base
FROM ubuntu:latest

# Installer des outils de base
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copier un script de démarrage
COPY start.sh /start.sh

# Rendre le script exécutable
RUN chmod +x /start.sh

# Définir le point d'entrée
ENTRYPOINT ["/start.sh"]

