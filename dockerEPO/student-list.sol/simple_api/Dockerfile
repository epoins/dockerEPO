FROM python:3.8-buster
LABEL maintainer=epo
RUN apt-get update -y && \
apt-get install python3-dev libsasl2-dev libldap2-dev libssl-dev -y
COPY requirements.txt ./
RUN pip3 install -r ./requirements.txt
VOLUME ["/data"]
EXPOSE 5000
COPY student_age.json /data/
COPY student_age.py /
CMD [ "python3", "./student_age.py" ]

