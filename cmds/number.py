import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
with open('./setting/number.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)
owner=560091826170626071

class Number(Cog_Extension):
    @commands.command()                 #啟動遊戲
    async def bingo(self,ctx):
        user=ctx.author.mention
        min=jdata[str(ctx.guild.id)]["min"]
        max=jdata[str(ctx.guild.id)]["max"]
        count=jdata[str(ctx.guild.id)]["count"]
        lastnumber=random.randint(min,max)
        jdata[str(ctx.guild.id)].update({"lastnumber":lastnumber})
        await ctx.send(f"{user}已開始遊戲,請在{min}到{max}中找到正確數字,總共有{count}次機會~")
        with open('./setting/number.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.command()                 #猜數字
    async def b(self,ctx,num:int):
        user=ctx.author.mention
        min=jdata[str(ctx.guild.id)]["min"]
        max=jdata[str(ctx.guild.id)]["max"]
        count=jdata[str(ctx.guild.id)]["count"]
        lastnumber=jdata[str(ctx.guild.id)]["lastnumber"]
        if count != 0:
            if num < lastnumber:
                count1=count-1
                await ctx.send(f"{user}比{num}大喔~次數剩餘{count1}")
            if num > lastnumber:
                count1=count-1
                await ctx.send(f"{user}比{num}小喔~次數剩餘{count1}")
            if num == lastnumber:
                count1=count-1
                await ctx.send(f"{user}正確答案!,答案是{lastnumber}!")
        else:
            await ctx.send(f"{user}該局次數用盡囉~")
        
        jdata[str(ctx.guild.id)].update({"count":count1})
        with open('./setting/number.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)


    @commands.command()                 #遊戲設定
    async def bs(self,ctx,min:int,max:int,count:int):
        if 0<count<10000:
            if min>=0 & min<max & max>min+10 & max<10000:
                jdata[str(ctx.guild.id)].update({"min":min})
                jdata[str(ctx.guild.id)].update({"max":max})
                jdata[str(ctx.guild.id)].update({"count":count})
                await ctx.send(f"""數字已確認
```最小數字:{min},最大數字:{max},嘗試次數:{count}```""")
                with open('./setting/number.json','w',encoding='utf8') as mlink:
                    json.dump(jdata,mlink,indent=4)
            else:
                await ctx.send(f"最大數值**大於**最小數值,最大數值沒有**超過**最小數字+10或是最小數值低於0,因此條件不成立喔")
        else:
            await ctx.send(f"次數大於9999或小於1,所以條件不成立")

    @commands.command()
    async def stopbingo(self,ctx):
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            await ctx.send(f'已強制停止遊戲***stop***!!!')
            jdata[str(ctx.guild.id)].update({"lastnumber":0})
            jdata[str(ctx.guild.id)].update({"min":0})
            jdata[str(ctx.guild.id)].update({"max":0})
            jdata[str(ctx.guild.id)].update({"count":0})
            with open('./setting/number.json','w',encoding='utf8') as mlink:
                json.dump(jdata,mlink,indent=4)
        else:
            await ctx.send(f'你非開發者或管理員無法使用該指令')
    

    

    
def setup(maple):
    maple.add_cog(Number(maple))