# 导入random模块和datetime模块
import random
import datetime

# 获取1-100的随机数
print(round(random.random() * 100))
# 打印当前时间：格式 年-月-日 时:分:秒
print(datetime.datetime.now().strftime('%Y-%m-%d %X'))
# 代码注释控制比例：3:1
# 三引号：多行注释
"""
多行注释
多行注释
"""
