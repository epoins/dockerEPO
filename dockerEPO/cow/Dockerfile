FROM building5/dumb-init:1.2.1 AS dumb-init
FROM node:latest
COPY --from=dumb-init /dumb-init /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
# Installer app cowsay
RUN apt-get update && apt-get install -y cowsay
ENV MESSAGE="Viva docker!"
CMD ["/bin/bash", "-c", "/usr/games/cowsay $MESSAGE"]
