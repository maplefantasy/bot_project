import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime,random,copy
with open('./setting/wolfgame.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)

    
class wolfgame(Cog_Extension):


#玩家清單
    @commands.command()
    async def wg_list(self,ctx):
        list=[]
        playlist=jdata[str(ctx.guild.id)]["wglist"]
        i=0
        while i < len(playlist):
            a=playlist[i]
            i = i+1
            play=f'{i}號玩家:{self.maple.get_guild(ctx.guild.id).get_member(a).display_name}\n'
            list.append(play)
        jdata[str(ctx.guild.id)].update({"wggamech":""})

        embed=discord.Embed(title="狼人殺名單", description="以下加入的玩家",timestamp=datetime.datetime.utcnow())
        embed.add_field(name="玩家名單", value=f"{list}", inline=False)
        embed.add_field(name="參加人數", value=f"{len(list)}", inline=False)
        await ctx.send(embed=embed)
        await ctx.send('''以關閉報名系統!
開啟報名系統請輸入!!wgsu''')
        with open('./setting/wolfgame.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)
    

    @commands.command()
    async def wg_givelist(self,ctx):
        with open('./setting/setting.json','r',encoding='utf8') as mlink:
            jdata = json.load(mlink)
        owner=(int(jdata['OWNER_ID']))
        user=ctx.author.mention
        if ctx.message.author.id==owner or ctx.author.guild_permissions.administrator:
            with open('./setting/wolfgame.json','r',encoding='utf8') as mlink:
                json.dump(jdata,mlink,indent=4)
            pr=jdata[str(ctx.guild.id)]["wggamelist"]
            await ctx.author.send(pr)
            await ctx.send(f"已將玩家職業資料發送給{user}了")
        else:
            await ctx.send(f'你的身分組無管理員權限或開發者權限無法使用該指令')




#職業分配
    @commands.command()
    async def wg_r(self,ctx):
        wglist=copy.deepcopy(jdata[str(ctx.guild.id)]["wglist"])
        wgname=copy.deepcopy(wglist)
        user=ctx.author.mention
        tslist=[]
        profession=[]
        prophet=[]
        witch=[]
        hunter=[]
        knight=[]
        villager=[]
        werewolf=[]
        wolfking=[]
        tw=[]
        ps=[]
        bm=[]
        wc=[]
        gr=[]
        wbb=[]
        wbs=[]
        bmm=[]
        gg=[]
        gk=[]
        wb=[]
        sw=[]
        mg=[]
        gd=[]

        playnum=jdata[str(ctx.guild.id)]["prophet_mete"]+jdata[str(ctx.guild.id)]["witch_mete"]+jdata[str(ctx.guild.id)]["hunter_mete"]+jdata[str(ctx.guild.id)]["knight_mete"]+jdata[str(ctx.guild.id)]["villager_mete"]+jdata[str(ctx.guild.id)]["werewolf_mete"]+jdata[str(ctx.guild.id)]["wolfking_mete"]+jdata[str(ctx.guild.id)]["tw_mete"]+jdata[str(ctx.guild.id)]["ps_mete"]+jdata[str(ctx.guild.id)]["bm_mete"]+jdata[str(ctx.guild.id)]["wc_mete"]+jdata[str(ctx.guild.id)]["gr_mete"]+jdata[str(ctx.guild.id)]["wbb_mete"]+jdata[str(ctx.guild.id)]["wbs_mete"]+jdata[str(ctx.guild.id)]["bmm_mete"]+jdata[str(ctx.guild.id)]["gg_mete"]+jdata[str(ctx.guild.id)]["gk_mete"]+jdata[str(ctx.guild.id)]["wb_mete"]+jdata[str(ctx.guild.id)]["sw_mete"]+jdata[str(ctx.guild.id)]["mg_mete"]+jdata[str(ctx.guild.id)]["gd_mete"]

        if len(wglist) == playnum :

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["prophet_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"prophet":tslist})
            print('預言家')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                prophet.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["witch_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"witch":tslist})
            print('女巫')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                witch.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["hunter_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"hunter":tslist})
            print('獵人')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                hunter.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["knight_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"knight":tslist})
            print('騎士')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                knight.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["villager_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"villager":tslist})
            print('村民')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                villager.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["werewolf_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"werewolf":tslist})
            print('狼人')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                werewolf.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["wolfking_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"wolfking":tslist})
            print('狼王')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                wolfking.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["tw_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"tw":tslist})
            print('機械狼')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                tw.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["ps_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"ps":tslist})
            print('通靈師')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                ps.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["bm_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"bm":tslist})
            print('血月使者')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                bm.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["wc_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"wc":tslist})
            print('獵魔人')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                wc.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["gr_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"gr":tslist})
            print('惡靈騎士')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                gr.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["wbb_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"wbb":tslist})
            print('狼兄')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                wbb.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["wbs_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"wbs":tslist})
            print('狼弟')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                wbs.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["bmm_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"bmm":tslist})
            print('黑市商人')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                bmm.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["gg_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"gg":tslist})
            print('石像鬼')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                gg.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["gk_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"gk":tslist})
            print('守墓人')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                gk.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["wb_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"wb":tslist})
            print('狼美人')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                wb.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["sw_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"sw":tslist})
            print('雪狼')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                sw.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["mg_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"mg":tslist})
            print('魔術師')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                mg.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1

            tslist = random.sample(wgname,k=jdata[str(ctx.guild.id)]["gd_mete"])
            i=0
            jdata[str(ctx.guild.id)].update({"gd":tslist})
            print('守衛')
            while i < len(tslist):
                a=tslist[i]
                wgname.remove(a)
                gd.append(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).display_name)
                print(self.maple.get_guild(ctx.guild.id).get_member(a).id)
                i = i+1
            
            print('一輪')
            await ctx.channel.purge(limit = 1)
            embed=discord.Embed(title="公布玩家職業",timestamp=datetime.datetime.utcnow())
            embed.add_field(name="預言家", value=f"{prophet}", inline=True)
            embed.add_field(name="女巫", value=f"{witch}", inline=True)
            embed.add_field(name="獵人", value=f"{hunter}", inline=True)
            embed.add_field(name="騎士", value=f"{knight}", inline=True)
            embed.add_field(name="平民", value=f"{villager}", inline=True)
            embed.add_field(name="狼人", value=f"{werewolf}", inline=True)
            embed.add_field(name="狼王", value=f"{wolfking}", inline=True)
            embed.add_field(name="機械狼", value=f"{tw}", inline=True)
            embed.add_field(name="通靈師", value=f"{ps}", inline=True)
            embed.add_field(name="血月使者", value=f"{bm}", inline=True)
            embed.add_field(name="獵魔人", value=f"{wc}", inline=True)
            embed.add_field(name="惡靈騎士", value=f"{gr}", inline=True)
            embed.add_field(name="狼兄", value=f"{wbb}", inline=True)
            embed.add_field(name="狼弟", value=f"{wbs}", inline=True)
            embed.add_field(name="黑市商人", value=f"{bmm}", inline=True)
            embed.add_field(name="石像鬼", value=f"{gg}", inline=True)
            embed.add_field(name="守墓人", value=f"{gk}", inline=True)
            embed.add_field(name="狼美人", value=f"{wb}", inline=True)
            embed.add_field(name="雪狼", value=f"{sw}", inline=True)
            embed.add_field(name="魔術師", value=f"{mg}", inline=True)
            embed.add_field(name="守衛", value=f"{gd}", inline=True)
            await ctx.author.send(embed=embed)
            await ctx.send(f"已將資料發送給{user}了")


            pr=f"預言家:{prophet},女巫{witch}獵人:{hunter},騎士:{knight},平民:{villager},狼人:{werewolf},狼王:{wolfking},機械狼:{tw},通靈師:{ps},血月使者:{bm},獵魔人:{wc},惡靈騎士:{gr},狼兄:{wbb},狼弟:{wbs},黑市商人:{bmm},石像鬼:{gg},守墓人:{gk},狼美人:{wb},雪狼:{sw},魔術師:{mg},守衛:{gd}"
            jdata[str(ctx.guild.id)].update({"wggamelist":pr})

        else:
            await ctx.channel.purge(limit = 1)
            await ctx.send(f"玩家人數{len(wglist)}與職業數量{playnum}不相等")






        
        if str(ctx.guild.id) in jdata:
            jdata[str(ctx.guild.id)].update({"wglist":wglist})
        else:
            jdata[str(ctx.guild.id)]={"wglist":wglist}
        with open('./setting/wolfgame.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)


#職業數量設定
    @commands.command()
    async def wg_si(self,ctx,profession:str,num:int): #單一設定
        if profession=="預言家":
            jdata[str(ctx.guild.id)].update({"prophet_mete":num})
            await ctx.send(f"預言家人數設定為{num}人")
        if profession=="女巫":
            jdata[str(ctx.guild.id)].update({"witch_mete":num})
            await ctx.send(f"女巫人數設定為{num}人")
        if profession=="獵人":
            jdata[str(ctx.guild.id)].update({"hunter_mete":num})
            await ctx.send(f"獵人人數設定為{num}人")
        if profession=="騎士":
            jdata[str(ctx.guild.id)].update({"knight_mete":num})
            await ctx.send(f"騎士人數設定為{num}人")
        if profession=="平民":
            jdata[str(ctx.guild.id)].update({"villager_mete":num})
            await ctx.send(f"平民人數設定為{num}人")
        if profession=="狼人":
            jdata[str(ctx.guild.id)].update({"werewolf_mete":num})
            await ctx.send(f"狼人人數設定為{num}人")
        if profession=="狼王":
            jdata[str(ctx.guild.id)].update({"wolfking_mete":num})
            await ctx.send(f"狼王人數設定為{num}人")
        if profession=="機械狼":
            jdata[str(ctx.guild.id)].update({"tw_mete":num})
            await ctx.send(f"機械狼人數設定為{num}人")
        if profession=="通靈師":
            jdata[str(ctx.guild.id)].update({"ps_mete":num})
            await ctx.send(f"通靈師人數設定為{num}人")
        if profession=="血月使者":
            jdata[str(ctx.guild.id)].update({"bm_mete":num})
            await ctx.send(f"血月使者人數設定為{num}人")
        if profession=="獵魔人":
            jdata[str(ctx.guild.id)].update({"wc_mete":num})
            await ctx.send(f"獵魔人人數設定為{num}人")
        if profession=="惡靈騎士":
            jdata[str(ctx.guild.id)].update({"gr_mete":num})
            await ctx.send(f"惡靈騎士人數設定為{num}人")
        if profession=="狼兄":
            jdata[str(ctx.guild.id)].update({"wbb_mete":num})
            await ctx.send(f"狼兄人數設定為{num}人")
        if profession=="狼弟":
            jdata[str(ctx.guild.id)].update({"wbs_mete":num})
            await ctx.send(f"狼弟人數設定為{num}人")
        if profession=="黑市商人":
            jdata[str(ctx.guild.id)].update({"bmm_mete":num})
            await ctx.send(f"黑市商人人數設定為{num}人")
        if profession=="石像鬼":
            jdata[str(ctx.guild.id)].update({"gg_mete":num})
            await ctx.send(f"石像鬼人數設定為{num}人")
        if profession=="守墓人":
            jdata[str(ctx.guild.id)].update({"gk_mete":num})
            await ctx.send(f"守墓人人數設定為{num}人")
        if profession=="狼美人":
            jdata[str(ctx.guild.id)].update({"wb_mete":num})
            await ctx.send(f"狼美人人數設定為{num}人")
        if profession=="雪狼":
            jdata[str(ctx.guild.id)].update({"sw_mete":num})
            await ctx.send(f"雪狼人數設定為{num}人")
        if profession=="魔術師":
            jdata[str(ctx.guild.id)].update({"mg_mete":num})
            await ctx.send(f"魔術師人數設定為{num}人")
        if profession=="守衛":
            jdata[str(ctx.guild.id)].update({"gd_mete":num})
            await ctx.send(f"守衛人數設定為{num}人")

        with open('./setting/wolfgame.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.command()
    async def wg_all(self,ctx,prophet:int,witch:int,hunter:int,knight:int,villager:int,werewolf:int,wolfking:int,tw:int,ps:int,bm:int,wc:int,gr:int,wbb:int,wbs:int,bmm:int,gg:int,gk:int,wb:int,sw:int,mg:int,gd:int):
        jdata[str(ctx.guild.id)].update({"prophet_mete":prophet})
        jdata[str(ctx.guild.id)].update({"witch_mete":witch})
        jdata[str(ctx.guild.id)].update({"hunter_mete":hunter})
        jdata[str(ctx.guild.id)].update({"knight_mete":knight})
        jdata[str(ctx.guild.id)].update({"werewolf_mete":villager})
        jdata[str(ctx.guild.id)].update({"wolfking_mete":werewolf})
        jdata[str(ctx.guild.id)].update({"villager_mete":wolfking})
        jdata[str(ctx.guild.id)].update({"tw_mete":tw})
        jdata[str(ctx.guild.id)].update({"ps_mete":ps})
        jdata[str(ctx.guild.id)].update({"bm_mete":bm})
        jdata[str(ctx.guild.id)].update({"wc_mete":wc})
        jdata[str(ctx.guild.id)].update({"gr_mete":gr})
        jdata[str(ctx.guild.id)].update({"wbb_mete":wbb})
        jdata[str(ctx.guild.id)].update({"wbs_mete":wbs})
        jdata[str(ctx.guild.id)].update({"bmm_mete":bmm})
        jdata[str(ctx.guild.id)].update({"gg_mete":gg})
        jdata[str(ctx.guild.id)].update({"gk_mete":gk})
        jdata[str(ctx.guild.id)].update({"wb_mete":wb})
        jdata[str(ctx.guild.id)].update({"sw_mete":sw})
        jdata[str(ctx.guild.id)].update({"mg_mete":mg})
        jdata[str(ctx.guild.id)].update({"gd_mete":gd})
        with open('./setting/wolfgame.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)
    
        embed=discord.Embed(title="職業分配設定", description="以下為職業數量")
        embed.add_field(name="預言家", value=f"{prophet}人", inline=True)
        embed.add_field(name="女巫", value=f"{witch}人", inline=True)
        embed.add_field(name="獵人", value=f"{hunter}人", inline=True)
        embed.add_field(name="騎士", value=f"{knight}人", inline=True)
        embed.add_field(name="平民", value=f"{villager}人", inline=True)
        embed.add_field(name="狼人", value=f"{werewolf}人", inline=True)
        embed.add_field(name="狼王", value=f"{wolfking}人", inline=True)
        embed.add_field(name="機械狼", value=f"{tw}人", inline=True)
        embed.add_field(name="通靈師", value=f"{ps}人", inline=True)
        embed.add_field(name="血月使者", value=f"{bm}人", inline=True)
        embed.add_field(name="獵魔人", value=f"{wc}人", inline=True)
        embed.add_field(name="惡靈騎士", value=f"{gr}人", inline=True)
        embed.add_field(name="狼兄", value=f"{wbb}人", inline=True)
        embed.add_field(name="狼弟", value=f"{wbs}人", inline=True)
        embed.add_field(name="黑市商人", value=f"{bmm}人", inline=True)
        embed.add_field(name="石像鬼", value=f"{gg}人", inline=True)
        embed.add_field(name="守墓人", value=f"{gk}人", inline=True)
        embed.add_field(name="狼美人", value=f"{wb}人", inline=True)
        embed.add_field(name="雪狼", value=f"{sw}人", inline=True)
        embed.add_field(name="魔術師", value=f"{mg}人", inline=True)
        embed.add_field(name="守衛", value=f"{gd}人", inline=True)
        embed.add_field(name="指令詳細", value="""指令的排法順序
        !!wg_all 預言家 女巫 獵人 騎士 平民 狼人 狼王 機械狼 通靈師 血月使者 獵魔人 惡靈騎士 狼兄 狼弟 黑市商人 石像鬼 守墓人 狼美人 雪狼 魔術師 守衛""", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def wgstart(self,ctx):
        if str(ctx.guild.id) in jdata:
            jdata[str(ctx.guild.id)].update({"wglist":[]})
            jdata[str(ctx.guild.id)].update({"prophet_mete":0})
            jdata[str(ctx.guild.id)].update({"witch_mete":0})
            jdata[str(ctx.guild.id)].update({"hunter_mete":0})
            jdata[str(ctx.guild.id)].update({"knight_mete":0})
            jdata[str(ctx.guild.id)].update({"villager_mete":0})
            jdata[str(ctx.guild.id)].update({"werewolf_mete":0})
            jdata[str(ctx.guild.id)].update({"wolfking_mete":0})
            jdata[str(ctx.guild.id)].update({"tw_mete":0})
            jdata[str(ctx.guild.id)].update({"ps_mete":0})
            jdata[str(ctx.guild.id)].update({"bm_mete":0})
            jdata[str(ctx.guild.id)].update({"wc_mete":0})
            jdata[str(ctx.guild.id)].update({"gr_mete":0})
            jdata[str(ctx.guild.id)].update({"wbb_mete":0})
            jdata[str(ctx.guild.id)].update({"wbs_mete":0})
            jdata[str(ctx.guild.id)].update({"bmm_mete":0})
            jdata[str(ctx.guild.id)].update({"gg_mete":0})
            jdata[str(ctx.guild.id)].update({"gk_mete":0})
            jdata[str(ctx.guild.id)].update({"wb_mete":0})
            jdata[str(ctx.guild.id)].update({"sw_mete":0})
            jdata[str(ctx.guild.id)].update({"mg_mete":0})
            jdata[str(ctx.guild.id)].update({"gd_mete":0})
            jdata[str(ctx.guild.id)].update({"prophet":[]})
            jdata[str(ctx.guild.id)].update({"witch":[]})
            jdata[str(ctx.guild.id)].update({"hunter":[]})
            jdata[str(ctx.guild.id)].update({"knight":[]})
            jdata[str(ctx.guild.id)].update({"villager":[]})
            jdata[str(ctx.guild.id)].update({"werewolf":[]})
            jdata[str(ctx.guild.id)].update({"wolfking":[]})
            jdata[str(ctx.guild.id)].update({"tw":[]})
            jdata[str(ctx.guild.id)].update({"ps":[]})
            jdata[str(ctx.guild.id)].update({"bm":[]})
            jdata[str(ctx.guild.id)].update({"wc":[]})
            jdata[str(ctx.guild.id)].update({"gr":[]})
            jdata[str(ctx.guild.id)].update({"wbb":[]})
            jdata[str(ctx.guild.id)].update({"wbs":[]})
            jdata[str(ctx.guild.id)].update({"bmm":[]})
            jdata[str(ctx.guild.id)].update({"gg":[]})
            jdata[str(ctx.guild.id)].update({"gk":[]})
            jdata[str(ctx.guild.id)].update({"wb":[]})
            jdata[str(ctx.guild.id)].update({"sw":[]})
            jdata[str(ctx.guild.id)].update({"mg":[]})
            jdata[str(ctx.guild.id)].update({"gd":[]})
            jdata[str(ctx.guild.id)].update({"wggamech":""})

        else:
            jdata[str(ctx.guild.id)]=({"wglist":[]})
            jdata[str(ctx.guild.id)]={"prophet_mete":0}
            jdata[str(ctx.guild.id)]={"witch_mete":0}
            jdata[str(ctx.guild.id)]={"hunter_mete":0}
            jdata[str(ctx.guild.id)]={"knight_mete":0}
            jdata[str(ctx.guild.id)]={"villager_mete":0}
            jdata[str(ctx.guild.id)]={"werewolf_mete":0}
            jdata[str(ctx.guild.id)]={"wolfking_mete":0}
            jdata[str(ctx.guild.id)]={"tw_mete":0}
            jdata[str(ctx.guild.id)]={"ps_mete":0}
            jdata[str(ctx.guild.id)]={"bm_mete":0}
            jdata[str(ctx.guild.id)]={"wc_mete":0}
            jdata[str(ctx.guild.id)]={"gr_mete":0}
            jdata[str(ctx.guild.id)]={"wbb_mete":0}
            jdata[str(ctx.guild.id)]={"wbs_mete":0}
            jdata[str(ctx.guild.id)]={"bmm_mete":0}
            jdata[str(ctx.guild.id)]={"gg_mete":0}
            jdata[str(ctx.guild.id)]={"gk_mete":0}
            jdata[str(ctx.guild.id)]={"wb_mete":0}
            jdata[str(ctx.guild.id)]={"sw_mete":0}
            jdata[str(ctx.guild.id)]={"mg_mete":0}
            jdata[str(ctx.guild.id)]={"gd_mete":0}
            jdata[str(ctx.guild.id)]={"prophet":[]}
            jdata[str(ctx.guild.id)]={"witch":[]}
            jdata[str(ctx.guild.id)]={"hunter":[]}
            jdata[str(ctx.guild.id)]={"knight":[]}
            jdata[str(ctx.guild.id)]={"villager":[]}
            jdata[str(ctx.guild.id)]={"werewolf":[]}
            jdata[str(ctx.guild.id)]={"wolfking":[]}
            jdata[str(ctx.guild.id)]={"tw":[]}
            jdata[str(ctx.guild.id)]={"ps":[]}
            jdata[str(ctx.guild.id)]={"bm":[]}
            jdata[str(ctx.guild.id)]={"wc":[]}
            jdata[str(ctx.guild.id)]={"gr":[]}
            jdata[str(ctx.guild.id)]={"wbb":[]}
            jdata[str(ctx.guild.id)]={"wbs":[]}
            jdata[str(ctx.guild.id)]={"bmm":[]}
            jdata[str(ctx.guild.id)]={"gg":[]}
            jdata[str(ctx.guild.id)]={"gk":[]}
            jdata[str(ctx.guild.id)]={"wb":[]}
            jdata[str(ctx.guild.id)]={"sw":[]}
            jdata[str(ctx.guild.id)]={"mg":[]}
            jdata[str(ctx.guild.id)]={"gd":[]}
            jdata[str(ctx.guild.id)]={"wggamech":""}
        
        with open('./setting/wolfgame.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

#遊戲報名
    @commands.command()
    # @commands.is_owner()
    async def wgsu(self,ctx):
        await ctx.channel.purge(limit = 1)
        text="要遊玩狼人殺的請點擊下方表情✅"
        wolf = await ctx.send(text)
        emoji='✅'
        wglist=[]
        await wolf.add_reaction(emoji)
        message_id = wolf.id
        if str(ctx.guild.id) in jdata:
            jdata[str(ctx.guild.id)].update({"wggamech":message_id})
            jdata[str(ctx.guild.id)].update({"wglist":wglist})
        else:
            jdata[str(ctx.guild.id)]={"wggamech":message_id}
            jdata[str(ctx.guild.id)]={"wglist":wglist}
        with open('./setting/wolfgame.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        guild=data.guild_id
        user=data.user_id
        channel=data.channel_id
        member=data.member
        emoji=data.emoji
        wglist=jdata[str(guild)]["wglist"]
        emojich=jdata[str(guild)]["wggamech"]
        if str(guild) in jdata:
            if str(emoji) == '✅'and member != self.maple.user and data.message_id == emojich:
                wglist.append(member.id)
                if str(guild) in jdata:
                    jdata[str(guild)].update({"wglist":wglist})
                else:
                    jdata[str(guild)]={"wglist":wglist}

        with open('./setting/wolfgame.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        guild=self.maple.get_guild(data.guild_id)
        guildstr=data.guild_id
        member=guild.get_member(data.user_id)
        emoji=data.emoji
        wglist=jdata[str(guildstr)]["wglist"]
        emojich=jdata[str(guildstr)]["wggamech"]
        emojich=int(emojich)
        if str(guildstr) in jdata:
            if str(emoji) == '✅'and member != self.maple.user and data.message_id == emojich:
                wglist.remove(member.id)
                if str(guildstr) in jdata:
                    jdata[str(guildstr)].update({"wglist":wglist})
                else:
                    jdata[str(guildstr)]={"wglist":wglist}

        with open('./setting/wolfgame.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)

    @commands.command()
    async def wgpeople(self,ctx):
        list=jdata[str(ctx.guild.id)]["wglist"]
        await ctx.send(f'目前資料庫內有{len(list)}筆資料喔~')
    @commands.command()
    async def cleanwg(self,ctx):
        wglist=[]
        jdata[str(ctx.guild.id)].update({"wglist":wglist})
        jdata[str(ctx.guild.id)].update({"wggamech":""})
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'謝謝大家的反應點擊,已清除清單資料了')



        



def setup(maple):
    maple.add_cog(wolfgame(maple))
