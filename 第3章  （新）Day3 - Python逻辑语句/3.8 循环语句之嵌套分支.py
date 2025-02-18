# 案例2:在循环中嵌套分支或循环
# 计算1-100的所有偶数和
# ret = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         if i < 100:
#             print(f'{i}+', end='')
#         else:
#             print(f'{i}', end='')
#         ret += i
#
# print(f'={ret}')

# 计算1-100所有能整除13的数字和
# ret = 0
# for i in range(1, 101):
#     if i % 13 == 0:
#         if i < 100:
#             print(f'{i}+', end='')
#         else:
#             print(f'{i}', end='')
#         ret += i
#
# print(f'={ret}')

# 无限循环嵌套分支语句
print("""
    1.前进
    2.攻击
    3.购买装备
    4.查看地图
    5.回城
    """)
while True:
    choice = input('请输入你的选择:')
    if choice == '1':
        print('前进')
    elif choice == '2':
        print('攻击')
    elif choice == '3':
        print('购买装备')
    elif choice == '4':
        print('查看地图')
    elif choice == '5':
        print('回城')
    else:
        print('程序退出!')
        break
