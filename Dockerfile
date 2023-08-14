FROM python:3

WORKDIR /KYOKO-BOT

COPY . .

RUN echo $TOKEN >> .env

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]