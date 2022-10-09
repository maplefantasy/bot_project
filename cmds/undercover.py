import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime,random,copy
with open('./setting/undercover.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)

class undercover(Cog_Extension):

    @commands.command()
    async def uc_list(self,ctx):
        list=[]
        playlist=jdata[str(ctx.guild.id)]["uclist"]
        i=0
        while i < len(playlist):
            a=playlist[i]
            i = i+1
            play=f'{i}號玩家:{self.maple.get_guild(ctx.guild.id).get_member(a).display_name}'
            list.append(play)

        jdata[str(ctx.guild.id)].update({"ucgamech":""})

        embed=discord.Embed(title="誰是臥底玩家名單", description="以下加入的玩家",timestamp=datetime.datetime.utcnow())
        embed.add_field(name="玩家名單", value=f"{list}", inline=False)
        embed.add_field(name="參加人數", value=f"{len(list)}", inline=False)
        await ctx.send(embed=embed)
        await ctx.send('''以關閉報名系統!
        開啟報名系統請輸入!!ucsu''')
        with open('./setting/undercover.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    #臥底抽選
    @commands.command()
    async def uc_r(self,ctx):
        object=jdata[str(ctx.guild.id)]["object"]
        uclist=jdata[str(ctx.guild.id)]["uclist"]
        uclist1=copy.deepcopy(uclist)
        oblist=[]
        oblist=copy.deepcopy(object)
        uclist2=[]
        ucob = random.choice(oblist) #臥底物件
        jdata[str(ctx.guild.id)].update({"ucob":ucob})

        oblist.remove(ucob)
        ucp = random.sample(uclist1,k=jdata[str(ctx.guild.id)]["uc"])
        i=0
        while i < len(ucp):
            uc=ucp[i]
            ucid=self.maple.get_guild(ctx.guild.id).get_member(uc).id
            ucdn=self.maple.get_guild(ctx.guild.id).get_member(uc).display_name
            user = self.maple.get_user(ucid)
            # await user.send(f'這是你的物件:{ucob}')
            uclist1.remove(uc)
            uclist2.append(uc)
            jdata[str(ctx.guild.id)].update({"ucplayer":uclist2})
            i=i+1
            print(f'''已dm:{ucdn}
            臥底名為:{ucob}''')


        npob=random.choice(oblist)
        i = 0
        while i < len(uclist1):
            np=uclist1[i]
            npid=self.maple.get_guild(ctx.guild.id).get_member(np).id
            npdn=self.maple.get_guild(ctx.guild.id).get_member(np).display_name
            user = self.maple.get_user(npid)
            # await user.send(f'這是你的物件:{npob}')
            i = i+1
            print(f'''已dm:{npdn}
            平民名為:{npob}''')

        await ctx.channel.purge(limit = 1)
        # await ctx.send('分發完成')
        with open('./setting/undercover.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    #公告臥底
    @commands.command()
    async def uc_mp(self,ctx):
        ucplay=jdata[str(ctx.guild.id)]["ucplayer"]
        ucob=jdata[str(ctx.guild.id)]["ucob"]
        ucp=copy.deepcopy(ucplay)
        ucplayer=[]
        i=0
        while i < len(ucp):
            uc=ucp[i]
            npdn=self.maple.get_guild(ctx.guild.id).get_member(uc).display_name
            ucplayer.append(npdn)
            i=1
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'''公告臥底!!
        臥底是......||{ucplayer},臥底物品是{ucob}||''')

    #設定詞語跟臥底人數
    @commands.command()
    async def uc_setting(self,ctx,object1,object2,np:int,uc:int):
        user=ctx.author.mention
        ob=[]
        if uc<np and object1!='' and object2!='':
            ob.append(object1)
            ob.append(object2)
            jdata[str(ctx.guild.id)].update({"object":ob})
            jdata[str(ctx.guild.id)].update({"np":np})
            jdata[str(ctx.guild.id)].update({"uc":uc})
            await ctx.channel.purge(limit = 1)
            await ctx.send(f'{user}已完成遊戲設定,查看設定可以打dm_ucs')
        else:
            await ctx.channel.purge(limit = 1)
            await ctx.send(f'''{user}由於間諜數量多於平民數量或物件未填上
            指令語法請重新設定~
            !!uc_setting 物件1 物件2 平民數量 臥底數量''')
        with open('./setting/undercover.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)
    
    @commands.command()
    async def obadd(self,ctx,uc):
        ob=[]
        ob=jdata[str(ctx.guild.id)]["object"]
        ob.append(uc)
        jdata[str(ctx.guild.id)].update({"object":ob})
        await ctx.send(f'物件已新增')
        with open('./setting/undercover.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    
    @commands.command()
    async def dm_ucs(self,ctx):
        user=ctx.author.mention
        await ctx.author.send(f'''物件1:{jdata[str(ctx.guild.id)]["object"]}
        平民數量:{jdata[str(ctx.guild.id)]["np"]}
        臥底數量:{jdata[str(ctx.guild.id)]["uc"]}''')
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'設定資訊已送出到{user}')


    #報名指令
    @commands.command()
    # @commands.is_owner()
    async def ucsu(self,ctx):
        await ctx.channel.purge(limit = 1)
        text="""這裡是誰是臥底的beta測試遊戲報名系統
        點選✅反應加入遊戲!"""
        uct = await ctx.send(text)
        emoji='✅'
        uclist=[]
        await uct.add_reaction(emoji)
        message_id = uct.id
        if str(ctx.guild.id) in jdata:
            jdata[str(ctx.guild.id)].update({"ucgamech":message_id})
            jdata[str(ctx.guild.id)].update({"uclist":uclist})
        else:
            jdata[str(ctx.guild.id)]={"ucgamech":message_id}
            jdata[str(ctx.guild.id)]={"uclist":uclist}
        with open('./setting/undercover.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        guild=data.guild_id
        member=data.member
        emoji=data.emoji
        uclist=jdata[str(guild)]["uclist"]
        emojich=jdata[str(guild)]["ucgamech"]
        if str(guild) in jdata:
            if str(emoji) == '✅'and member != self.maple.user and data.message_id == emojich:
                uclist.append(member.id)
                if str(guild) in jdata:
                    jdata[str(guild)].update({"uclist":uclist})
                else:
                    jdata[str(guild)]={"uclist":uclist}

        with open('./setting/undercover.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        guild=self.maple.get_guild(data.guild_id)
        guildstr=data.guild_id
        member=guild.get_member(data.user_id)
        emoji=data.emoji
        uclist=jdata[str(guildstr)]["uclist"]
        emojich=jdata[str(guildstr)]["ucgamech"]
        emojich=int(emojich)
        if str(guildstr) in jdata:
            if str(emoji) == '✅'and member != self.maple.user and data.message_id == emojich:
                uclist.remove(member.id)
                if str(guildstr) in jdata:
                    jdata[str(guildstr)].update({"uclist":uclist})
                else:
                    jdata[str(guildstr)]={"uclist":uclist}

        with open('./setting/undercover.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)


def setup(maple):
    maple.add_cog(undercover(maple))