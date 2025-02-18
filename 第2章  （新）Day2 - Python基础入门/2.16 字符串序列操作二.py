# 字符串的拼接 使用加号+
s1 = 'hello'
s2 = 'world'
print(s1 + s2)
print(s1 + " " + s2)
# 格式化输出
print(f"{s1} {s2}")
print("*" * 20)

# 计算字符串对象的长度 内置函数 len()
print(len(s1+s2))  # 容器类型都有长度
# 中文 占一个长度
s3 = 'i am 谭'
print(len(s3))

# 判断 in 针对容器类型 判断某个成员是否存在
print('am' in s3)  # True
