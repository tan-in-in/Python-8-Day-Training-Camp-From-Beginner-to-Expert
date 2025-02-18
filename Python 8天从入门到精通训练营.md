# Python 8天从入门到精通训练营

# 第1章 （新）Day1 - 初识Python

## 1.1 计算机组成原理

计算机组成原理

CPU 存储器 输入设备 输出设备

磁盘 内存 寄存器

## 1.2 编程语言

沟通双方：人和计算机（二进制->机器语言）

使计算机完成特定的操作

编程语言发展历程：机器语言（1930-1960）->汇编语言（第一个汇编语言-1947伦敦大学）->现代高级语言（1972-C语言/1980-C++/1991-python/VB/1994-Java/1995-PHP/JavaScript） 根据使用场景 选择合适变成语言

封装越高 开发效率越高 运行性能越低

计算机只能识别机器语言。

## **1.3 编译型语言和解释型语言**

编程语言分类

编译型：C C++ GO ...

解释型：Python PHP Ruby JavaScript

混合型：Java

编译型语言优缺点：

1.一次性编译成平台相关的机器语言文件 运行时脱离开发环境 运行效率高

2.与特定平台相关 一般无法移植到其他平台

解释型语言有缺点：

1.解释型语言每次都需要将源代码解释成机器码执行 执行效率低

2.只要平台提供相应的解释器 就可以运行源代码 所以可以方便源程序移植

## 1.4 Python环境安装

