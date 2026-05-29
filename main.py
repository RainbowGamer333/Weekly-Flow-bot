# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('TOKEN').strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
    
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if message.content.startswith('!start'):
            print("Starting the printing task...")
            my_cog = MyCog(bot)
            my_cog.printing.start()

    @tasks.loop(seconds=5.0)
    async def printing(self):
        print(self.index)
        self.index += 1
    
    @printing.before_loop
    async def before_printing(self):
        print('Waiting until the bot is ready...')
        await self.bot.wait_until_ready()
    
bot.run(TOKEN)
