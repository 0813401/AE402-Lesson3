# from 模組 import 函式
from pytube import YouTube 

# def 函式名(正在寫的串流, 還沒寫入硬碟的資訊, 還剩下多少bytes沒下載完)
def showProgress(stream, chunk, bytes_remaining):
    
    size = stream.filesize 
    
    currentProgress = (size - bytes_remaining) * 100 / size
    
    print("目前進度： " + str(currentProgress) + "%")


# yt = YouTube('你想要的網址')
yt = YouTube("https://youtu.be/QkkvaiG1rJA", 
             on_progress_callback = showProgress)

stream = yt.streams.filter(only_audio = True).first()

stream.download()


