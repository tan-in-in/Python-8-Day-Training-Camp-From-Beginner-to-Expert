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
