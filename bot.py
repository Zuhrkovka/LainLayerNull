import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# User who is banned from using !slap — gets roasted instead if he tries.
BASSUS_ID = 709851355371536454

BASSUS_ROASTS = [
    "Nice try, bassus. You don't get to slap people.",
    "Denied. grow some hair on your forehead.",
    "bassus, sit down. The last thing you should be swinging is your ass out of this conversation.",
    "Not happening, bassus. This command has higher standards than your dad in the gay club.",
    "bassus trying to slap someone is like a Roomba trying to headbutt a wall — pointless and slightly sad.",
    "Access denied. bassus's slap privileges were repossessed, like his dignity.",
    "You really thought you'd get to slap someone, bassus? Adorable.",
    "bassus, the bot has more self-respect than to let you touch this command.",
]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.reply("Everything is connected!")


@bot.command()
async def roll(ctx):
    await ctx.reply(f"Your random number is: {random.randint(1, 100)}")


@bot.command()
async def help(ctx):
    await ctx.reply("Here are the commands you can use:\n- `!hello`: Say hello to the bot\n- `!roll`: Roll a random number between 1 and 100\n- `!coin`: Flip a coin\n- `!dice`: Play a dice game\n- `!kiss @member`: Kiss a member\n- `!hug @member`: Hug a member \n- `!slap @member`: Slap a member")


@bot.command()
async def coin(ctx):
    coin_flip = random.choice(["Heads", "Tails"])
    await ctx.reply(f"The coin landed on: **{coin_flip}**")


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


kiss_gif = [
    "gifs/kiss/giphy.gif",
    "gifs/kiss/giphy2.gif",
    "gifs/kiss/giphy3.gif",
    "gifs/kiss/giphy4.gif",
    "gifs/kiss/giphy5.gif",
    "gifs/kiss/giphy6.gif",
    "gifs/kiss/giphy7.gif",
    "gifs/kiss/giphy8.gif",
    "gifs/kiss/giphy9.gif",
    "gifs/kiss/giphy10.gif",
]
hug_gif = [
    "gifs/hug/giphy(1).gif",
    "gifs/hug/giphy2h.gif",
    "gifs/hug/giphy3h.gif",
    "gifs/hug/giphy4h.gif",
    "gifs/hug/giphy5h.gif",
    "gifs/hug/giphy6h.gif",
    "gifs/hug/giphy7h.gif",
    "gifs/hug/giphy8h.gif",
    "gifs/hug/giphy9h.gif",
    "gifs/hug/giphy10h.gif",
]
slap_gif = [
    "gifs/slap/giphy1s.gif",
    "gifs/slap/giphy2s.gif",
    "gifs/slap/giphy3s.gif",
    "gifs/slap/giphy4s.gif",
    "gifs/slap/giphy5s.gif",
]


@bot.command()
async def kiss(ctx, member: discord.Member):
    gif = random.choice(kiss_gif)

    await ctx.reply(
        f"{ctx.author.mention} kissed {member.mention} 💋",
        file=discord.File(gif)
    )


@bot.command()
async def hug(ctx, member: discord.Member):
    gif = random.choice(hug_gif)

    await ctx.reply(
        f"{ctx.author.mention} hugged {member.mention}",
        file=discord.File(gif)
    )


@bot.command()
async def slap(ctx, member: discord.Member):
    if ctx.author.id == BASSUS_ID:
        await ctx.reply(random.choice(BASSUS_ROASTS))
        return

    gif = random.choice(slap_gif)

    await ctx.reply(
        f"{ctx.author.mention} slapped {member.mention}",
        file=discord.File(gif)
    )


@kiss.error
async def kiss_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You need to mention a member to kiss.")


@hug.error
async def hug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You need to mention a member to hug.")


@slap.error
async def slap_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.author.id == BASSUS_ID:
            await ctx.reply(random.choice(BASSUS_ROASTS))
        else:
            await ctx.reply("You need to mention a member to slap.")


bot.run(os.getenv("DISCORD_TOKEN"))