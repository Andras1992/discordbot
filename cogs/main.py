import discord
import os
from discord.commands import Option

intents = discord.Intents.default()
intents.members = True


bot = discord.Bot(intents=intents,
                  debug_guilds=[947466334764171284]
                  )
async def on_ready():
    print(f'{bot.user} ist Online!')


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run("DEIN BOT TOKEN")