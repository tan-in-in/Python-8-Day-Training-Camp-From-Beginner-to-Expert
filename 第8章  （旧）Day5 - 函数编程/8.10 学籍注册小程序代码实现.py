# 1. 要求⽤户输⼊姓名、年龄、⼿机号、身份证号、所选课程，然后为学员完成注册
# 2. ⼿机号、身份证号唯⼀
# 3. 可选的课程只能从Python、Linux、⽹络安全、前端、数据分析 这⼏⻔⾥选
# 4. 学员信息存⼊⽂件

# 1.数据存到文件里的格式 姓名,年龄,手机,身份证,学科
# 2.手机号,身份证号的唯一
db_file = 'student_data.txt'


def register_api():
    stu_data = {}  # 初始化一个空字典
    print('欢迎进入注册'.center(50, '-'))
    print('请完成学籍注册:')
    name = input('姓名:').strip()
    age = input('年龄:').strip()
    phone = input('手机号:').strip()
    id_num = input('身份证号:').strip()

    course_list = ['python', 'java', 'kotlin']
    for index, course in enumerate(course_list):
        print(f'{index+1}. {course}')

    selected_course = input('选择想学的课程:')
    if selected_course.isdigit():
        if 1 <= int(selected_course) <= len(course_list):
            picked_course = course_list[int(selected_course) - 1]
        else:
            exit('不合法的选项...')
    else:
        exit('非法输入...')
    stu_data['姓名'] = name
    stu_data['年龄'] = age
    stu_data['电话号'] = phone
    stu_data['身份证号'] = id_num
    stu_data['课程'] = picked_course
    return stu_data


def commit_to_db(filename, stu_data):
    # 把学员数据存到文件中
    f = open(filename, 'a', encoding='utf-8')
    row = f"{stu_data['姓名']}, {stu_data['年龄']}, {stu_data['电话号']}, {stu_data['身份证号']}, {stu_data['课程']}\n"
    f.write(row)
    f.close()


stu_data = register_api()
print(stu_data)
commit_to_db(db_file, stu_data)
