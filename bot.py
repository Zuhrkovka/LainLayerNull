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
    await ctx.reply("Here are the commands you can use:\n- `!hello`: Say hello to the bot\n- `!roll`: Roll a random number between 1 and 100\n- `!coin`: Flip a coin\n- `!dice`: Play a dice game")


@bot.command()
async def dice(ctx):
    first_roll = random.randint(1, 6)

    await ctx.reply(
        f"I rolled a **{first_roll}**.\n"
        "Will the next roll be **lower** or **higher**?"
    )

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        answer = await bot.wait_for("message", check=check, timeout=30)

        answer = answer.content.lower().strip()

        if answer not in ["lower", "higher"]:
            await ctx.reply("You need to answer **lower** or **higher**.")
            return

        second_roll = random.randint(1, 6)

        if second_roll == first_roll:
            result = "It's the same number! You lose."

        elif answer == "higher" and second_roll > first_roll:
            result = "You guessed correctly! **You win!**"

        elif answer == "lower" and second_roll < first_roll:
            result = "You guessed correctly! **You win!**"

        else:
            result = "Wrong guess! **You lose!**"

        await ctx.reply(
            f"The second roll is **{second_roll}**.\n{result}"
        )

    except TimeoutError:
        await ctx.reply("You took too long to answer.")


bot.run(os.getenv("DISCORD_TOKEN"))
