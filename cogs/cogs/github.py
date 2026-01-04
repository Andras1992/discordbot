import discord
from discord.ext import commands
from discord.commands import slash_command


class Github(commands.Cog):
    def __init__(self, bot: discord.bot):
        self.bot = bot

@slash_command(description="Sende GitHub Link")
async def github(ctx):
    await ctx.respond(f"Hallo der Github Link ist https://github.com/Andras1992/discordbot !")


def setup(bot: discord.bot):
    bot.add_cog(Github(bot))