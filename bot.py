from fileinput import filename
import discord
from discord.ext import commands
import json
import random
import os
with open('./setting/setting.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)
# intents=discord.Intents.all()

owner=(int(jdata['OWNER_ID']))

maple = commands.Bot(command_prefix='!!', intents=discord.Intents.all())
# maple.remove_command('help')
#event為事件
@maple.event #機器人上線通知
async def on_ready():
    print(">>DC測試機已上線<<")

@maple.command()
@commands.is_owner()
async def load(ctx,extention):
    maple.load_extension(f'cmds.{extention}')
    await ctx.send(f'已經重新讀取{extention}囉')

@maple.command()
@commands.is_owner()
async def unload(ctx,extention):
    maple.unload_extension(f'cmds.{extention}')
    await ctx.send(f'這個{extention}資料已經卸除了')

@maple.command()
@commands.is_owner()
async def reload(ctx,extention):
    maple.reload_extension(f'cmds.{extention}')
    await ctx.send(f'重新讀取到了{extention}這個檔案了')

#連結,讀取資料夾

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        maple.load_extension(f'cmds.{filename[:-3]}')


if __name__ == "__main__":
    maple.run(jdata['TOKEN'])