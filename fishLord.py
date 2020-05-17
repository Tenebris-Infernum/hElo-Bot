import discord
from discord.ext import commands
from discord.utils import get
import time

client = commands.Bot(command_prefix = ('h', 'H'))
shameRole = 'Pit Of Shame'

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    await member.send(f'Welcome {member} to the fish cult.')

@client.event
async def on_member_remove(member):
    await member.send(f'You have been kicked from the fish cult for you have displeased the fish lord .')

@client.event
async def on_message(message):

    #Fish Helo Meme
    if 'helo' in message.content.lower():
        await message.channel.send(str(message.author) + ' has summoned the fish lord.\nhttps://imgur.com/a/BxMCgvh')

    #UWU Moderation
    if 'uwu' in message.content.lower():
        await message.channel.send(str(message.author) + ' has uttered the forbidden word. You shall now persish.')
        role = get(message.author.guild.roles, name=shameRole)
        await message.author.add_roles(role)
        time.sleep(60)
        await message.author.remove_roles(role)

client.run('enter token here')
