# 字符串定义 特性
# 字符串:一个有序的字符的合集 用于在计算机里存储和表示文本信息
# 有序 索引 切片 不可变
s = 'hello world'
print(s[0:5])  # 顾头不顾尾
print(id(s))  # 1766053474288
s = 'hello'
print(id(s))  # 1766053386768

# 字符串常用操作
# 1.center 字符串填充
# ------------hello-------------
print(s.center(30, '-'))

# 2.count 计数
print(s.count('l'))  # 2

# 3.endswith startswith 判断结尾开头
print(s.startswith('h'))  # True
print(s.endswith('l'))  # False

# 4.find 查找字符在字符串中索引 找不到会返回-1
print(s.find('l'))  # 2

# 5.isdigit 判断是否是整数
print(s.isdigit())  # False

# 6.join 字符串的拼接
print(' '.join(['1', '2', '3']))  # 1 2 3

# 7.replace 字符串替换
print(s.replace('l', 'a'))  # heaao

# 8.split 分割字符串
print(s.split('l'))  # ['he', '', 'o']
