# 1.ord chr相反 答应字符对应的10进制数字
print(ord('a'))  # 97

# 2.enumerate 迭代器
for i, j in enumerate(range(10)):
    print(i, j)

# 3.round 保留浮点数
print(round(3.1415926, 5))  # 3.14159

# 4.type 返回变量数据类型
print(type('1'))  # <class 'str'>

# 5.zip
a = [1, 2, 3]
b = [4, 5, 6]
for i in zip(a, b):
    print(i)

# 6.filter 把列表里的每一个元素交给第一个参数(函数)运行, 若结果为真则返回值
