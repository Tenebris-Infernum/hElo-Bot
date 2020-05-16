import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ('h', 'H'))

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    #print(f'{member} has joined the fish cult.') # this and line 17 produce a syntax error for some reason
    print('Someone has joined the fish cult.')

@client.event
async def on_member_remove(member):
    #print(f'{member} has sinned and has been left to rot in a desert.')
    print('Someone has sinned and has been left to rot in a desert.')

#UWU Moderation
@client.event
async def on_message(message):
    if 'helo' in message.content.lower():
        if str(message.author) == "Tenebris#3685":
            print('Tenebris has summoned the fish lord.')
            await message.channel.send('Tenebris has summoned the fish lord.\nhttps://shorturl.at/eg267')
        
        if str(message.author) == "azure#2467":
            print('Azure has summoned the fish lord.')
            await message.channel.send('Azure has summoned the fish lord.\nhttps://shorturl.at/eg267')

        if str(message.author) == "JVT038#2995":
            print('JVT038 has summoned the fish lord.')
            await message.channel.send('JVT038 has summoned the fish lord.\nhttps://shorturl.at/eg267')
        
        if str(message.author) == "sn4k3_ch4rm3r#6736":
            print('Longjumping_Flamingo has summoned the fish lord.')
            await message.channel.send('Longjumping_Flamingo has summoned the fish lord.\nhttps://imgur.com/a/BxMCgvh')
        
        if str(message.author) == "Koalo#2322":
            print('insane_playzYT has summoned the fish lord.')
            await message.channel.send('insane_playzYT has summoned the fish lord.\nhttps://imgur.com/a/BxMCgvh')
        
        if str(message.author) == "Bassab03#2609":
            print('Bassab has summoned the fish lord.')
            await message.channel.send('Bassab has summoned the fish lord.\nhttps://imgur.com/a/BxMCgvh')

        if str(message.author) == "Spurtle#7680":
            print('haistv has summoned the fish lord.')
            await message.channel.send('haistv has summoned the fish lord.\nhttps://imgur.com/a/BxMCgvh')
        
        if str(message.author) == "Haritoo#3941":
            print('Haritoo has summoned the fish lord.')
            await message.channel.send('Haritoo has summoned the fish lord.\nhttps://imgur.com/a/BxMCgvh')
        
        if str(message.author) == "suspiciousvegetable#0015":
            print('Our lord has summoned the fish lord.')
            await message.channel.send('Our lord has summoned the fish lord.\nhttps://imgur.com/a/BxMCgvh')


    if 'uwu' in message.content.lower():
        if str(message.author) == "Tenebris#3685":
            print('Tenebris has uttered the forbidden word.')
            await message.channel.send('Tenebris has uttered the forbidden word.')
        
        if str(message.author) == "azure#2467":
            print('Azure has uttered the forbidden word.')
            await message.channel.send('Azure has uttered the forbidden word.')

        if str(message.author) == "JVT038#2995":
            print('JVT038 has uttered the forbidden word.')
            await message.channel.send('JVT038 has uttered the forbidden word.')
        
        if str(message.author) == "sn4k3_ch4rm3r#6736":
            print('Longjumping_Flamingo has uttered the forbidden word.')
            await message.channel.send('Longjumping_Flamingo has uttered the forbidden word.')
        
        if str(message.author) == "Koalo#2322":
            print('insane_playzYT has uttered the forbidden word.')
            await message.channel.send('insane_playzYT has uttered the forbidden word.')
        
        if str(message.author) == "Bassab03#2609":
            print('Bassab has uttered the forbidden word.')
            await message.channel.send('Bassab has uttered the forbidden word.')

        if str(message.author) == "Spurtle#7680":
            print('haistv has uttered the forbidden word.')
            await message.channel.send('haistv has uttered the forbidden word.')
        
        if str(message.author) == "Haritoo#3941":
            print('Haritoo has uttered the forbidden word.')
            await message.channel.send('Haritoo has uttered the forbidden word.')
        
        if str(message.author) == "suspiciousvegetable#0015":
            print('Our lord has uttered the forbidden word.')
            await message.channel.send('Our lord has uttered the forbidden word.')

client.run('NzEwODI2OTU1NDAxOTg2MDY4.Xr6kBA.f2lWX-L6gv6w4C8EY17Dgbkxk04')
