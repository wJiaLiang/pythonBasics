import pyaudio
import wave

# 录制扬声器的声音

# 每个缓冲区的帧数
CHUNK = 1024
# 采样位数
FORMAT = pyaudio.paInt16
# 单声道
CHANNELS = 1
# 采样频率
RATE = 44100

# 录制声音的相关函数（参数1：录制的路径；参数2：录制的声音秒数）
def record_audio(wave_out_path, record_second):
    # 实例化相关的对象
    p = pyaudio.PyAudio()
    # 打开相关的流，然后传入响应参数
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    # 打开wav文件
    wf = wave.open(wave_out_path, 'wb')
    # 设置相关的声道
    wf.setnchannels(CHANNELS)
    # 设置采样位数
    wf.setsampwidth(p.get_sample_size((FORMAT)))
    # 设置采样频率
    wf.setframerate(RATE)

    for _ in range(0, int(RATE * record_second / CHUNK)):
        data = stream.read(CHUNK)
        # 写入数据
        wf.writeframes(data)
    # 关闭流
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

if __name__ == '__main__':
    record_audio('text.mp3', 10)