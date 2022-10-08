import discord

TOKEN = 'MTAyODM0NDM0ODAyODQ0MDcwNw.G0rNoo.sTjbnrLcdLWFYqESG4_qfeSwRDVWxhDec2fUZ4'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    # only respond in current channel
    if message.channel.name == 'general':
        if user_message.lower().startswith('!anime'):
            keyword = user_message[11:].replace(" ", "%20") # parse the command out of the message, replace spaces with '%20'
            await message.channel.send(f'https://myanimelist.net/search/all?q={keyword}&cat=all')
            return
        else:
            await message.channel.send(f'Bye {username}!')
            return

client.run(TOKEN)