import random
import discord
from discord.ext import commands
import urllib.request
from urllib.request import urlopen
import json

# Word bank for random text function
nouns = ("Lemon", "Rag", "Goat", "Funk", "Crunch", "Suculant", "Tastey", "Juice", "Grilled", "Mario", "Stink")
adjectives = ("Stinky", "Smelly", "Funky", "Breaded", "Soaked", "Sour", "Sweet")

#Set Discord API bot token here
TOKEN = 'Njg3MDgzNDE1NzA2NTMzOTUy.Xsb05w._Gct2Z0ESuZUHniWQtTixj6qbmA'

description = "Sandwich text using NAN"
bot = commands.Bot(command_prefix='!', description=description)




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def start():
    await bot.say(print(adjectives[random.randrange(0,16)] + ' ' + nouns[random.randrange(0,16)] + ' ' + adjectives[random.randrange(0,16)] + ' ' + nouns[random.randrange(0,16)]))


