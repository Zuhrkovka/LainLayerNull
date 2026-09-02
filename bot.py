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
    await ctx.reply("Everything is connected!")


@bot.command()   
async def roll (ctx):
    await ctx.reply(f"Your random number is: {random.randint(1, 100)}")


@bot.command()
async def help(ctx):
    await ctx.send("""!hello = Everything is connected
                    !roll = throws a dice""")


@bot.command()
async def wc(ctx,  *,
message):
    characters = len(message)
    words = len(message.split())
    lines = len(message.splitlines())

    await ctx.reply(
        f"Characters: {characters}\n"
           f"Words:  {words} \n"
              f"Lines:  {lines}"
        )

bot.run(os.getenv("DISCORD_TOKEN"))
