FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y --reinstall build-essential

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /star-wars-planets
WORKDIR /star-wars-planets

RUN chmod +x /star-wars-planets/entry.sh

ENTRYPOINT ["/star-wars-planets/entry.sh"]