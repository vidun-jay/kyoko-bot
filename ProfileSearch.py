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
from a user profile used in the profileSearch function in main.
"""

def getDays(profile_url, index):
    """Returns an array of days of anime watched and days of manga read

    Args:
        profile_url (string): profile link to search
        index (int): whether to return anime or manga days

    Returns:
        list: list of the days, days[0] = anime days watched, days[1] = days of manga read
    """

    r = requests.get(profile_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    beginning = '<div class="di-tc al pl8 fs12 fw-b"><span class="fn-grey2 fw-n">Days: </span>'
    end = '</div>'
    days = soup.find_all("div", {"class": "di-tc al pl8 fs12 fw-b"})

    days[0] = str(days[0]).replace(beginning, "").replace(end, "")
    days[1] = str(days[1]).replace(beginning, "").replace(end, "")

    return days[index]

def getEpisodes(profile_url):
    """Returns the number of episodes watched from a given profile

    Args:
        profile_url (string): profile link to search

    Returns:
        string: number of episodes watched
    """
    r = requests.get(profile_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    beginning = '<span class="di-ib fl-r">'
    end = '</span>'
    episodes = soup.find_all("span", {"class": "di-ib fl-r"})
    episodes[2] = str(episodes[2]).replace(beginning, "").replace(end, "")

    return episodes[2]

def getWatching(profile_url):
    """Returns the number of anime currently watching

    Args:
        profile_url (string): profile link to search

    Returns:
        string: number of anime currently watching
    """
    r = requests.get(profile_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    beginning = '<span class="di-ib fl-r lh10">'
    end = '</span>'
    watching = soup.find_all("span", {"class": "di-ib fl-r lh10"})
    watching[0] = str(watching[0]).replace(beginning, "").replace(end, "")

    return watching[0]

def getCompleted(profile_url):
    """Returns the number of completed anime

    Args:
        profile_url (_type_): _description_

    Returns:
        string: number of completed anime
    """
    r = requests.get(profile_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    beginning = '<span class="di-ib fl-r lh10">'
    end = '</span>'
    watching = soup.find_all("span", {"class": "di-ib fl-r lh10"})
    watching[1] = str(watching[1]).replace(beginning, "").replace(end, "")

    return watching[1]

def getProfilePicture(profile_url):
    """Gets the profile picture of a given profile

    Args:
        profile_url (string): profile link to search

    Returns:
        string: url of the profile picture
    """
    r = requests.get(profile_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    image_html = soup.find_all("div", {"class": "user-image"})

    extractor = URLExtract()
    image = extractor.find_urls(str(image_html[0]))

    return image[0]