from ast import keyword
import discord
from discord import SyncWebhook
from discord.utils import get
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

def get_description(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    description_html = soup.find_all('p', attrs={'itemprop':'description'})

    for block in description_html:
        print(block)

    description = str(description_html)[27:-5].replace('<br>', '\n').replace('<br/>', '')

    # print(description)
    return description

def get_url(keyword):
    ''' Takes in a keyword and returns the url from that keyword '''
    r = requests.get(f'https://myanimelist.net/anime.php?q={keyword}&cat=anime')
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        print(link.get('href'))
    # print(links[93].get('href'))
    # return links[93].get('href')

get_url('one%20piece')
# get_description('https://myanimelist.net/anime/31490/One_Piece_Film__Gold')