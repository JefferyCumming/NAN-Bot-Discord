import random
import discord
from discord.ext import commands
import urllib.request
from urllib.request import urlopen
import json

# Word bank for random text function
word_bank = ("Lemon", "Rag", "Goat", "Funk", "Crunch", "Suculant", "Tastey", "Juice", "Grilled", "Mario", "Hot", "Stink")

#Set Discord API bot token here
TOKEN = ''

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
    await bot.say(print(word_bank[random.randrange(0,16)] + ' ' + word_bank[random.randrange(0,16)] + ' ' + word_bank[random.randrange(0,16)] + ' ' + word_bank[random.randrange(0,16)]))


