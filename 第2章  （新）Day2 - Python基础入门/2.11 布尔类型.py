x = 10
y = 3.14

# 比较运算符 > >= < <= == !=
print(x > y)  # True
print(x < y)  # False

# 布尔值一般用于条件判断
age = 23
if age > 18:
    print('已成年')
else:
    print('未成年')

# 直接赋值
b1 = True
print(b1)
print(type(b1))  # <class 'bool'>

# 所有数据都有自己的bool值
print(bool(1))  # True
print(bool(0))  # False
# 零值：所有的数据类型中都有且只有一个值的bool状态是False 该值成为此类型的零值
# 整型：0 其他数据类型为空就是零值
print(bool([]))  # False
