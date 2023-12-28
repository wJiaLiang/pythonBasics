import wave
import threading
from os import remove, mkdir, listdir
from datetime import datetime
from time import sleep
import pyaudio
from PIL import ImageGrab
from numpy import array
import cv2
from moviepy.editor import *
import os
# import win32api
import time
from multiprocessing import cpu_count

CHUNK_SIZE = 1024
CHANNELS = 2
FORMAT = pyaudio.paInt16
RATE = 48000
allowRecording = True
CPU_COUNT = cpu_count() -2

event = threading.Event()
path = './video'

if not os.path.exists(path):
    os.mkdir(path)

# 显示画面
def imshow(frame):
    # color = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow('v', frame)
    cv2.waitKey(40)

def record_audio2():
    # 实例化相关的对象
    p = pyaudio.PyAudio()
    event.wait()
    sleep(3)
    # 打开相关的流，然后传入响应参数
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK_SIZE)
    # 打开wav文件
    wf = wave.open(audio_filename, 'wb')
    # 设置相关的声道
    wf.setnchannels(CHANNELS)
    # 设置采样位数
    wf.setsampwidth(p.get_sample_size((FORMAT)))
    # 设置采样频率
    wf.setframerate(RATE)

    while allowRecording:
        data = stream.read(CHUNK_SIZE)
        # 写入数据
        wf.writeframes(data)
    
    # 关闭流
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

def record_audio():
    p = pyaudio.PyAudio()
     #等待摄像头启动好，然后大家一起等3秒开始录制
    event.wait()
    sleep(3)
    # 创建输入流
    stream = p.open(format=FORMAT, channels=CHANNELS,rate=RATE, input=True, frames_per_buffer=CHUNK_SIZE)
    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    while allowRecording:
         # 从录音设备读取数据， 直接写入wav文件     
         data = stream.read(CHUNK_SIZE)     
         wf.writeframes(data)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

    
def record_screen():
     # 录制屏幕
     # 等待摄像头启动好，然后大家一起等3秒开始录制
     event.wait()
     sleep(3)
     im = ImageGrab.grab()
     video = cv2.VideoWriter(screen_video_filename, cv2.VideoWriter_fourcc(*'XVID'), 25, im.size) # 侦速和视频宽度、高度
     while allowRecording:

         im = ImageGrab.grab()
         im = cv2.cvtColor(array(im), cv2.COLOR_RGB2BGR)
         video.write(im)
     video.release()

def record_webcam():

    # 参数0表示笔记本自带摄像头
    cap = cv2.VideoCapture(0)
    # 启动好摄像头，发出通知，大家一起等3表然后开始录制
    event.set()
    sleep(3)
    aviFile = cv2.VideoWriter(webcam_video_filename, cv2.VideoWriter_fourcc(*'MJPG'), 25, (640, 480))

    while allowRecording and cap.isOpened():
        # 捕捉当前头像， ret=True表示成功，Fasle表示失败
        ret, frame = cap.read()
        if ret:
            aviFile.write(frame)
    aviFile.release()
    cap.release()

num = 0
def keepTime():
    while  True:
        sleep(1)
        num+=1
        print('\r',num,end='',flush=True)


if __name__ == '__main__':
    now = str(datetime.now())[:19].replace(":", "_")
    audio_filename = f'./video/{now}.mp3'
    # webcam_video_filename = f'./video/t{now}.avi'
    screen_video_filename = f'./video/tt{now}.avi'
    video_filename = f'./video/{now}.mp4'
    # 创建两个线程， 分别录音与录屏
    t1 = threading.Thread(target=record_audio)
    t2 = threading.Thread(target=record_screen)
    # t3 = threading.Thread(target=record_webcam)
    t4 = threading.Thread(target=keepTime)

    # 创建时间，用户多个线程同步，等摄像头准备以后再一起等3秒开始录制
    event.clear()

    print("按s键,回车后开始录制")
    if input() == 's':
        event.set()
    # for t in (t1, t2, t3):
    for t in (t1, t2):
        t.start()


    # 等待摄像头准备好，提示用户3秒钟以后开始录制
    event.wait()
    print('正在录制中...',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print('按q键结束录制')

    while True:
        if input() == 'q':
            print('录制结束',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            break

    allowRecording = False
    # for t in (t1, t2, t3):
    for t in (t1, t2):
        t.join()

    # 把录制的音频和屏幕截图合成视频文件
    audio = AudioFileClip(audio_filename)
    video1 = VideoFileClip(screen_video_filename)
    ratio1 = audio.duration/video1.duration
    print("时间",video1.duration)
    video1 = (video1.fl_time(lambda t: t/ratio1, apply_to=['video']).set_end(audio.duration))
    # video2 = VideoFileClip(webcam_video_filename)
    # ratio2 = audio.duration/video2.duration
    # video2 = (video2.fl_time(lambda t: t/ratio2, apply_to=['video'])).set_end(audio.duration).resize((320, 240)).set_position(('right','bottom'))
    # video = CompositeVideoClip([video1, video2]).set_audio(audio)
    video = CompositeVideoClip([video1]).set_audio(audio)
    video.write_videofile(video_filename, codec='libx264', threads = CPU_COUNT, fps=30)
    # 设置码率可以调视频的大小 bitrate
    # video.write_videofile(video_filename, codec='libx264',bitrate="2000k", threads = CPU_COUNT, fps=30)

    # 删除历史音频文件和视频
    remove(audio_filename)
    remove(screen_video_filename)
    # remove(webcam_video_filename)