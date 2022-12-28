import discord
from discord import SyncWebhook
from discord.utils import get
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from urlextract import URLExtract

from ProfileSearch import *
from AnimeSearch import *

# loading in token and webhook from .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
webhook = os.getenv("WEBHOOK")

# global variables
client = discord.Client(intents=discord.Intents.all())
results = []
keyword = ""
first_reaction = True

@client.event
async def on_ready():
    """Sends up message to console"""
    print('Bot started with username: {0.user}'.format(client))

@client.event
async def on_message(message):
    """Listens for message event and reads command

    Args:
        message (message): the latest message sent
    """
    global first_reaction

    user_message = str(message.content) # gets content of message

    # only read human messages
    if message.author == client.user:
        return

    # !anime command
    if user_message.lower().startswith('!anime'):
        # every new command, send a new embed (see on_reaction_add method)
        first_reaction = True
        await animeSearch(user_message, message)

    if user_message.lower().startswith('!profile'):
        await profileSearch(user_message, message)
    return

async def animeSearch(user_message, message):
    """Takes in user message as input and searches MyAnimeList for those keywords

    Args:
        user_message (string): CONTENT of the message
        message (message): message OBJECT
    """
    global results
    global keyword
    keyword = user_message[7:].replace(" ", "%20") # parse the command out of the message, replace spaces with '%20'

    # parse MyAnimeList and return top 10 results
    r = requests.get(f'https://myanimelist.net/anime.php?q={keyword}&cat=anime')
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('a', attrs={'class':'hoverinfo_trigger fw-b fl-l'})
    return_message = ""

    # take the top 5 results from MyAnimeList
    for i in range(0, 5, 1):
        results[i] = str(results[i].find('strong'))[8:-9]
        return_message += f'{i + 1}. {str(results[i])}\n'

    # send message as embed and set reaction buttons 1-5
    embed = discord.Embed(title=f'Results for: {keyword.replace("%20", " ")}', description=f"{return_message}", color=0x36509D)
    msg = await message.channel.send(embed=embed)
    reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]

    # add reactions
    for reaction in reactions:
        await msg.add_reaction(reaction)

async def profileSearch(user_message, message):
    """Searches for an MAL profile and returns its stats

    Args:
        user_message (string): the message from the user command containing the profile to search for
        message (string): message object
    """
    # parse the "!profile " part out
    profile_name = user_message[9:]
    profile_url = f'https://myanimelist.net/profile/{profile_name}'
    r = requests.get(profile_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # if the request returns a error 404 (profile not found)
    if r.ok:
        embed = discord.Embed(title="MyAnimeList Profile", url=profile_url, color=0x00DBFF)
        embed.set_author(name=profile_name)
        embed.set_thumbnail(url=getProfilePicture(profile_url))
        embed.add_field(name="Anime Stats:", value=f"Days watched: {getDays(profile_url, 0)}\nEpisodes: {getEpisodes(profile_url)}\nWatching: {getWatching(profile_url)}\n Completed: {getCompleted(profile_url)}", inline=True)
        embed.add_field(name="Manga Stats:", value=f"Days read: {getDays(profile_url, 1)}\nChapters: \nReading: \n Completed: ", inline=True)
    else:
        embed = discord.Embed(title="Profile not found. ", description="Please enter a valid profile name.", color=0xFF0000)
        embed.set_thumbnail(url='https://64.media.tumblr.com/1e8b63b8e33978d7d5ef5019f32c5930/aebf5a6e89fb27e4-db/s400x600/37381ac3b8ae4be3df56bf18d20fcebf0fc00aa0.png')

    await message.channel.send(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    """Expands on description when reaction is pressed

    Args:
        reaction (reaction): reaction object
        user (user): user who reacted
    """
    global keyword
    global results
    global first_reaction
    global send

    # if the bot is the one reacting, do nothing
    if reaction.message.author == user:
        return
    else:
        # send the selected name and corresponding description of the selected search result
        if reaction.emoji == '1️⃣':
            await reaction.remove(user)
            url = getUrl(keyword, 0)
            description = getDescription(url)
            embed = discord.Embed(title=f'{results[0]}', url=url, description=description, color=0x36509D)
            embed.set_thumbnail(url=getImage(url))
            if first_reaction:
                send = await reaction.message.channel.send(embed=embed)
                first_reaction = False
            else:
                await send.edit(embed=embed)
        elif reaction.emoji == '2️⃣':
            await reaction.remove(user)
            url = getUrl(keyword, 1)
            description = getDescription(url)
            embed = discord.Embed(title=f'{results[1]}', url=url, description=description, color=0x36509D)
            embed.set_thumbnail(url=getImage(url))
            if first_reaction:
                send = await reaction.message.channel.send(embed=embed)
                first_reaction = False
            else:
                await send.edit(embed=embed)
        elif reaction.emoji == '3️⃣':
            await reaction.remove(user)
            url = getUrl(keyword, 2)
            description = getDescription(url)
            embed = discord.Embed(title=f'{results[2]}', url=url, description=description, color=0x36509D)
            embed.set_thumbnail(url=getImage(url))
            if first_reaction:
                send = await reaction.message.channel.send(embed=embed)
                first_reaction = False
            else:
                await send.edit(embed=embed)
        elif reaction.emoji == '4️⃣':
            await reaction.remove(user)
            url = getUrl(keyword, 3)
            description = getDescription(url)
            embed = discord.Embed(title=f'{results[3]}', url=url, description=description, color=0x36509D)
            embed.set_thumbnail(url=getImage(url))
            if first_reaction:
                send = await reaction.message.channel.send(embed=embed)
                first_reaction = False
            else:
                await send.edit(embed=embed)
        elif reaction.emoji == '5️⃣':
            await reaction.remove(user)
            url = getUrl(keyword, 4)
            description = getDescription(url)
            embed = discord.Embed(title=f'{results[4]}', url=url, description=description, color=0x36509D)
            embed.set_thumbnail(url=getImage(url))
            if first_reaction:
                send = await reaction.message.channel.send(embed=embed)
                first_reaction = False
            else:
                await send.edit(embed=embed)
    return

if __name__ == "__main__":
    try:
        client.run(TOKEN)
    except:
        print("\nERROR: Client can't be run with token. Is .env file properly imported?")