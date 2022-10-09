import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
with open('./setting/gateway_channel.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member}join!')
        channel =self.maple.get_channel(int(jdata[str(member.guild.id)]["channel_Id"]))
        await channel.send(f'{member}加入了桌遊同樂!')
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member}leave!')
        channel =self.maple.get_channel(int(jdata[str(member.guild.id)]["channel_Id"]))
        await channel.send(f'{member}被狼人殺了QwQ')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        member_channel = self.maple.get_channel(int(jdata[str(member.guild.id)]["channel_Id"]))
        await member_channel.edit(name=f"人數: {member.guild.member_count}")
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        member_channel = self.maple.get_channel(int(jdata[str(member.guild.id)]["channel_Id"]))
        await member_channel.edit(name=f"人數: {member.guild.member_count}")



    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == 'hi' and msg.author != self.maple.user:
            await msg.channel.send('hello')

        if msg.content == 'test' and msg.author != self.maple.user:
            await msg.channel.send(f'<@895989639360438292>')

        if msg.content.startswith('我希望') and msg.author != self.maple.user:
                drawlots=["luck","unluck"]
                expect=random.choice(drawlots)
                if expect == "luck":
                    await msg.channel.send('你的願望會實現喔<:_mumi:748525629716037643>')
                else:
                    await msg.channel.send('那個...對不起<:_cat:878216638971920414>')
        with open('./setting/message.json','r',encoding='utf8') as mlink:
                jdata = json.load(mlink)
        if msg.content == '活著嗎' or msg.content == '醒著嗎' or msg.content == '還在嗎' and msg.author != self.maple.user:
            message = random.choice(jdata['call'])
            await msg.channel.send(message)
        j_morning=jdata['j_morning']
        endmorning=jdata['endmorning']
        i = 0
        a = 0
        if  msg.author != self.maple.user:
            while i < len(j_morning) and a == 0:
                a=j_morning[i]
                i = i + 1
                if msg.content.startswith(a) or msg.content == '早' or msg.content == '早～' or msg.content == '早~' and msg.author != self.maple.user:
                    emoji='<:_mumi:748525629716037643>'
                    await msg.add_reaction(emoji)
                    morning=random.randint(1,100)
                    if morning<=10:
                        gmorning = random.choice(jdata['morning'])
                        await msg.channel.send(gmorning)
                        # a = 1
            i = 0
            while i < len(endmorning) and a == 0:
                a=endmorning[i]
                i = i + 1
                if msg.content.endswith(a) and msg.author != self.maple.user:
                    emoji='<:_mumi:748525629716037643>'
                    await msg.add_reaction(emoji)
                    morning=random.randint(1,100)
                    if morning<=10:
                        gmorning = random.choice(jdata['morning'])
                        await msg.channel.send(gmorning)
                        # a = 1
        j_night=jdata['j_night']
        i = 0
        a = 0
        if msg.author != self.maple.user:
            while i < len(j_night) and a == 0:
                b=j_night[i]
                i = i+1
                if msg.content.endswith(b) or msg.content == "晚安" or msg.content == "安晚" or msg.content.startswith("晚安") and msg.author != self.maple.user:
                    emoji="<:_hug:856146331297775616>"
                    await msg.add_reaction(emoji)
                    night=random.randint(1,100)
                    if night<=10:
                        gnight = random.choice(jdata['night'])
                        await msg.channel.send(gnight)
                        # a = 1
        if msg.content == '好欸下班回家' and msg.author.id==515423438421229568 and msg.author != self.maple.user:
            await msg.channel.send("好欸<:_mumi:748525629716037643>")
        
def setup(maple):
    maple.add_cog(Event(maple))