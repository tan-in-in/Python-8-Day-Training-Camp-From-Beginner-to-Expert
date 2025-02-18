# 摇号小程序
"""
需求:
允许用户最多选三次
每次放出20个车牌供用户选择
京[A-Z]-[xxxxx],可以是数字和字母的组合
"""
import string
import random  # choice simple randint

words = string.ascii_uppercase
numbers = string.digits

print('摇号程序开始-----------------')
for i in range(3):
    print(f'第{i + 1}次')
    for j in range(20):
        temp = random.sample(words + numbers, 5)
        print(f'京{random.choice(words)}·{"".join(temp)}')
    if i < 2:
        flag = input('是否继续>>>')
        if flag == '是':
            continue
        else:
            print('程序退出')
            break
