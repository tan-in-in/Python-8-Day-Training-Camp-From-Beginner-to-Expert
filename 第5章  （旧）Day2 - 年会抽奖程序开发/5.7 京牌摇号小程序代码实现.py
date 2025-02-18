import random
import string

count = 0
while count < 3:
    print(f'第{count + 1}次摇号')
    car_nums = []  # 存储供用户选择的车牌号
    for i in range(20):
        car_num = f'京{random.choice(string.ascii_uppercase)}·'f'{"".join(random.sample(string.ascii_uppercase + string.digits, 5))}'
        car_nums.append(car_num)  # 把生成的号码添加到列表
        print(f'{i + 1}.{car_num}')
    choice = input('输入你喜欢的车牌号:')
    if choice in car_nums:
        print(f"恭喜你选择了新车牌号:{choice}")
        exit('程序退出')
    else:
        count += 1

