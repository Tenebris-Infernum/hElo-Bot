import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = ('h', 'H'))
ROLE = 'shame'

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the fish cult.')

@client.event
async def on_member_remove(member):
    print(f'{member} has sinned and has been left to rot in a desert.')

@client.event
async def on_message(message):

    #Fish Helo Meme
    if 'helo' in message.content.lower():
        await message.channel.send(str(message.author) + ' has summoned the fish lord.\nhttps://imgur.com/a/BxMCgvh')

    #UWU Moderation
    if 'uwu' in message.content.lower():
        await message.channel.send(str(message.author) + ' has uttered the forbidden word. You shall now persish.')
        role = get(message.author.guild.roles, name=ROLE)
        await message.author.add_roles(role)

client.run('NzEwODI2OTU1NDAxOTg2MDY4.Xr6kBA.f2lWX-L6gv6w4C8EY17Dgbkxk04')
