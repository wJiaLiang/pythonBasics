
'''
制作视频录制器
实现功能：
1、倒计时开始进行录制
2、点击 键盘的 esc按键，就停止录制
3、打包成.exe， 直接点击就可以运行
'''
import cv2
from PIL import ImageGrab
import numpy as np
import datetime
from pynput import keyboard
import threading
from loguru import logger
import  time
import  os
# 初始化变量
is_running = True

'#创建录制过程生成的generate_video,用于生成录制视频'

def generate_video():
    '''
    生成录制视频
    :return:
    '''
    #当前时间戳为文件名字
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')
    file_name = (start_time + '录制视频')
    # file_name= input("输入录制文件的名称")
    screen = ImageGrab.grab()
    width,height = screen.size
    fource = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter('%s.mp4'% file_name,fource,20,(width,height))
    for n in range(3):
        logger.debug(str(3-n)+ '秒后开始录制')
        time.sleep(1)
    while True:
        im1 = ImageGrab.grab()
        im2 = cv2.cvtColor(np.array(im1),cv2.COLOR_RGBA2RGB)
        video.write(im2)
        if is_running is False:
            logger.debug('屏幕录制结束')
            break
    video.release()

'创建键盘监听函数 press_keyboard,监听输入，如果按下esc则改变运行状态'
# is_running = False #注释掉
def press_keyboard(key):
    '''
    键盘监听函数
    :param key:
    :return:
    '''
    global  is_running
    if key == keyboard.Key.esc:
        logger.debug('已按下ESC键，录制结束')
        is_running = False
        return False

if __name__ == '__main__':
    thread_ = threading.Thread(target=generate_video)
    thread_.start()
    logger.debug('开始进入录制视频')
    with keyboard.Listener(on_press = press_keyboard) as listener:
        listener.join()