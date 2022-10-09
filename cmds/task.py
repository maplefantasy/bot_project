import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime
import threading
from discord.ext import tasks
tt=0
# with open('./setting/setting.json','r',encoding='utf8') as mlink:
#     jdata = json.load(mlink)
owner=560091826170626071
with open('./setting/loop.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)


    #json文件 r=讀取,w=寫入

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.working_guild = []
        async def time_task():
            await self.maple.wait_until_ready()
            while tt == 0:#bot沒關閉繼續loop
                now_time=datetime.datetime.utcnow() + datetime.timedelta(hours=8)
                now_time = now_time.strftime("%H%M")
                for guild_id_str in jdata:
                    guild_id = int(guild_id_str)
                    guild = self.maple.get_guild(guild_id)
                    data_dict = jdata[guild_id_str]
                    channel = guild.get_channel(data_dict.get("set_loop_channel"))
                    time_set = data_dict.get("time_set")
                    tell = data_dict.get("tell")
                    sleep_time = int(data_dict.get("sleep_time"))
                    if all([channel, time_set, tell, sleep_time]) and now_time == time_set and guild_id not in self.working_guild:
                        task = asyncio.create_task(self.send_msg(channel, time_set, tell, sleep_time))
                        self.working_guild.append(guild_id)
                        await task
                await asyncio.sleep(3)

        self.bg_task=self.maple.loop.create_task(time_task())

    async def send_msg(self, channel: discord.TextChannel, time_set: str, tell: str, sleep_time: int):
        now_time=datetime.datetime.now().strftime('%H%M')
        while now_time == time_set:
            await channel.send(tell)
            await asyncio.sleep(sleep_time)
            now_time=datetime.datetime.now().strftime('%H%M')
        self.working_guild.remove(channel.guild.id)

        # self.bg_task=self.maple.loop.create_task(time_task())
            # loop.create_task[創建一個背景作業](taskname)

    @commands.command()
    async def ls_c(self,ctx,ch:int):
        self.channel=self.maple.get_channel(ch)
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            if str(ctx.guild.id) in jdata:
                jdata[str(ctx.guild.id)].update({"set_loop_channel":ch})
            else:
                jdata[str(ctx.guild.id)]={"set_loop_channel":ch}
            with open('./setting/loop.json','w',encoding='utf8') as mlink:
                json.dump(jdata,mlink,indent=4)
            await ctx.send(f'迴圈訊息已設定在:{self.channel.mention}')
        else:
            await ctx.send(f'你的身分組無管理員權限或開發者權限無法使用該指令')
        

    @commands.command()
    async def set_t(self,ctx,time):
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            if str(ctx.guild.id) in jdata:
                jdata[str(ctx.guild.id)].update({"time_set":time})
            else:
                jdata[str(ctx.guild.id)]={"time_set":time}
            with open('./setting/loop.json','w',encoding='utf8') as mlink:
                json.dump(jdata,mlink,indent=4)
            user=ctx.author.display_name
            await ctx.send(f'{user}把迴圈訊息設定在{time}')
        else:
            await ctx.send(f'你的身分組無管理員權限或開發者權限無法使用該指令')
        
    
    @commands.command()
    async def set_tell(self,ctx,tell,sleep:int):
        user=ctx.author.display_name
        ch=ctx.channel.id
        self.channel=self.maple.get_channel(ch)
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            if str(ctx.guild.id) in jdata:
                jdata[str(ctx.guild.id)].update({"tell":tell})
                jdata[str(ctx.guild.id)].update({"set_loop_channel":ch})
                jdata[str(ctx.guild.id)].update({"sleep_time":sleep})
            else:
                jdata[str(ctx.guild.id)]={"tell":tell, "set_loop_channel":ch, "sleep_time":sleep}
            with open('./setting/loop.json','w',encoding='utf8') as mlink:
                json.dump(jdata,mlink,indent=4)
            embed=discord.Embed()
            embed.add_field(name=f"{user}把迴圈訊息設定為{tell}", value=f"於{self.channel.mention},迴圈時間為{sleep}秒", inline=False)
            embed.add_field(name="延伸設定", value="""可以使用sl_c來設定想發送的頻道
可以使用stoploop讓助手停止訊息迴圈""", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'你的身分組無管理員權限或開發者權限無法使用該指令')
        

    @commands.command()
    async def stoploop(self,ctx):
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            if str(ctx.guild.id) in jdata:
                jdata[str(ctx.guild.id)].update({"set_loop_channel":""})
                jdata[str(ctx.guild.id)].update({"time_set":""})
            else:
                jdata[str(ctx.guild.id)]={"set_loop_channel":""}
                jdata[str(ctx.guild.id)]={"time_set":""}
            with open('./setting/loop.json','w',encoding='utf8') as mlink:
                json.dump(jdata,mlink,indent=4)
            await ctx.send('已經停止迴圈訊息囉')
        else:
            await ctx.send(f'你的身分組無管理員權限或開發者權限無法使用該指令')



def setup(maple):
    maple.add_cog(Task(maple))
