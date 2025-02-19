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

numbers = list(range(1, 301))
third_prize = random.sample(numbers, 30)
for i in numbers:
    if i in third_prize:
        numbers.remove(i)
second_prize = random.sample(numbers, 6)
for i in numbers:
    if i in second_prize:
        numbers.remove(i)
first_prize = random.sample(numbers, 3)
first_prize.sort()
second_prize.sort()
third_prize.sort()
print(f'恭喜{str(first_prize).strip("[]")}号员工中得一等奖')
print(f'恭喜{str(second_prize).strip("[]")}号员工中得一等奖')
print(f'恭喜{str(third_prize).strip("[]")}号员工中得一等奖')
