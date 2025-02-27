# 1.abs 取绝对值
print(abs(-10))  # 10

# 2.all 判断容器数据类型里面的变量
a = [0, 1, 2, 3, 4]
print(all(a))  # False

# 3.any 和all相反
print(any(a))  # True

# 4.bool 判断变量布尔值
print(bool(0))  # False

# 5.chr 根据数字返回相应ascii字符
print(chr(97))  # a

# 6.dict 生成字典

# 7.dir 返回当前程序环境下的内存变量
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a']
print(dir())

# 8.locals 返回当前程序环境下的内存变量名和变量值
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000029D76D9BC20>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\code\\python\\Python-8-Day-Training-Camp-From-Beginner-to-Expert\\第8章  （旧）Day5 - 函数编程\\8.8 常用内置函数_1.py', '__cached__': None, 'a': [0, 1, 2, 3, 4]}
print(locals())

# 9.map
l = list(range(10))
print(l)


def calc(x):
    return x * x


print(map(calc, l))  # <map object at 0x0000014FC5D342B0>
m = map(calc, l)  # 迭代器
for i in m:  # 每循环一次 就把列表里的每一个元素扔给calc函数执行
    print(i)

# 10.max
print(max(l))  # 9

# 11.min
print(min(l))  # 0

# 12.sum
print(sum(l))  # 45
