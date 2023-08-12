import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True
secilen_renk = ""
bot = commands.Bot(command_prefix='!', intents=intents)
ruletgecmis = []
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {ctx.author}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')
@bot.command()
async def rulet(ctx,arg):
    global secilen_renk
    global ruletgecmis
    renkler = ["Kırmızı","Siyah","Yeşil"]
    if arg not in renkler:
        await ctx.send("Geçersiz renk. Lütfen Kırmızı, Siyah veya Yeşil renklerinden birini seçin.")
        return  # Geçersiz renk seçildiğinde fonksiyonu sonlandır
    secilen_renk = random.choices(renkler, weights=[48,48,4], k=1)[0]
    if arg != secilen_renk:
        await ctx.send("Seçtiğiniz renk çıkmadı. Çıkan renk:{}".format(secilen_renk))
    else:
        await ctx.send("Kazandınız! Çıkan renk:{}".format(secilen_renk))
    #await ctx.send(secilen_renk)
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir(f'images/'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
def animal():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command()
async def animals(ctx):
    image_url = animal()
    await ctx.send(image_url)
@bot.command()
async def sil(ctx):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge()
        await ctx.channel.send("Tüm mesajlar silindi.")

bot.run("token")