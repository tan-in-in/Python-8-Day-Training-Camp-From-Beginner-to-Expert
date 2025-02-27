d = {
    'name': 'tan',
    'age': 25,
    'hobbie': 'run'
}
l = ['a', 'b', 'c']
print(id(d))
print(id(l))


def change_data(info, girls):
    print(id(info))
    print(id(girls))
    info['hobbie'] = '学习'
    girls.append('d')


change_data(d, l)
# {'name': 'tan', 'age': 25, 'hobbie': '学习'} ['a', 'b', 'c', 'd']
print(d, l)
