import discord
import os
from dotenv import load_dotenv
from discord.commands import Option

intents = discord.Intents.default()
intents.members = True


bot = discord.Bot(intents=intents,
                  debug_guilds=[947466334764171284]
                  )
async def on_ready():
    print(f'{bot.user} ist Online!')

if __name__ == "__main__":

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

load_dotenv()
bot.run(os.getenv("TOKEN"))