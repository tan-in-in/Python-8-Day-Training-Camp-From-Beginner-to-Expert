# 切片
num = list(range(1,11))
print(num)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[0:4])  # [1, 2, 3, 4]

print(num[4:])  # [5, 6, 7, 8, 9, 10] 省略写法
print(num[4:10])  # [5, 6, 7, 8, 9, 10] 超标写法

# 倒着切 从左往右切
print(num[-3:-1])  # [8, 9]
print(num[-1:-3])  # []

# 步长
print(num[::2])  # [1, 3, 5, 7, 9]

# 反转
print(num[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
num.reverse()
print(num)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 排序 sort()
num.sort()
print(num)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 循环列表元素
for i in enumerate(num):
    print(i[0], i[1])

