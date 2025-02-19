# 定义:逗号分隔 按照索引 存放各种数据类型 每个位置代表一个元素
a = []
print(type(a))  # <class 'list'>

# 增加 append 追加 insert 插入 extend 合并
# 列表的嵌套
a = [1, 2, [3, 4, 5], 6]
print(a)  # [1, 2, [3, 4, 5], 6]
print(a[2][1])  # 4

# 删除 del 直接删除 pop 删除(默认删除最后一个元素 并返回删除值)
print(a.pop())  # 6
print(a.pop())  # [3, 4, 5]

# remove 指定元素名删除 只会删除找到的第一个值

# 修改

# 查找 index 查找索引 count 返回个数 in 判断
# 先判断 取索引 去修改
