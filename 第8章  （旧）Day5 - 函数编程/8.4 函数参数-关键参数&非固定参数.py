# 关键参数(指定参数)
# 关键参数必须放在位置参数之后

# 非固定参数 *args 会把传入的参数变成一个元组形式
# **kwargs(字典)
def stu_info(name, age, *args, **kwargs):
    print(name, age, args)
    print(type(args))  # <class 'tuple'>


stu_info('tan', 20, 'boy', 'stu', 'c')

