import discord
from discord import SyncWebhook
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = discord.Client(intents=discord.Intents.all())
webhook = os.getenv("WEBHOOK")


@client.event
async def on_ready():
    ''' Sends up message to console '''
    print('Bot started with username: {0.user}'.format(client))


@client.event
async def on_message(message):
    ''' Listens for message event and reads command '''

    username = str(message.author).split('#')[0] # gets username of message author
    user_message = str(message.content) # gets content of message
    channel = str(message.channel.name) # gets name of current channel

    if message.author == client.user:
        return

    # only respond in current channel
    if channel == 'general':
        if user_message.lower().startswith('!anime'):
            keyword = user_message[7:].replace(" ", "%20") # parse the command out of the message, replace spaces with '%20'

            # parse MyAnimeList and return top 10 results
            r = requests.get(f'https://myanimelist.net/anime.php?q={keyword}&cat=anime')
            soup = BeautifulSoup(r.text, 'html.parser')
            results = soup.find_all('a', attrs={'class':'hoverinfo_trigger fw-b fl-l'})
            return_message = ""

            for i in range(10):
                results[i] = str(results[i].find('strong'))[8:-9]
                return_message += str(results[i]) + '\n'


            embed = discord.Embed(title=f'Results for: {SentenceCase(user_message[7:]).replace("%20", " ")}', description=f"{return_message}", color=0x36509D)
            await message.channel.send(embed=embed)
            return


def SentenceCase(sentence):
    ''' Takes in a sentence and then returns it with the first letter of each word capitalized '''
    return " ".join(word[0].upper()+word[1:] for word in sentence.split(" "))


if __name__ == "__main__":
    client.run(TOKEN)