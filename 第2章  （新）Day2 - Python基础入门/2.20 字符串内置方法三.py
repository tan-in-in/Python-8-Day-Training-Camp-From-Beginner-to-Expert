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
