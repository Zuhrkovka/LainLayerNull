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
                            !roll = throws a dice
                                  !wc = counts numbers and line output""")


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

@bot.command()
async def dice(ctx):
    first_roll = random.randint(1, 6)

    await ctx.reply(
           f"i rolled a **{first_roll}**.\n"
                           "will the next roll be **lower** or **higher**?"
       )

    def check(message):
        return
message.author ==
ctx.author and
message.channel ==
ctx.channel

     try:
          answer = await
bot.wait_for("message",
             check=check, timeout=30)

          answer =
answer.content.lower().str
ip()

          if answer not in
["lower", "higher"]:
           await 
ctx.reply("You need to answer **lower** or **higher**.") 

return

           second_roll =
random.randint(1, 6)

        if second_roll ==
first_roll:
            result = "It´s the same number! You lose."

        elif answer == 
"higher" and second_roll <
first roll:

            result = "you guessed correctly! **you win!**"

        elif answer == 
        "lower" and second_roll <
        first roll:
        
                    result = "you guessed correctly! **you win!**"

        else:
            result = "Wrong guess! **You lose!**"

                      await ctx.reply(
                             f"The second roll is **{second_roll}**.
                             \n {result}"
                      )
        
              except TimeoutError:
                  await
ctx.reply("you took too long to answer.")



bot.run(os.getenv("DISCORD_TOKEN"))
