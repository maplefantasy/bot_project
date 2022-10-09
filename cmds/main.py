from distutils import command
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime,random


import json
with open('./setting/setting.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)
owner=(int(jdata['OWNER_ID']))


class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'目前ping值是{round(self.maple.latency*1000)}ms喔')
    @commands.command()
    async def helpd(self,ctx):
        if ctx.message.author.id==owner :
            await ctx.send(f'```以下為目前有的指令\n**觸發指令**\nhi,我希望,醒著嗎,早安\n\n**main指令**\nhelp\,helpd(當前使用指令),sayd,saygm,clean int,cleand int,set_gatec,set_gatem,pick 文字,repeople,dm id 文字,bury 文字\n\n**react指令**\nholo,holeen,srn,運勢占卜,upsrn,resrn,srnc\n\n**task指令**\nls_c chid,set_t time(24h),set_tell 文字 sleep(int),stoploop\n\n**wolfgame指令**\nwg_setting 預言家 女巫 獵人 騎士 村民 狼人 狼王\nwgsu,wgpeople,cleanwg,wglist,wg_r\n\n**undercover指令**\nuc_setting 物件1 物件2 平民數量 臥底數量\nobadd 物件,dm_ucs,ucsu,uc_list,uc_r,uc_mp\n\n**gamecrad指令**\np_bright num(int) %(int)\ncompasscard,```')
        else:
            await ctx.send(f'你非開發者無法使用該指令')

    @commands.command()
    async def sayd(self,ctx,*,msg):
        user=ctx.author.display_name
        await ctx.message.delete()
        await ctx.send(f"{user}說了{msg}")
    
    @commands.command()
    async def saygm(self,ctx,*,msg):
        if ctx.message.author.id==owner :
            await ctx.message.delete()
            await ctx.send(f"{msg}")
        else:
            await ctx.send(f'你非開發者無法使用該指令')
    
    @commands.command()
    async def clean(self,ctx,*,num:int):
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            await ctx.channel.purge(limit = num + 1)
            user=ctx.message.author.display_name  #get用戶當前伺服器名稱
            await ctx.send(f'{user}啟用指令刪除{num}則訊息')
        else:
            await ctx.send(f'你的身分組無管理員權限或開發者權限無法使用該指令')

    @commands.command()
    async def cleand(self,ctx,*,num:int):
        if ctx.message.author.id==owner :
            await ctx.channel.purge(limit = num + 1)
        else:
            await ctx.send(f'你非開發者無法使用該指令')

    
    
    @commands.command()
    async def set_gatec(self,ctx,channelId:int):
        with open('./setting/gateway_channel.json','r',encoding='utf8') as mlink:
            jdata = json.load(mlink)
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            if ctx.guild.id in jdata["gateway_channel"]:
                jdata["gateway_channel"][ctx.guild.id] = channelId
            else:
                jdata["gateway_channel"].update({ctx.guild.id:f"{channelId}"})
        else:
            await ctx.send(f'你的身分組無管理員權限或開發者權限無法使用該指令')
        with open('./setting/gateway_channel.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.command()
    async def set_gatem(self,ctx,channelId:int):
        self.channel=self.maple.get_channel(channelId)
        with open('./setting/gateway_channel.json','r',encoding='utf8') as mlink:
            jdata = json.load(mlink)
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            if ctx.guild.id in jdata["membernum"]:
                jdata["membernum"][ctx.guild.id] = channelId
                await ctx.send(f'已更新人員檢測頻道於{self.channel}')
            else:
                jdata["membernum"].update({ctx.guild.id:f"{channelId}"})
                await ctx.send(f'已新增人員檢測頻道於{self.channel}')
        else:
            await ctx.send(f'你的身分組無管理員權限或開發者權限無法使用該指令')
        with open('./setting/gateway_channel.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.command()
    async def pick(self,ctx,name):
        user=ctx.author.display_name
        bot=jdata['BOT_ID']
        if bot in name:
            await ctx.send("不要在句子裡提到我!(敲")
        else:
            await ctx.send(f'{user}把{name}撿起來了')

    @commands.command()
    async def repeople(self,ctx):
        people=ctx.guild.member_count
        member_channel=self.maple.get_channel(jdata["membernum"][ctx.guild.id])
        await member_channel.edit(name=f"Members: {ctx.guild.member_count}")
        await ctx.send(f'已修改人數,目前為{people}人')

    @commands.command()
    async def dm(self,ctx,id:discord.Member,*,word):
        if ctx.message.author.id==owner:
            await id.send(f'{word}')
            await ctx.channel.purge(limit = 1)
            await ctx.send(f'訊息已送出')
        else:
            await ctx.send(f'你的身分組無開發者權限無法使用該指令')
    
    @commands.command()
    async def bury(self,ctx,name):
        bot=jdata['BOT_ID']
        if bot in name:
            await ctx.send("不要在句子裡提到我!(反埋葬")
        else:
            await ctx.send(f'{name}埋葬掉了,讓我們一起哀悼QAQ')
def setup(maple):
    maple.add_cog(Main(maple))