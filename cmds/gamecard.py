import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random,datetime,os,asyncio
import json
with open('./setting/compass.json','r',encoding='utf8') as mlink:
    jdata = json.load(mlink)
compassur=["終極係無防守戰法","武術家的超加速","樂團團長 指揮家","-蒼王宮- 恩寵天使 索恩=尤利耶夫","湮滅長程步槍Hum-Buster","名校足球社 閃電射門","掌管靈魂的聖天使 加百列","妖炎參謀 月夜叉","超美味!!! 熱量傳揚 遠距教學空手道","機航師彈 飛船","狂暴的天空之王 烈焰龍","慶典的壓軸！煙火","我最喜歡媽媽了","戰略之燈／國防長官芙蕾","聯合宇宙軍 強襲壓制型 裝甲多腳戰車","慶典的重頭戲！龍形煙火","任意門","妖軍一統 大將","聯合宇宙軍 防護罩摧毀波","恆星間傳送裝置 Tele-Pass","反導砲 加諾涅•法伊耶爾","爸爸陪我玩","米娜&露娜&蕾娜的大拍賣戰爭","時髦盟友忍者 -任生笑美美寶","*絢爛之美* 最多&最初&無限大","-蒼王宮- 聖歌連隊 旋律","【黛露敏】惡魔薄荷始龍","合力攻擊！夢想☆天使之箭","超美味!!! 熱量霸王 波尼亞托夫斯基一族","| | |狐笑| | |祓三姊妹 夢色 | 桃色","戰陣之燈/VDN-93 強襲登陸艦 尤克特拉希爾","學園的王者 學生會執行部","全方位攻擊","迅雷的科學家 阿巴坎","聯合宇宙軍 衛星加農砲","全員集合 ! 魔法少女莉莉卡☆露露卡","小千的外遇懲罰狙擊","創靈的庇佑 泰奧瓦","*真實之美* 喬凡尼","【黛露敏】惡魔薄荷鬼龍把拔敏","絕夢魔女 啟示錄★露露卡","| | |貍原| | | 破戒怨士 喰色","某家用機械的叛亂","命運的女神 進化☆莉莉卡","革命的旗幟","自深淵湧出的黑影","夢想☆魔法陣","全天首都防護罩 Hum-Sphere LLIK","銀河防衛機器人 Unidoll-2525","慶典的精隨！男人的手筒煙火","磐石 Hum-Unknown","神祭官 安潔．索雷","獨災者 安古利夫．基夫特","忘愛的長女 亞歷珊卓","樂團公主 歌姬","紅薔薇的副團長 友情","-蒼王宮- 冰冠女王 依迪雅=N=由朗布魯克","加魯魯的閃亮亮凸額頭戰車","雷靈的庇佑 雷鳥","對手狂刃忍者 -幽幽院夢良良-","-蒼王宮- 終結禁獸 導彈","背負亡妻的庇佑","＃夜光犯罪特區 ＃小讚演唱會","＃夜光犯罪特區 ＃整夜都是本大爺讚美會","能源罐 100000ml"]
owner=560091826170626071
cpt=0
class game_card(Cog_Extension):

    @commands.command()
    async def p_bright(self,ctx,name,num:int,probability:int):
        list=[]
        for sampling in range(num):
            bright=random.randint(1,100)
            if bright <=probability:
                list.append(bright)
        await ctx.send(f"{name}的亮晶晶{num}次抽取中成功亮晶晶了{len(list)}次(此次設定%數為{probability}%)")
    
    @commands.command()
    async def compasscard(self,ctx):
        UR=[]
        SR=[]
        i=0
        user=ctx.author.display_name
        while i < 60:
            bright=random.randint(0,99)
            i= i + 1
            if bright < 1:
                urcard=random.choice(compassur)
                UR.append(urcard)
            if 1 <= bright < 10:
                SR.append(bright)
            if i==60:
                ur=(len(UR))
                if ur < 1 :
                    await ctx.send(f"""{user}這次60次抽卡中成功抽到了{len(UR)}張UR跟{len(SR)}張SR...BM投多一點吧<:_cat:878216638971920414>""")
                if 0 < ur <= 3 :
                    await ctx.send(f"""{user}這次60次抽卡中成功抽到了{len(UR)}張UR跟{len(SR)}張SR,很厲害喔<:megu01:575877808052764682>
以下是你抽到的UR卡:{UR}""")
                if 3 < ur :
                    await ctx.send(f"""{user}這次60次抽卡中成功抽到了{len(UR)}張UR跟{len(SR)}張SR,歐皇出來了!!!<:kokuriko03:922352410884730881>
以下是你抽到的UR卡:{UR}""")
        with open('./setting/compass.json','r',encoding='utf8') as mlink:
             jdata = json.load(mlink)
        if str(ctx.message.author.id) in jdata:
            URnum=jdata[str(ctx.message.author.id)]["URnum"]
            SRnum=jdata[str(ctx.message.author.id)]["SRnum"]
            BMnum=jdata[str(ctx.message.author.id)]["BM"]
            card=jdata[str(ctx.message.author.id)]["card"]
            URnum=URnum+len(UR)
            SRnum=SRnum+len(SR)
            BMnum=BMnum+5000
            card=card+1
            jdata[str(ctx.message.author.id)].update({"URnum":URnum})
            jdata[str(ctx.message.author.id)].update({"SRnum":SRnum})
            jdata[str(ctx.message.author.id)].update({"BM":BMnum})
            jdata[str(ctx.message.author.id)].update({"card":card})
        else:
            URnum=len(UR)
            SRnum=len(SR)
            BMnum=5000
            card=1
            jdata[str(ctx.message.author.id)]={"URnum":URnum,"SRnum":SRnum,"BM":BMnum,"card":card}
        with open('./setting/compass.json','w',encoding='utf8') as mlink:
            json.dump(jdata,mlink,indent=4)
    @commands.command()
    async def cprecord(self,ctx):
        with open('./setting/compass.json','r',encoding='utf8') as mlink:
             jdata = json.load(mlink)
        if str(ctx.message.author.id) in jdata:
            icon=ctx.author.avatar_url
            user=ctx.author.display_name
            URnum=jdata[str(ctx.message.author.id)]["URnum"]
            SRnum=jdata[str(ctx.message.author.id)]["SRnum"]
            BMnum=jdata[str(ctx.message.author.id)]["BM"]
            card=jdata[str(ctx.message.author.id)]["card"]
            embed=discord.Embed(title="個人當天抽卡紀錄",timestamp=datetime.datetime.utcnow())
            embed.set_author(name=user, icon_url=icon)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/953597155904487424/995905671298027530/unknown.png")
            embed.add_field(name="總UR:", value=f"{URnum}", inline=False)
            embed.add_field(name="總SR:", value=f"{SRnum}", inline=False)
            embed.add_field(name="總花費BM:", value=f"{BMnum}", inline=False)
            embed.add_field(name="60抽次數:", value=f"{card}", inline=False)
            await ctx.send(embed=embed)
    @commands.command()
    async def clearcp(self,ctx):
        if ctx.message.author.id==owner :
            os.remove("./setting/compass.json")
            mlink ={}
            json_object = json.dumps(mlink, indent = 4)
            with open("./setting/compass.json", "w") as mlink:
                mlink.write(json_object)
            await ctx.send(f'已清除抽卡資料')
        else:
            await ctx.send(f'你非開發者無法使用該指令')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        async def cprecordtime():
                await self.maple.wait_until_ready()
                while cpt==0:
                    now_time=datetime.datetime.utcnow() + datetime.timedelta(hours=8)
                    now_time = now_time.strftime("%H%M")
                    if now_time == "0001":
                        print(1)
                        os.remove("./setting/compass.json")
                        mlink ={}
                        json_object = json.dumps(mlink, indent = 4)
                        with open("./setting/compass.json", "w") as mlink:
                            mlink.write(json_object)
                        await asyncio.sleep(60)
                    else:
                        await asyncio.sleep(1)

        self.bg_task = self.maple.loop.create_task(cprecordtime())
    
    
        
def setup(maple):
    maple.add_cog(game_card(maple))