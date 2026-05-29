# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN').strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)
