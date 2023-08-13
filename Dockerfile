FROM python:3

WORKDIR /KYOKO-BOT

RUN pip install discord.py

RUN pip install python-dotenv

RUN pip install requests

RUN pip install beautifulsoup4

RUN pip install urlextract

RUN pip install markdownify

COPY . .

CMD ["python3", "main.py"]