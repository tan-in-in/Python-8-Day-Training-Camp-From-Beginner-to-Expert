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

