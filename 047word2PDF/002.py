import os
from docx2pdf import convert
import time

# 获取当前目录下所有文件
files = os.listdir()

# 遍历每个文件
for file in files:
    # 如果文件是.docx文件，则进行转换
    if file.endswith('.docx'):
        # 构造输入文件路径
        input_file = os.path.abspath(file)
        # 构造输出文件路径
        output_file = os.path.splitext(input_file)[0] + ".pdf"
        
        # 转换文件
        convert(input_file, output_file)

        print(f"Converted {input_file} to {output_file}")
        # 等待一段时间以确保 Word 实例被关闭
        time.sleep(1)
