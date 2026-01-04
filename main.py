import discord
from discord.commands import Option

intents = discord.Intents.default()



bot = discord.Bot(intents=intents,
                  debug_guilds=[947466334764171284]
                  )
async def on_ready():
    print(f'{bot.user} ist Online!')

@bot.slash_command(description="Sende GitHub Link")
async def github(ctx):
    await ctx.respond(f"Hallo der Github Link ist https://github.com/Andras1992/discordbot !")

@bot.slash_command(description="Sende eine Nachricht in einen Channel der Wahl")
async def say(ctx,
                 text: Option(str, "Der User den du benennen willst"),
                 channel: Option(discord.TextChannel, "Der Channel in den es soll"),
                 ):
       await channel.send(text)
       await ctx.respond("Die Nachricht wurde gesendet", ephemeral=True)

@bot.slash_command(description="Zeige die Infos von einem User!")
async def info(ctx,
               alter: Option(int, "Das Alter", min_value= 1, max_value= 99),
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
        embed.add_field(name="Alter", value = alter)
        embed.add_field(name="Account erstellt", value=time, inline=False)

        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"Das ist der Footer von {user.name}")


        await ctx.respond(embed=embed)

bot.run("DEIN DISCORD BOT TOKEN")