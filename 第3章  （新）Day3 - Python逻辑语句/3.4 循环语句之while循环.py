# 循环:重复执行一段语句
"""
while循环的语法格式:
while 表达式:
    语句
"""

# 无限循环:死循环
# while True:
#     print('Hello world!')

# 有效次数循环
# 循环三要素:初始变量 条件判断 步进语句
count = 0
while count < 10:
    print(count)
    count += 1  # count自加1
