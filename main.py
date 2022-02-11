from discord.ext import commands
import datetime
import ctx
import time
from datetime import datetime
import aiohttp
import random
import discord
from discord_slash import SlashContext, SlashCommand

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')

g = [937738822400221204]


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(name='Wer wird Millionär?', url='https://www.twitch.tv/clutcher'))
    print("Ready")

@client.command(aliase=["help"])
async def help(ctx):
    embed = discord.Embed(
        title="NoMercy",
        description=" ",
        color=0x0684f6, timestamp=datetime.utcnow()
    )
    embed.add_field(name="• Infos", value="!regeln, !gewinne, !userinfo", inline=False)
    embed.add_field(name="• Gewinnspiele", value="!rndm, !soon", inline=False)
    embed.add_field(name="• Fun Commands", value="!memes", inline=False)
    embed.add_field(name="• Unsere Links",
                    value="[YouTube](https://youtube.com/channel/UCXcXzOTIwLSsMXNoH77HgrQ) • [Twitch](https://twitch.tv/nomercy765) • [Insta]()")
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed)

@client.command(aliase=["regeln"])
async def regeln(ctx):
    embed = discord.Embed(
        title="Regeln",
        description="1. Teilnahme ab 14 Jahre \n 2. Wer kein Partner hat ist nicht Gewinnberechtigt. \n 3. Auszahlung bis 1k werden innerhalb von 6-12 Stunden ausgezahlt. Höhere Gewinne können sich bis zu 31 Tage verzögern. \n 4. PP wieder verfügbar \n 5. Gutscheine verfügbar, auch Psc. \n 6. Keine Stornierung mehr oder Gewinnsummen weniger machen. \n 7. Strenge Regeln, wer sie nicht folgt wird sofort gesperrt \n Eine Auszahlung des Gewinns in bar, in sonstigen Sachwerten, dessen Tausch oder Übertragung auf andere Personen ist nicht möglich. \n 8. Verfügbarkeit und Abbruch des Gewinnspiels \n Der Veranstalter weist darauf hin, dass die Verfügbarkeit und Funktion des Gewinnspiels nicht gewährleistet werden kann. Das Gewinnspiel kann aufgrund von äußeren Umständen und Zwängen beendet oder entfernt werden, ohne dass hieraus Ansprüche der Teilnehmer gegenüber dem Veranstalter entstehen. Ein Rechtsanspruch auf Auszahlung des Gewinns besteht nicht. \n 7. Haftung Für eine Haftung des Veranstalters auf Schadensersatz gelten unbeschadet der sonstigen gesetzlichen Anspruchsvoraussetzungen folgende Haftungsausschlüsse und Haftungsbegrenzungen: \n 7.1 Der Veranstalter haftet unbeschränkt, soweit die Schadensursache auf Vorsatz oder grober Fahrlässigkeit beruht. \n 7.2 Ferner haftet der Veranstalter für die leicht fahrlässige Verletzung von vertragswesentlichen Pflichten (Kardinalpflichten). In diesem Fall haftet der Veranstalter jedoch nur für den vorhersehbaren, vertragstypischen Schaden. \n 7.3 Die vorstehenden Haftungsbeschränkungen gelten nicht bei Verletzung von Leben, Körper und Gesundheit, für einen Mangel nach Übernahme von Beschaffenheitsgarantien für die Beschaffenheit eines Produktes und bei arglistig verschwiegenen Mängeln. Die Haftung nach dem Produkthaftungsgesetz bleibt unberührt. \n 7.4 Soweit die Haftung des Veranstalters ausgeschlossen oder beschränkt ist, gilt dies auch für die persönliche Haftung von Arbeitnehmern, Vertretern und Erfüllungsgehilfen des Veranstalters.",
        color=0x0684f6, timestamp=datetime.utcnow()
    )
    embed.add_field(name="• Unsere Links",
                    value="[Website](https://google.com) • [Donation](https://paypal.me/Julienodin123@gmail.com) • [Discord](https://discord.gg/Pv65gHTTmW)")
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong! 🏓")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong! 🏓 `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="Meme", description="", color=0xB980FF, timestamp=datetime.utcnow())

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            await ctx.send(embed=embed)

@client.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=f'Info for {member.display_name}',
                          color=0x0684f6, timestamp=datetime.utcnow())

    embed.add_field(name='Name', value=f"{member.name}#{member.discriminator}", inline=True)
    embed.add_field(name='Bot', value=f'{("Yes" if member.bot else "No")}', inline=True)
    embed.add_field(name='Nickname', value=f'{(member.nick if member.nick else "Not Set")}', inline=True)
    embed.add_field(name='Entered the Server', value=f'{member.joined_at}', inline=True)
    embed.add_field(name='Created Discord Accound', value=f'{member.created_at}', inline=True)
    embed.add_field(name='Roles', value=f'{len(member.roles)}', inline=True)
    embed.add_field(name='Highest Role', value=f'{member.top_role.name}', inline=True)
    embed.add_field(name='Farbe', value=f'{member.color}', inline=True)
    embed.add_field(name='Booster', value=f'{("Yes" if member.premium_since else "No")}', inline=True)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed)

@client.command()
async def rndm(ctx):
    embed = discord.Embed(title="Random Number",
                          description=f"{ctx.author.mention} your number is **{random.randint(1, 100)}**!",
                          color=0x7d00ff, )
    await ctx.send(embed=embed)

client.run("OTQxMzM2ODA4NDAxMjgxMDY0.YgUeOA.9kxsRN5VIQf91GcBH5lbjJZXgz0")
