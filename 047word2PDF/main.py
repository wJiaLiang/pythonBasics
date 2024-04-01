import os

# 遍历当前目录及其子目录，打印出所有文件名
for root, dirs, files in os.walk('.'):
    for file in files:
        # print(dirs)
        # 当前文件的绝对路径
        print(os.path.abspath(file))
        disf = os.path.abspath(file)

        # 将多个路径片段连接起来，生成一个合法的路径。
        print(os.path.join(root, file))

        # 将路径分割成基名和扩展名两部分并以元组形式返回。
        print(os.path.splitext(disf))
