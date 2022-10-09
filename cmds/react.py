import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
with open('./setting/setting.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)

owner=(int(jdata['OWNER_ID']))

class React(Cog_Extension):

    @commands.command()
    async def holo(self,ctx):
        holo = random.choice(jdata['holo_url_pic'])
        await ctx.send(holo)
    @commands.command()
    async def holoen(self,ctx):
        holo = random.choice(jdata['holoen_url'])
        await ctx.send(holo)
    @commands.command()
    async def srn(self,ctx):
        srn = random.choice(jdata['sp_url'])
        await ctx.send(srn)
    @commands.command()
    async def 運勢占卜(self,ctx):
        fortune = random.choice(jdata['fortune'])
        await ctx.send(f'今日你的運勢是...||{fortune}!||')


    @commands.command()
    async def upsrn(self,ctx,urlp):
        if ctx.message.author.id==owner:
            if urlp in jdata["sp_url"]:
                await ctx.send('這個圖片已經存在於檔案夾內囉~')
            else:
                jdata["sp_url"].append(urlp)
                await ctx.send('已經把圖片儲存至檔案夾內囉~')
        else:
            await ctx.send(f'你無開發者權限無法使用該指令')
        with open('./setting/setting.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.command()
    async def resrn(self,ctx,urlp):
        if ctx.message.author.id==owner:
            if urlp in jdata["sp_url"]:
                jdata["sp_url"].remove(urlp)
                await ctx.send('已經把圖片從檔案夾內刪除囉~')
            else:
                await ctx.send('這個圖片不存在於檔案夾內喔~')
        else:
            await ctx.send(f'你無開發者權限無法使用該指令')
        with open('./setting/setting.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)
    @commands.command()
    async def srnc(self,ctx):
        list=jdata['sp_url']
        await ctx.send(f'目前資料庫內有{len(list)}筆資料喔~')
        


def setup(maple):
    maple.add_cog(React(maple))