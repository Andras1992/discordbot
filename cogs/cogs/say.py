import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option


class Say(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot


@slash_command(description="Sende eine Nachricht in einen Channel der Wahl")
async def say(ctx,
              text: Option(str, "Der User den du benennen willst"),
              channel: Option(discord.TextChannel, "Der Channel in den es soll"),
              ):
    await channel.send(text)
    await ctx.respond("Die Nachricht wurde gesendet", ephemeral=True)


def setup(bot: discord.Bot):
    bot.add_cog(Say(bot))
