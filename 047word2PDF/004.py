import os
from pdf2docx import Converter

# 获取当前目录下所有文件
files = os.listdir()

# 遍历每个文件
for file in files:
    # 构造文件路径
    file_path = os.path.join(os.getcwd(), file)
    # 如果文件是.pdf文件，则进行转换
    if file.endswith('.pdf'):
        # 构造输出文件路径
        output_file = os.path.splitext(file_path)[0] + ".docx"

        # 转换文件
        cv = Converter(file_path)
        cv.convert(output_file, start=0, end=None)
        cv.close()

        print(f"Converted {file_path} to {output_file}")
