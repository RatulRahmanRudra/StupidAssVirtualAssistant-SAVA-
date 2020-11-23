from asyncio.tasks import wait
from os import name
import discord
from discord import channel 
from discord.ext import commands, tasks
import random
from youtube_search import YoutubeSearch as yt_search
import os
from voice_com import speak, take_command
import voice_com



# handle voice commands

activeDiscord = False



client = commands.Bot(command_prefix='>')

token = 'Nzc3MTUwMjMxNTQzNTQ1ODg3.X6_PjQ.s3_NwHkHCfn_EP6gcPT93kafpqs'

status = ['to Bang!', 'lost!', 'for a new girl', 'to jack off']
greetings = ['wassup nigga', "how's it hanging", 'fuck off', 'yo dumbass']

channel  = discord.Object(id='776916632483397664')


@client.event
async def on_ready():
    change_status.start()
    print('bot is on')
    activeDiscord = True
    speak('we are currently in bot script & bot is running')
    # run_commands()
    
    
    

@tasks.loop(seconds=random.randrange(20, 300))
async def change_status():
    await client.change_presence(activity=discord.Game(random.choice(status)))


@client.command(name='ping', help='this command returns latency')
async def ping(ctx):
    await ctx.send(f'u r fucking {round(client.latency*1000)} ms late bitch')


@client.command(name='hello', help = 'gives you a random greetings!', aliases = ['yo', 'wassup'])
async def hello(ctx):
    await ctx.send(random.choice(greetings))

@client.command(name='play', help = 'plays the song on voice command given from local server', aliases = ['p', 'pp'])
async def play(ctx):
    speak('what do you want to say')
    search = take_command()
    await ctx.send(search)

def run_commands():
    speak('What do you want to search?')
    try :
        search = take_command()
        yt = voice_com.get_yt(search) # its a list [id, title]
        return yt[1]
    except Exception as e :
        speak(str(e))
                


                
# async with 



