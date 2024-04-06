from PIL import Image
import os

# 获取当前目录下所有文件
files = os.listdir()

# 遍历每个文件
for file in files:
    # 构造文件路径
    file_path = os.path.join(os.getcwd(), file)
    # 如果文件是.png文件，则进行转换
    if file.endswith('.png'):
        # 打开PNG文件
        with Image.open(file_path) as img:
            # 将图像调整为128x128尺寸
            img_resized = img.resize((128, 128))
            # 构造输出ICO文件路径
            output_file = os.path.splitext(file_path)[0] + ".ico"
            # 将PNG图像保存为ICO图标
            img_resized.save(output_file)

            print(f"Converted {file_path} to {output_file}")