[python官网](https://www.python.org)

下载版本：3.6版本以上 新版本最近一个

安装流程：选择自定义安装（设置安装路径）->添加到系统环境

## 1.5 终端环境

命令窗口->可视化窗口

win+R->cmd:打开命令窗口

dir:显示文件夹下的目录

cd:切换文件夹

cd..:返回上一层

## **1.6 环境变量配置**

添加系统环境变量

path

## **1.7 交互式命令行**

1.交互器命令行（只能做一些简单的测试）：注意要使用英文半角符号，否则要报错！

```python
print('hello world')
```

2.文件书写py代码：python文件的后缀为.py

## **1.8 PyCharm的安装与使用**

python集成开发环境（IDE）

pycharm官网：https://www.jetbrains.com

```python
import datetime

print(datetime.datetime.now())
```

# 第2章 （新）Day2 - Python基础入门

## **2.1 课程介绍**

基本语法 变量 基本数据类型 运算符

## 2.2 环境切换

配置python解释器

创建文件夹

## **2.3 语句分隔符**

```python
# 在python中 通常使用换行符作为语句分隔符 每个语句独占一行
print('hello world!')
print(1 + 1)
# 另外 在某些情况下 需要在同一行打印多个字符串 可以使用分号;作为语句分隔符
print('hello world!');print(1 + 1)
# 需要注意的是 虽然分好可以用作语句分隔符 但在python中并不常用 通常我们还是建议每个语句独占一行 这样可以提高代码的可读性和可维护性
```

## **2.4 注释语句**

注释：提高代码可读性的一种方式 注释内容会被python解释器忽略

python支持单行注释和多行注释两种形式

需要注意的是 注释是编写高质量python的中药组成部分 良好的注释可以提高代码的可读性和可维护性 使代码更易于理解 因此 在编写python代码时 应该适当的添加注释。

```python
# 导入random模块和datetime模块
import random
import datetime

# 获取1-100的随机数
print(round(random.random() * 100))
# 打印当前时间：格式 年-月-日 时:分:秒
print(datetime.datetime.now().strftime('%Y-%m-%d %X'))
# 代码注释控制比例：3:1
# 三引号：多行注释
"""
多行注释
多行注释
"""
```

## **2.5 pep8规范**

PEP8是python官方代码风格指南 旨在提供一致 易于阅读和易于维护的python代码 PEP8规范包括以下方面：

1. 缩进：使用四个空格表示缩进
2. 行长：每行代码不应超过79个字符
3. 命名规范：变量名应以小写字母开头 使用下划线分割多个单词 类名应该以大写字母开头 使用驼峰命名法
4. 空格：在运算符两侧 逗号后以及冒号后应添加空格
5. 注释：注释应该清晰 简洁 使用英文书写 注释应该说明代码的作用 而不是如何实现
6. 函数和类：函数和类之间应该用两个空行分割
7. 导入：每个导入应该单独成行 避免使用通配符号导入
8. 括号：在函数调用和定义中 括号内部应该没有空格

除此之外 PEP8还涵盖了代码布局 字符串引号 空行 文件编码等方面的规范

遵守PEP8规范可以增加代码的可读性和可维护性 这对于团队开发 代码重构和代码维护都非常有帮助 建议python开发者遵守这些规则 以便于其他python开发者协作 并使代码更易于理解和维护。

```python
# 规范不是语法
# 快捷键：ctrl+alt+l
# PEP8: W292 no newline at end of file
```

## **2.6 变量初识**

在Python中 变量是一个标识符 用于引用存储在计算机内存中的数据 每个变量都有一个名称和一个关联的值 可以将值存储在变量中并在程序中多次使用

1. 变量名：变量名是用于表示变量的字符串 变量名由字母 数字和下划线组成 必须以字母或下划线开头 不能以字母开头
2. 使用等号将一个值赋给一个变量
3. 在变量赋值时 python会自动为变量选择适当的数据类型

```python
# 变量：标识符 用来引用存储在计算机内存中的数据

# 版本1
# print(1 + 2)
# print(1 - 2)
# print(1 * 2)
# print(1 / 2)

# 版本2
x = 1  # 赋值语句
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
```

## **2.7 变量值多次使用**

```python
x = 1  # 赋值语句
y = 2
z = x + y
print(z)
print(x - y)
print(x * y)
print(z * 10)
```

## 2.8 变量值修改v2

```python
x = 10
print(x)
# 变量可以重复赋值 变量名应该见名知意
x = 20
print(x)
```

## 2.9 变量命名规范v2

```python
"""
python的变量命名规范通常遵循以下规则：
    变量名只能包含字母 数字和下划线 不能以数字开头
    变量名不能使用保留字或内置函数
    变量名应该具备描述性 以便代码的可读性更高
    变量名应该遵循一定的命名约定 区分大小写 使用下划线隔开 驼峰命名法
"""
```

## 2.10 整型和浮点型

基本数据类型：整型和浮点型 布尔类型 字符串类型

```python
# 整型 Integer
x = 10
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>
```

## **2.11 布尔类型**

```python
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
```

## **2.12 创建字符串**

```python
# 字符串：文本数据
# 方式一 单引号
s1 = 'hello'
# 方式二 双引号
s2 = "world"
# 方式三 三引号
s3 = '''
!
'''
s4 = """
    1.购买道具
    2.攻击
    3.逃跑
    4.退出
"""
print(s4)
```

## 2.13 字符串的转义符

```python
# 转移符号：\
# 功能：将某些普通符号给予特殊功能 将一些特殊功能的符号普通化

# \n 换行
s = 'i am yuan \nmy age is 19'
print(s)

s2 = "let's Go!"
# s3 = 'let's Go!'  # SyntaxError: unterminated string literal (detected at line 9) SyntaxError：未终止的字符串文字（在第 9 行检测到）
# \' 表示'
s3 = 'let\'s Go!'
print(s2)
print(s3)

# C:\Users\TAN\Desktop\Python8天训练营课件
# \\ 表示 \
print('C:\\Users\\TAN\\Desktop\\Python8天训练营课件')
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
```

## 2.14 格式化输出

```python
# 字符串格式化输出
# 固定输出
print('名字Tan，年龄20，身高167')

# 变量输出
nane = 'Tan'
age = 20
height = 167
# 方式一 3.6版本后解释器拥有 推荐
print(f'名字{nane}，年龄{age}，身高{height}')
# 方式二
print('名字%s，年龄%d，身高%d' % (nane, age, height))
```

## 2.15 字符串序列操作一

```python
# 序列类型 容器 有序
s1 = 'hello world'
# 索引 从0开始 字符串[索引] 查询字符
# python支持正索引和负索引
print(len(s1))  # 字符串长度：11
# 索引操作：拿取一个字符
print(s1[0])  # 第一个的字符：h
print(s1[-1])  # 最后一个字符：d

# 切片操作 拿取一段字符串 字符串[开头：结尾：步长（step，默认为1）] 步长为正：从左向右切片 步长为负：从右向左切片
print(s1[0:2])  # 顾头不顾尾
print(s1[3:])  # 缺省状态 取到最后或者从最开头取
print(s1[3::2])  # 步长为2
```

## **2.16 字符串序列操作二**

```python
# 字符串的拼接 使用加号+
s1 = 'hello'
s2 = 'world'
print(s1 + s2)
print(s1 + " " + s2)
# 格式化输出
print(f"{s1} {s2}")
print("*" * 20)

# 计算字符串对象的长度 内置函数 len()
print(len(s1+s2))  # 容器类型都有长度
# 中文 占一个长度
s3 = 'i am 谭'
print(len(s3))

# 判断 in 针对容器类型 判断某个成员是否存在
print('am' in s3)  # True
```

## 2.17 输入输出函数

```python
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
```

## **2.18 字符串内置方法一**

```python
# 字符串内置方法
# 1.upper lower
s1 = 'Hello World'
print(type(s1))  # <class 'str'>
# 将字符串内所有的字符大写
print(s1.upper())  # HELLO WORLD
# 将字符串内所有的字符小写
print(s1.lower())  # hello world

# 2.startswith endswith
# 判断该字符串是否以什么内容开头 返回一个布尔值
print(s1.startswith('H'))  # True
# 判断该字符串是否以什么内容结尾 返回一个布尔值
print(s1.endswith('d'))  # True
```

## **2.19 字符串内置方法二**

```python
# 3.isdigit 判断一个字符串是否为一个纯数字字符串
# x = input('请输入一个数字：')
# if x.isdigit():
#     print(f'"{x}"是一个纯数字')
# else:
#     print(f'"{x}"不是一个纯数字')

# strip 去除字符串两端的空格或换行符
user = input('请输入用户名：')
# 变量的重新赋值
user = user.strip()
# 打印变量和变量的长度
print(user, len(user))
```

## **2.20 字符串内置方法三**

```python
# 4.split 字符串的分割 将字符串分割为列表
cities = '北京 哈尔滨 深圳 重庆'
ret = cities.split(' ')
print(ret, len(ret))  # ['北京', '哈尔滨', '深圳', '重庆']

# 5.join 字符串的拼接
ret2 = '、'.join(ret)
print(ret2)  # 北京、哈尔滨、深圳、重庆

# 6.find和index 查询子字符串的位置
# find找不到返回-1 index找不到会报错
print(cities.find('重庆'))  # 10
print(cities[10])  # 重

# print(cities.index('1'))  # ValueError: substring not found

# 7.count 计数
print(cities.count('重庆'))

# replace 替换
new_cities = cities.replace('重庆', 'cq')
print(new_cities)
```

## **2.21 运算符一**

```python
# 1.计算运算符
# + - * / % //

# 2.比较运算符
# > >= < <= == !=

# 3.赋值运算符
# = += -= *= /=
```

## 2.22 运算符二

```python
# 逻辑运算符
# and or not

# 成员运算符
# in not in
```

# 第3章 （新）Day3 - Python逻辑语句

## 3.1 双分支语句

```python
# 流程控制语句：顺序语句 分支语句 循环语句
# if-else语句
"""
双分支语句 要有缩进
if 表达式:
    语句
else:
    语句
"""
age = int(input('请输入你的年龄:'))
if age >= 18:
    print('已成年')
else:
    print('未成年')
print('程序结束')
```

## 3.2 多分支语句

```python
# 多分支语句:if-elif-else
# BMI计算
"""
if 表达式:
    语句
elif 表达式:
    语句
elif 表达式:
    语句
else:
    语句
"""
height = float(input('请输入你的身高[m]:'))
weight = float(input('请输入你的体重[kg]:'))

BMI = weight/height**2
print(f'你的BMI指数为{round(BMI, 2)}')
if BMI < 18.5:
    print('偏瘦')
elif 18.5 <= BMI < 24:
    print('正常')
elif 24 <= BMI < 28:
    print('超重')
else:
    print('肥胖')
```

## 3.3 分支嵌套语句

```python
# 分支嵌套
# 身份证号判断

pid = input('请输入你的身份证号:')

# 身份证号是否为18位
if len(pid) == 18:
    print('打印个人基本信息:')
    # 1.打印性别 身份证号倒数第二位如果是偶数 代表是女生 否则男生
    if int(pid[-2]) % 2 == 0:
        print('性别:女性')
    else:
        print('性别:男性')
    # 打印籍贯
    origin = pid[:3]
    if origin == '110':
        print('籍贯:北京市')
    elif origin == '120':
        print('籍贯:天津市')
    elif origin == '310':
        print('籍贯:上海市')
    elif origin == '500':
        print('籍贯:重庆市')
    else:
        print('不是直辖市!')

else:
    print('身份证位数有误!')
print('程序结束!')
```

## 3.4 循环语句之while循环

```python
# 循环:重复执行一段语句
"""
while循环的语法格式:
while 表达式:
    语句
"""

# 无限循环:死循环
# while True:
#     print('Hello world!')

# 有效次数循环
# 循环三要素:初始变量 条件判断 步进语句
count = 0
while count < 10:
    print(count)
    count += 1  # count自加1
```

## **3.5 循环语句之for循环**

```python
# for循环:遍历循环
"""
for 变量 in 容器:
    语句
"""

# for i in range(1, 100):
#     print(i)

# 步长默认为1
for i in range(1, 100, 2):
    print(i)
```

## **3.6 随机验证码案例**

```python
# 随机验证码案例
# 模块 import
import random  # 生成随机数模块
import string  # 字符串模块

# 在字符串中随机选择一个字符
# char = random.choice('0123456789')

# 生成26位小写字母: abcdefghijklmnopqrstuvwxyz
# print(string.ascii_lowercase)
# 生成26位大写字母: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_uppercase)
# 生成0-9数字:0123456789
# print(string.digits)

all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
# print(all_chars)


# 随机生成一个字符
def show_char():
    chars = ''
    for i in range(6):
        chars += random.choice(all_chars)
    print(chars)


for j in range(10):
    show_char()
```

## **3.7 累加和案例**

```python
# 案例1:从1+100案例
ret = 0
for i in range(1, 101):
    if i < 100:
        print(f'{i}+', end='')
    else:
        print(f'{i}', end='')
    ret += i
print(f'={ret}')

# 案例2:在循环中嵌套分支或循环
# 计算1-100的所有偶数和
```

## **3.8 循环语句之嵌套分支**

```python
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
```

## **3.9 退出循环之break**

```python
# 循环退出机制
# break continue 强制退出
# break:退出整个循环
# continue:退出当次循环
# print('break')
# for i in range(10):
#     if i == 6:
#         break
#     print(i, end='')
#
# print()
# print('continue')
# for i in range(10):
#     if i == 6:
#         continue
#     print(i, end='')

# 1.打印半径为1-100的圆的面积 pi * r ** 2
# 2.半径为1-100范围内找到第一个面积大于1000的半径值
import math
for r in range(1, 100):
    # 计算圆的面积
    area = math.pi * r ** 2
    if area > 1000:
        print(f'半径为{r}的圆的面积:{round(area, 2)}')
        break
```

## **3.10 continue退出循环**

```python
# continue 退出当前循环迭代
for i in range(10):
    if i == 6:
        # break
        continue
    # 0 1 2 3 4 5 7 8 9 
    print(i, end=' ')
```

## **3.11 游戏小案例**

```python
# 退出循环应用
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
```

# 第4章  （旧）Day1 - Python小白上路

## 4.1 为何Python能屌丝逆袭？

- 开发效率第一
- 学习曲线第一
- 生态圈第一
- 运行速度

## 4.2 Python在哪些领域大放异彩

1. web开发-Djnago框架
2. 网络编程
3. 爬虫
4. 云计算
5. 人工智能 数据分析
6. 自动化运维
7. 金融分析
8. 科学运算
9. 游戏开发

## 4.3 5分钟装好Python解释器

装python环境的原因：代码->python解释器->机器码

windows系统安装过程:官网下载(python3)->自定义安装(配置系统环境变量)->本地测试(cmd命令行)

```python
Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

## 4.4 写下你第一个Python程序

1. python交互器:仅供调试使用
2. 写在py文件中:可以永久保存 随时执行

向屏幕打印hello world

```python
print('hello world!')  # 符号应为英文半角状态下
```

## 4.5 cpu 内存 硬盘 三大硬件的作用与关系

**硬盘(只负责数据存储)->内存(只负责数据临时存储)->CPU(只负责计算)**

内存:解决硬盘与CPU运行速度不匹配的问题

## 4.6 变量来了

变量:用于在内存中存放程序数据的容器

变量名 变量值 内存地址

变量的定义规则:

1. 在程序全局都会用到的变量,尽量在文件开头定义变量
2. 变量名的第一个字符只能是字母或者下划线,且变量名只能由字母 下划线 和数字组成
3. python关键字不能作为变量使用

```python
# 变量名 = 变量值
# 先定义后调用
# print(name)  # NameError: name 'name' is not defined
name = 'hello'
print(name)  # hello
# 内存地址 id()
print(id(name))  # 2608946844400
```

## 4.7 变量名在命名规范

规则-强制要求

规范-建议要求

**常用的变量名定义规范**

1. 驼峰体
2. 下划线

**不建议变量名写法**

1. 用拼音 中文做变量名
2. 变量名过长
3. 不能见名知义
4. 首字母大写(特定情况西才会首字母大写,不能随意使用)

## 4.8 变量的修改与删除

```python
name = 'hello'
print(f'name = {name}')
# 修改变量
name = 'world'
print(f'name = {name}')

name2 = name
print(f'name2 = {name2}')
print(id(name))  # 2025006907088
print(id(name2))  # 2025006907088

name = '?'
print(f'name = {name}')
print(f'name2 = {name2}')
print(id(name2))
print(id(name))
```

## 4.9 数据类型初识-数字&字符串

**python数据类型:**

整数 浮点 字符串 布尔 列表 元组 字典 集合

```python
# 数字类型
# int(整型) integer
age = 18
# type()函数查看变量数据类型
print(type(age))  # <class 'int'>

# float(浮点型) 即小数
pi = 3.14
print(type(pi))  # <class 'float'>

# 字符串 在python中加了引号的都被认为是字符串!
city = '重庆'
print(type(city))  # <class 'str'>
```

## 4.10 数据类型初识-布尔&列表

```python
# 布尔数据类型
# True False
a = 3
b = 4
print(a > b)  # False
print(a < b)  # True
print(type(a > b))  # <class 'bool'>
print(type(a < b))  # <class 'bool'>

# 列表
names = ['Alex', 'Jack', 'Rain', 'WuSir', 'BlackGirl']
print(type(names))  # <class 'list'>
# 通过索引下标来取列表中的值 从左到右 从零开始
print(names[0])  # Alex

# 列表的修改
names[4] = '黑姑娘'
print(names)  # ['Alex', 'Jack', 'Rain', 'WuSir', '黑姑娘']

# 列表的插入
names.insert(4, '金角大王')
print(names)  # ['Alex', 'Jack', 'Rain', 'WuSir', '金角大王', '黑姑娘']

# 列表的追加
names.append('灰太狼')
print(names)  # ['Alex', 'Jack', 'Rain', 'WuSir', '金角大王', '黑姑娘', '灰太狼']

# 列表的删除
del names[4]
print(names)  # ['Alex', 'Jack', 'Rain', 'WuSir', '黑姑娘', '灰太狼']

# remove
names.remove('灰太狼')
print(names)  # ['Alex', 'Jack', 'Rain', 'WuSir', '黑姑娘']
```

## 4.11 常用运算符

1. 算术运算符
2. 比较运算符
3. 赋值运算符
4. 逻辑运算:and or not
5. 成员运算

## 4.12 安装配置全宇宙最好用的代码编辑器

**安装pycharm**:

- 创建项目
- 创建代码文件
- 执行代码
- 命令终端
- 代码调试
- 一些快捷键

## 4.13 读取用户指令

```python
# input
age = input('请输入你的年龄:')
print(f'你的年龄是{age}')
```

## 4.14 格式化输出-打印好看的个人信息卡

```python
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
job = input('请输入你的工作：')
hobby = input('请输入你的兴趣：')

print('-' * 10 + ' info of ' + name + ' ' + '-' * 10)
print(f'name\t:{name}\nage\t\t:{age}\njob\t\t:{job}\nhobby\t:{hobby}')
print('-' * 12 + ' ' + 'end' + ' ' + '-' * 12)
```

## 4.15 流程控制-if...else

**流程控制**

- 单分支
- 双分支
- 缩进
- 多分支

## 4.16 Python的代码缩进规范

**python原则**:

1. 顶级代码必须顶行写
2. 同一级别的代码必须缩进一致
3. 缩进最好为4个空格(官方建议)

## 4.17 流程控制-if..elif多分支

**多分支结构适用于多条件判断**

## 4.18 你的工资决定你的心态程序实现

```python
salary = int(input('Salary:'))

if salary > 100000:
    print('公司是我家')
elif salary > 50000:
    print('996像呼吸一样简单')
elif salary > 30000:
    print('老板说什么都是对的')
elif salary > 10000:
    print('老板说得对')
else:
    print('骂老板')
```

# 第5章  （旧）Day2 - 年会抽奖程序开发

## 5.1 for循环

1. 需指定循环次数
2. 相当于遍历了列表里每个元素
3. 循环猜年龄
4. 打印奇偶数
5. 打印各楼层房间号

```python
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
```

## 5.2 循环嵌套

```python
# 打印房间号
# 例:L2-202 第二层202房间
for i in range(1, 6):
    print(f'----------{i}层----------')
    for j in range(1, 9):
        print(f'L{i}-{i}0{j}室')
```

## 5.3 break&continue逃出鬼屋

```python
# 打印楼层的小程序:遇到第三层 不打印任何房间号 其他楼层都打印
# 到404房间后直接进入第五层
# 打印房间号
# 例:L2-202 第二层202房间
for i in range(1, 6):
    if i == 3:
        # continue:跳过当前循环
        # break:结束当前整个循环
        continue
    print(f'----------{i}层----------')
    for j in range(1, 9):
        print(f'L{i}-{i}0{j}室')
        if i == 4 and j == 4:
            print('遇到鬼屋404房间,over 了....')
            break
```

## 5.4 for循环打印三角形

```python
for i in range(1, 10):
    if i <= 5:
        print(i * '*')
    else:
        print((10 - i) * '*')
```

## 5.5 while 循环

- 死循环
- 循环指定次数
- while版猜年龄

```python
count = 0
# while True:  # dead loop
while count < 10:
    count += 1
    print(count)
```

## 5.6 京牌摇号小程序

```python
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
```

## 5.7 京牌摇号小程序代码实现
