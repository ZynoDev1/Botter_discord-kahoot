import discord
import time
from discord.ext import commands

token = ""
intents = discord.Intents.default()
pin_filename = "pins.txt"
amount_filename = "botammount.txt"
prefix = "!"

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    with open("pins.txt", "w") as pin_file:
        pin_file.write("")
    with open("botammount.txt", "w") as amount_file:
        amount_file.write("")
    await bot.change_presence(activity=discord.Game(name="!help | by Zyno"))
@bot.command(name="help", description="deuug")
async def help(ctx):
    embed=discord.Embed(title="Kahoot botter ", description="USAGE **!start <pin> <ammount_of_bots>**", color=0xcc1e1e)
    await ctx.send(embed=embed)
@bot.command(name="start", description="Please specify pin as well as the amount of bots")
async def start(ctx, pin: int = -1, amount: int = -1):
    await ctx.send(f"Flooding the kahoot {pin} with {amount} bots ")
    await ctx.send("Writing to file!")
    with open(pin_filename, "w") as pin_file:
        pin_file.write(str(pin))
    with open(amount_filename, "w") as amount_file:
        amount_file.write(str(amount))
    await ctx.send("Loading shit :/ :D :skull:  . . . . . .")
    print(f"""
        Logs (IGNORE)
        wrote {amount} to file

        wrote {pin} to file """)
    time.sleep(5)
    embed=discord.Embed(title="Kahoot botter ", description="**Botting the kahoot with PIN** "+(str(pin))+" **Sending** "+str(amount)+" **bots**  *ETA Depending on req*", color=0xcc1e1e)
    embed.add_field(name="A tool made by Zyno ", value="", inline=False)
    await ctx.send(embed=embed)
bot.run(token)
