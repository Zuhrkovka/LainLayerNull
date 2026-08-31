import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Everything is connected!")


@bot.command()   
async def roll (ctx):
    await ctx.reply(f"Your random number is: {random.randint(1, 100)}")


bot.run(os.getenv("DISCORD_TOKEN"))
