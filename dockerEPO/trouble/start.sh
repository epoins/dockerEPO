#!/bin/bash

# Simuler une erreur
echo "Starting the application..."
sleep 2
echo "An error occurred!" >  /var/log/error.log
echo "An error occurred!" >&2  # Rediriger le message d'erreur vers stderr

# Boucle infinie pour garder le conteneur en cours d'exécution
while true; do
    sleep 10
done

