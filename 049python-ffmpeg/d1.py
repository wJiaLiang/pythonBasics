"""
pip install ffmpeg-python
使用该库，需要自行安装FFmpeg，如果电脑已经安装了，可以忽略本步骤。
这里推荐直接使用conda进行安装，可以省下很多麻烦，其他的安装方式自行百度。

ffmpeg 压缩工具
https://www.zywvvd.com/notes/coding/python/tools/python-ffmpeg/python-ffmpeg/

"""

import ffmpeg

# 将视频反转
stream = ffmpeg.input('D:/Z_myProject/python/pythonBasics/048录屏/video/2023-12-29 23_06_09.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)

