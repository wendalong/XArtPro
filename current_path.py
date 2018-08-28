import os

# 查看当前文件的绝对路径
print(os.path.abspath(__file__))

# 看查当前文件所在的目录
abs_path = os.path.abspath(__file__)
print(os.path.dirname(abs_path))
