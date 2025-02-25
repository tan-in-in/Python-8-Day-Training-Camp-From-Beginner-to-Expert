f = open('7.14 stock_data.txt', 'r', encoding='utf-8')
data = f.readlines()
# 1. 程序启动后，给⽤户提供查询接⼝，允许⽤户查股票⾏情信息(⽤到循环)
# for i in data[1:]:
#     print(i, end='')

# 2. 允许⽤户通过模糊查询股票名，⽐如输⼊“啤酒”, 就把所有股票名称中包含“啤酒”的信息打印出来
name = input('请输入公司包含的汉字:')
count = 0
for i in data[1:]:
    if name in i.split(',')[1]:
        print(i, end='')
        count += 1
print(f'已为你找到{count}家包含"{name}"的公司')

# 3. 允许按股票价格、涨跌幅、换⼿率这⼏列来筛选信息，⽐如输⼊“价格>50”则把价格⼤于50的股票都打印，输⼊“市盈率<50“，则把市盈率⼩于50的股票都打印，不⽤判断等于。
f.close()
