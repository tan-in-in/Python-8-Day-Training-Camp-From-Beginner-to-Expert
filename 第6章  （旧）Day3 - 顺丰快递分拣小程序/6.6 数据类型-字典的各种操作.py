dic = {'Alex': [23, 'CEO', 66000], '黑菇凉': [24, '行政', 4000], '佩奇': [26, '讲师', 4000]}
# 增加
print(dic)

# 修改
dic['佩奇'] = 25
print(dic)

# 删除 clear() 清空
# dic.pop('佩奇')
# print(dic)

# 查找 通过key差value
print(dic['Alex'])
print(dic.keys())
print(dic.values())
print(dic.items())

for i, j in dic.items():
    print(i, j)

# 推荐用这种 功率速度最快
for i in dic:
    print(i, dic[i])

print(len(dic))  # 3
