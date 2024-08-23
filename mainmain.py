import discord
from discord.ext import commands
import random
import os
import requests
import kerasss
import omgg


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
async def img(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"./img/{dosya.filename}")
            await ctx.send("kaydedildi")
        sınıf, skor = kerasss.love (f"./img/{dosya.filename}")
        if sınıf == "kargalar\n":
            await ctx.send("karga tanındı")
        elemanlar=omgg.hermes(f"./img/{dosya.filename}")
        await ctx.send(elemanlar)
    else:
        await ctx.send("bir fotoğraf gönder")




