import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ('h', 'H'))

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the fish cult.')

@client.event
async def on_member_remove(member):
    print(f'{member} has sinned and has been left to rot in a desert.')

#UWU Moderation
@client.event
async def on_message(message):
    if 'helo' in message.content.lower():
        print('Someone has summoned the fish lord.')
        await message.channel.send('Someone has summoned the fish lord.\nhttps://shorturl.at/eg267')

    if 'uwu' in message.content.lower():
        print('Someone has dared to utter the forbidden word.')
        await message.channel.send('Someone has dared to utter the forbidden word.')

client.run('NzEwODI2OTU1NDAxOTg2MDY4.Xr6kBA.f2lWX-L6gv6w4C8EY17Dgbkxk04')
