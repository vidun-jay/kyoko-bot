FROM python:3

WORKDIR /KYOKO-BOT

COPY . .

RUN pip install -r requirements.txt

RUN chmod a+x newInstance.sh

CMD ["python3", "main.py"]
