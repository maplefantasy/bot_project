import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random,datetime
import json
with open('./setting/setting.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)


class Messagerecord(Cog_Extension):
    # @commands.Cog.listener()
    # async def on_message_delete(self,message):
    #     ch=message.channel.id
    #     embed=discord.Embed(title="{} 刪除了訊息".format(message.author.name),description="", color=0xFF0000)
    #     embed.add_field(name=message.content, value="訊息內容是",inline=True)
    #     channel = self.maple.get_channel(ch)
    #     await channel.send(channel, embed=embed)
    @commands.Cog.listener()
    async def on_raw_message_delete(self,payload):
        guild = payload.guild_id
        if guild == 575723730932858930:
            message = payload.cached_message
            ch=payload.channel_id
            msgid=payload.message_id
            userid=message.author.id
            channel = self.maple.get_channel(ch)
            sendchannel = self.maple.get_channel(881486976669351948)
            time=datetime.datetime.utcnow() + datetime.timedelta(hours=8)
            time = time.strftime("%Y/%m/%d %H:%M:%S")
            if message.author != self.maple.user:
                if not message.attachments:
                    embed=discord.Embed(title="{} 刪除了訊息".format(message.author.name),description="", color=0xFF0000,timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="訊息內容", value=message.content,inline=False)
                    embed.add_field(name="訊息刪除時間", value=f"台灣時間{time}",inline=False)
                    embed.add_field(name="ID", value=f"""```ansi
\u001b[0;33m用戶\u001b[0;0m = \u001b[0;36m{userid}
\u001b[0;33m訊息\u001b[0;0m = \u001b[0;36m{msgid}```""",inline=False)
                    embed.add_field(name="用戶訊息刪除位於", value=channel.mention,inline=False)
                    await sendchannel.send(embed=embed)
                else:
                    embed=discord.Embed(title="{} 刪除了訊息".format(message.author.name),description="", color=0xFF0000,timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="訊息內容", value=f"""{message.content}
        {message.attachments[0].url}""",inline=False)
                    embed.add_field(name="訊息刪除時間", value=f"台灣時間{time}",inline=False)
                    embed.add_field(name="ID", value=f"""```ansi
\u001b[0;33m用戶\u001b[0;0m = \u001b[0;36m{userid}
\u001b[0;33m訊息\u001b[0;0m = \u001b[0;36m{msgid}```""",inline=False)
                    embed.add_field(name="用戶訊息刪除位於", value=channel.mention,inline=False)
                    await sendchannel.send(embed=embed)

    @commands.command()
    async def msgchedit(self,ctx,*,num:int):
        if ctx.guild.id == 879225310556594196:
            ch = num
            jdata["chswich"] = ch
            channel = self.maple.get_channel(ch)
            await ctx.send(f"已更改發言頻道為{channel.mention}")
            with open('./setting/setting.json','w',encoding='utf8') as mlink:
                json.dump(jdata,mlink,indent=4)


    @commands.Cog.listener()
    async def on_message(self,message):
        guild=message.guild.id
        getchannel=message.channel.id
        chswich = jdata['chswich']
        if message.content.startswith("!!"):
            return
        else:
            if guild == 879225310556594196 and getchannel == 880407834020421662 and message.author != self.maple.user:
                sendchannel = self.maple.get_channel(chswich)
                msg=message.content
                await sendchannel.send(msg)
                
        

def setup(maple):
    maple.add_cog(Messagerecord(maple))