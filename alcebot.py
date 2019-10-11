import discord
import asyncio
import re

class MyClient(discord.Client):
    async def on_ready(self):
    
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('with your emotions'))
        print('Logged in as:')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):

        if 'cookie' in message.content:
            await message.channel.send(':cookie:'.format(message))

        if 'poopoo' in message.content:
            await message.channel.send(':poop:'.format(message))

        if 'badass santa' in message.content:
            await message.channel.send(':santa: :gun:'.format(message))

        if 'test' in message.content:
            await message.channel.send(':beer:'.format(message))

client = MyClient()
client.run('NDgwNDUxNDM5MTgxOTU1MDkz.XaCDQg.wvCQm2H-K-5E41-0MJuEQYn6vEc')
