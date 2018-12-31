# 字符串定义
str1 = "hello python"
# 定义字符串，里面有双引号时，外部用单引号
str2 = '我的外号"时大西瓜"'
print(str2)

# 取出字符串中的指定位置的字符
print(str1[6])
for char in str1:
    print(char)

print("=============================================================================")
hello_str = "hellollollo"
#获取字符串长度
print(len("hello wold"))

# 获取指定元素出现的位置,如果子字符串不存在，会报错
print(hello_str.index("llo"))
# 统计字符出现的次数
print(hello_str.count("llo"))

# 判断是否包含空格,其中换行，Tab键都是空白字符
space_str = "   \t\n\r"
print(space_str.isspace())   # True

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# 判断一个字符串是否只包含数字
# 1.这三种方法都不能判断小数
# 2.对于unicode字符串isdecimal() 会返回false,如num_str = "\u00b2"
# 3.中文数字 isnmueric返回true,其他两个返回false，如 num_str = "一千零一"
num_str = "一千零一"
print(num_str.isdigit(),num_str.isdecimal(),num_str.isnumeric())

print("-------------------------------------------------------------------------")
test_str = "hello world"
#字符串以什么开头
print(test_str.startswith("hello"))

#字符串以什么结尾
print(test_str.endswith("world"))

# 字符串查找和替换,打印出字符串的下标索引，等同于index()
print(test_str.find("llo"))
print(test_str.find("abc"))   # 查找的字符串不存在会返回-1，而index()不存在会报错

# 替换字符串
print(test_str.replace("world", "python"))  # 替换完成后会返回一个新的字符串，不会修改原有的字符串
print(test_str)   # 替换后还是原来的字符串，hello world

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# 文本对齐处理
poem = [
    "登鹳雀楼",
    "王之涣",
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"
]
for poem_str in poem:
   # print("|%s|" % poem_str.center(10), " ")  # 居中打印
   # print("|%s|" % poem_str.ljust(10), " ")   # 相左对齐  向右对其rjust()
   print("|%s|" % poem_str.strip().center(10, " "))

net_str = "登鹳雀楼\t 王之涣\t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t \n 更上一层楼"
print(net_str)

# 拆分字符串
net_list = net_str.split()
print(net_list)

# 合并字符串
result = " ".join(net_list)
print(result)

num1_str = "0123456789"
print(num1_str[2:])
print(num1_str[:5])
print(num1_str[:])
print(num1_str[::2])
print(num1_str[1::2])
print(num1_str[-2:])
print(num1_str[2:-1:2])
print(num1_str[::-1])  # 倒序输出

int_num = [1, 2, 5, 8, 4]
print(max(int_num))
print(min(int_num))

str_test = ["a", "c", "d", "z"]
print(max(str_test))

print(["a", "a", "a" ] < ["b", "b", "b"])
print(max({"a": "z", "b": "y", "c": "x"}))  # map中只能对key进行比较大小，无法对值进行比较

print([1, 2, 3, 4, 5][1:2])
print((1, 2, 3, 4, 5)[1:2])

print([1, 2]*5)  # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print((1, 2)*5)

# 字符串拼接
print("hello" + " python")  # hello python
# 列表的拼接
print([1, 2] + [3, 4])  # [1, 2, 3, 4]  生成一个新的列表

# 列表的拼接
t_list = [1, 2]
t_list.extend([3, 4])
print(t_list)   # [1, 2, 3, 4]

t_list.append(0)
t_list.append([8, 9])  # [1, 2, 3, 4, 0, [8, 9]]
print(t_list)

# 包含
print("a" in "abc")   # True
print(2 not in [1, 2, 3])  # False
print("a" in {"a": "c"})

for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # 如果没有break 退出循环，循环结束后，会执行代码。
    print("会执行吗？")   # for 有了break就不会执行，没有break就会执行
print("循环结束")

print("--------------------------------------------------------------------------")
# 在学员列表中搜索指定的名字
student = [
    {"name": "tom",
     "age": 20,
     "gender": True},
    {"name": "tony",
     "age": 25,
     "gender": True}
]

# find_name = "tomn"
# for stu_dict in student:
#     print(stu_dict)
#     if stu_dict["name"] == find_name:
#         print("找到了%s" % find_name)
#         # 如果已经找到，就退出循环
#         break
# else:
#     # 如果希望搜索列表时，所有的字典检查完之后，都没有找到需要搜索的目录，还需要得到一个统一的提示
#     print("抱歉，没有找到")
# print("循环结束")

# 写法二：
find_name = "tomn"
for stu_dict in student:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了%s" % find_name)
        # 如果已经找到，就退出循环
        break
    else:
        print("抱歉，没有找到")  # 如果单纯的写为if else 则else语句会被执行两遍，并没有得到一个统一的提示。
print("循环结束")