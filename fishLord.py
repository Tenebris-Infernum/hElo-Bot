import discord
from discord.ext import commands
from discord.utils import get
import time

client = commands.Bot(command_prefix = ('h', 'H'))
shameRole = 'Pit Of Shame'
timeAmount = time.time() + 60

#When the bot has connected to the server
@client.event
async def on_ready():
    print('Bot is ready.')

#When a member has joins the server
@client.event
async def on_member_join(member):
    await member.send(f'Welcome {member} to the fish cult.')

#When a member leaves the server
@client.event
async def on_member_remove(member):
    await member.send(f'You have been kicked from the fish cult for you have displeased the fish lord .')

#When someone leaves a voice channel
@client.event
async def on_voice_state_update(member):
    username = str(member).split('#', 1)
    

#When a certain word in a message is detected
@client.event
async def on_message(message):
    
    #Fish Helo Meme
    if 'helo' in message.content.lower():
        username = str(message.author).split('#', 1)
        await message.channel.send(str(username[0]) + ' has summoned the fish lord. \nhttps://imgur.com/a/BxMCgvh')

    #Hello There
    if 'hello there' in message.content.lower():
        username = str(message.author).split('#', 1)
        await message.channel.send('General Kenobi')

    #UWU Moderation
    if 'uwu' in message.content.lower():
        username = str(message.author).split('#', 1)
        await message.channel.send(str(username[0]) + ' has uttered the forbidden word. Perish, mortal.')
        role = get(message.author.guild.roles, name=shameRole)
        while time.time() < timeAmount:
            await message.author.add_roles(role)
        await message.author.remove_roles(role)

#Token used to connect code to bot     
client.run('NzEwODI2OTU1NDAxOTg2MDY4.XsDQUw.hhZLzZYDu2i0fYqRxgmW5E0O81c')
