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
