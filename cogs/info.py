import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option


class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@slash_command(description="Zeige die Infos von einem User!")
async def info(ctx,
               alter: Option(int, "Das Alter", min_value=1, max_value=99),
               user: Option(discord.Member, "Gib einen User an", default=None)
               ):
        if user is None:
            user = ctx.author

            embed = discord.Embed(
                title=f"Infos über {user.name}",
                description=f"Hier sieht du alle Details über {user.mention}!",
                color=discord.Color.brand_red()
                )

            time = discord.utils.format_dt(user.created_at, "R")
            embed.add_field(name="ID", value=user.id)
            embed.add_field(name="Alter", value=alter)
            embed.add_field(name="Account erstellt", value=time, inline=False)

            embed.set_thumbnail(url=user.display_avatar.url)
            embed.set_footer(text=f"Das ist der Footer von {user.name}")

            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))

