import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def aaaa(ctx):
    await ctx.send(f'noldu?')

@bot.command()
async def ampulcalismiyor(ctx):
    await ctx.send(f'bir de ben bakayım..')

@bot.command()
async def noldu(ctx):
    await ctx.send(f'ampul calismiyor')

@bot.command()
async def ciddiolamassın(ctx):
    await ctx.send(f'')

kshdgflşksdgafjhafsdflaşkjdfslşkjsdf



@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("GİZLİ TOKEN BURAYA")
