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
