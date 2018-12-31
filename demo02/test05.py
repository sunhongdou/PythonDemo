gl_list = [6, 3, 9]
# 默认排序是升序
# gl_list.sort()
# print(gl_list)  # [3, 6, 9]

# 降序排列  reverse=True
gl_list.sort(reverse=True)
print(gl_list)  # [9, 6, 3]

print("="*100)


# 缺省值： 在参数中设置 gender=True
# 注意：缺省值参数必须是最后一个参数，多个缺省参数时，需要明确指定参数名称
def print_info(name, title="班级信息", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s]： %s 是 %s" % (title, name, gender_text))


# 缺省值 True
print_info("小米")
print_info("张三", gender=False)  # 多个缺省值，在使用时要明确指定缺省的参数名：  gender=False
print("-"*50)


# 多值参数，一个*表示元组，两个*表示字典
def demo2(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


# demo2(1)
demo2(1, 2, 3, 4, 5, name="xm", age=12)
print("*"*50)


# 多值参数，可变参数，使用单个*表示元组
def sum_numbers(*args):
    num = 0
    print(args)
    for n in args:
        num += n
    return num


result = sum_numbers(1, 2, 3)
print(result)
print("-"*50)


# 拆包语法，简化元组变量/字典变量的传递
def demo3(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)
gl_dict = {"name": "zhangsan", "age": 18}
demo3(*gl_nums, **gl_dict)  # 等同于下面的写法
demo3(1, 2, 3, name="xiaoming", age=18)
print("="*50)


def sum(num):
    # 递归结束条件
    if num == 1:
         return 1
    # 数字的累加
    temp = sum(num - 1)
    return temp + num


res = sum(100)
print(res)

