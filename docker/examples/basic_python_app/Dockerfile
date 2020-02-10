FROM python:3.5.7-slim-buster

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip \
    && pip3 install -r requirements.txt

ENTRYPOINT ["python", "./app.py"]