import discord
from discord import SyncWebhook
from discord.utils import get
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from urlextract import URLExtract

"""
This file contains all the functions needed to get the elements
from an anime used in the animeSearch function in main.
"""

def getUrl(keyword, position):
    """Takes in a keyword and a position, and returns the URL of the search result at that position

    Args:
        keyword (string): keyword to search
        position (int): position of which to return url of (top result, second result, etc.)

    Returns:
        string: URL of the search result at position "position"
    """

    # the index of the first search result in the array of links on the page is 93
    # there are 4 miscellaneous links between results, so for the next position, go 5 links down
    index = 92 + (5 * position)

    r = requests.get(f'https://myanimelist.net/anime.php?q={keyword}&cat=anime')
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')

    return links[index].get('href')

def getDescription(url):
    """Gets the description from a URL of a specific anime

    Args:
        url (string): URL to get description from

    Returns:
        string: the description field from URL input
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    description_html = soup.find_all('p', attrs={'itemprop':'description'})

    description = str(description_html)[27:-5].replace('<br>', '\n').replace('<br/>', '')

    return description

def getImage(url):
    """Returns the URL for the cover image of an anime

    Args:
        url (string): URL to take image from

    Returns:
        string: image URL to the .jpg cover image
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    image_html = soup.find_all(attrs={'itemprop':'image'})

    extractor = URLExtract()
    image = extractor.find_urls(str(image_html[0]))

    return image[0]