FROM python:3.9-slim
RUN apt-get update && apt-get install -y bash \
    && rm -rf /var/lib/apt/lists/*
# dir for volumes
RUN mkdir -p /ano /named /bind /tmpfs
# Only the anonymous vol can be declared here
VOLUME /ano
ENTRYPOINT ["bash"]
