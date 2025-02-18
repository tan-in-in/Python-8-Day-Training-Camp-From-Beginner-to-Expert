# 输入函数 input() IO阻塞函数

# 案例1
# name = input('输入你的名字：')
# age = int(input('输入你的年龄：'))
# print(f'名字：{name}，年龄：{age}。')

# 案例2
# num1 = input('num1:')  # <class 'str'>
# 类型转换
numInt1 = int(input('numInt1:'))  # <class 'int'>
numInt2 = int(input('numInt2:'))
print(f'{numInt1}+{numInt2}={numInt1+numInt2}')

# 输出函数 print end参数
# 逗号 打印多个值
print(numInt1, numInt2)
print(numInt1, numInt2, end='')
