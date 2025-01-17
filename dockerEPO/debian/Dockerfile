# Utiliser une image de base Debian légère
FROM debian:bullseye-slim

# Mettre à jour les paquets et installer Bash
RUN apt-get update
RUN apt-get install -y --no-install-recommends bash 
RUN rm -rf /var/lib/apt/lists/*

# Définir Bash comme shell par défaut
SHELL ["/bin/bash", "-c"]

# Définir le point d'entrée pour lancer Bash
ENTRYPOINT ["/bin/bash"]
