from ast import keyword
import discord
from discord import SyncWebhook
from discord.utils import get
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()
TOKEN = os.getenv("TOKEN")
webhook = os.getenv("WEBHOOK")
client = discord.Client(intents=discord.Intents.all())
results = []
keyword = ""

@client.event
async def on_ready():
    ''' Sends up message to console '''
    print('Bot started with username: {0.user}'.format(client))

@client.event
async def on_message(message):
    ''' Listens for message event and reads command '''

    user_message = str(message.content) # gets content of message
    channel = str(message.channel.name) # gets name of current channel

    # only read human messages
    if message.author == client.user:
        return

    # only respond in current channel
    if channel == 'general':
        if user_message.lower().startswith('!anime'):
            await animeSearch(user_message, message)

        return

async def animeSearch(user_message, message):
    ''' Takes in user message as input and searches MyAnimeList for those keywords '''
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

    for reaction in reactions:
        await msg.add_reaction(reaction)

def get_url(keyword, position):
    ''' Takes in a keyword and a position, and returns the URL of the search result at that position '''

    # the index of the first search result in the array of links on the page is 93
    # there are 4 miscellaneous links between results, so for the next position, go 5 links down
    index = 93 + (5 * position)

    r = requests.get(f'https://myanimelist.net/anime.php?q={keyword}&cat=anime')
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')

    return links[index].get('href')

def get_description(url):
    ''' Get's the description from a URL of a specific anime '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    description_html = soup.find_all('p', attrs={'itemprop':'description'})

    description = str(description_html)[27:-5].replace('<br>', '\n').replace('<br/>', '')

    return description

@client.event
async def on_reaction_add(reaction, user):
    ''' Returns further information based on selection from list '''
    global keyword
    global results

    # if the bot is the one reacting, do nothing
    if reaction.message.author == user:
        return
    else:
        # send the selected name and corresponding description of the selected search result
        if reaction.emoji == '1️⃣':
            url = get_url(keyword, 0)
            description = get_description(url)
            embed = discord.Embed(title=f'{results[0]}', description=description, color=0x36509D)
            await reaction.message.channel.send(embed=embed)
        elif reaction.emoji == '2️⃣':
            url = get_url(keyword, 1)
            description = get_description(url)
            embed = discord.Embed(title=f'{results[1]}', description=description, color=0x36509D)
            await reaction.message.channel.send(embed=embed)
        elif reaction.emoji == '3️⃣':
            url = get_url(keyword, 2)
            description = get_description(url)
            embed = discord.Embed(title=f'{results[2]}', description=description, color=0x36509D)
            await reaction.message.channel.send(embed=embed)
        elif reaction.emoji == '4️⃣':
            url = get_url(keyword, 3)
            description = get_description(url)
            embed = discord.Embed(title=f'{results[3]}', description=description, color=0x36509D)
            await reaction.message.channel.send(embed=embed)
        elif reaction.emoji == '5️⃣':
            url = get_url(keyword, 4)
            description = get_description(url)
            embed = discord.Embed(title=f'{results[4]}', description=description, color=0x36509D)
            await reaction.message.channel.send(embed=embed)
    return

if __name__ == "__main__":
    client.run(TOKEN)
