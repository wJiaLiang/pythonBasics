from spire.doc import *
from spire.doc.common import *

# 创建Document对象
document = Document()

# 加载Word文档
document.LoadFromFile(r"C:\Users\admin\Desktop\简历表.docx")

# 将文档保存为PDF格式
document.SaveToFile("Word转PDF.pdf", FileFormat.PDF)
document.Close()