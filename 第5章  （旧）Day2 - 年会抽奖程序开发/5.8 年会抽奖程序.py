"""
年会抽奖程序
300名员工
一等奖 3名
二等奖 6名
三等奖 30名
规则
一共抽三次 第一次抽三等奖 第二次抽二等奖 第三次抽一等奖
每个员工限中奖一次 不能重复
"""
import random

numbers = []
for i in range(1, 301):
    numbers.append(str(i))
third_prize = random.sample(numbers, 30)
for i in numbers:
    if i in third_prize:
        numbers.remove(i)
second_prize = random.sample(numbers, 6)
for i in numbers:
    if i in second_prize:
        numbers.remove(i)
first_prize = random.sample(numbers, 3)
print(f'恭喜{" ".join(first_prize)}号员工中得一等奖')
print(f'恭喜{" ".join(second_prize)}号员工中得二等奖')
print(f'恭喜{" ".join(third_prize)}号员工中得三等奖')
