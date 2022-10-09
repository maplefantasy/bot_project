import discord
from discord.ext import commands
from core.classes import Cog_Extension
import cv2,asyncio,time,datetime
import mediapipe as mp

tt=0

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

async def cv(self):
    cap = cv2.VideoCapture(0)
    time1 = time.time()
    with mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0) as face_detection:
        while True:
            success, image = cap.read()
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.detections:  #是否出現人臉
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)
                if time.time() - time1 > 5: #判斷上一次紀錄的時間戳減去當前時間戳是否超過5秒
                    nowtime=datetime.datetime.utcnow() + datetime.timedelta(hours=8)
                    nowtime = nowtime.strftime("%Y/%m/%d %H:%M:%S")
                    time1 = time.time()
                    cv2.imwrite('./picture/out.jpg', image) #暫存圖片
                    self.channel=self.maple.get_channel(953597155904487424) #傳送檔案至私人通知
                    await self.channel.send(f"""0號攝影機捕捉人臉成功
台灣時間:{nowtime}""")
                    await self.channel.send(file=discord.File('./setting/out.jpg'))

            cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
            await asyncio.sleep(0.1)
            if cv2.waitKey(1) == 32:
              break

class Opencvtest(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.working_guild = []
        async def time_task():
            await self.maple.wait_until_ready() #等待機器人準備
            while tt == 0:#bot沒關閉繼續loop
                await cv(self)  #執行cv函數
                
        self.bg_task=self.maple.loop.create_task(time_task()) #創建一個背景作業

def setup(maple):
    maple.add_cog(Opencvtest(maple))