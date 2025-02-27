name = 'tan'


def change_name():
    # global 函数中使用全部变量
    global name
    name = 'jin'
    print(name)  # jin


change_name()
print(name)  # tan
