# 随机验证码案例
# 模块 import
import random  # 生成随机数模块
import string  # 字符串模块

# 在字符串中随机选择一个字符
# char = random.choice('0123456789')

# 生成26位小写字母: abcdefghijklmnopqrstuvwxyz
# print(string.ascii_lowercase)
# 生成26位大写字母: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_uppercase)
# 生成0-9数字:0123456789
# print(string.digits)

all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
# print(all_chars)


# 随机生成一个字符
def show_char():
    chars = ''
    for i in range(6):
        chars += random.choice(all_chars)
    print(chars)


for j in range(10):
    show_char()

