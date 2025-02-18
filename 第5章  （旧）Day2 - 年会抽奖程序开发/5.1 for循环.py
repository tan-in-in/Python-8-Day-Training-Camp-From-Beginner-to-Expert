# for i in range(10):
#     print(i)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(10)))

# for i in range(5, 11):
#     print(i)

# 循环猜年龄
# age = 26
# for i in range(3):
#     guess = int(input('输入你的猜测:'))
#
#     if guess > age:
#         print('猜大了')
#     elif guess < age:
#         print('猜小了')
#     else:
#         # print('猜对了')
#         # break
#         exit('猜对了')  # 直接退出程序

# for循环打印0-100的奇偶数
for i in range(0, 101):
    if i % 2 == 0:  # 代表是偶数
        print(f'{i}是偶数')
