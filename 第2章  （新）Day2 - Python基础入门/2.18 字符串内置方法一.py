# 字符串内置方法
# 1.upper lower
s1 = 'Hello World'
print(type(s1))  # <class 'str'>
# 将字符串内所有的字符大写
print(s1.upper())  # HELLO WORLD
# 将字符串内所有的字符小写
print(s1.lower())  # hello world

# 2.startswith endswith
# 判断该字符串是否以什么内容开头 返回一个布尔值
print(s1.startswith('H'))  # True
# 判断该字符串是否以什么内容结尾 返回一个布尔值
print(s1.endswith('d'))  # True
