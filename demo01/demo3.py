# # input输入的类型为string
# price = float(input("苹果的价格："))
# weight = float(input("苹果的重量："))
# # float()进行类型转换   string --> float
# money = price * weight
# #格式化输出
# print("价格为：%.02f" % money)
# print("单价：%.02f, 重量：%.02f" % (price,weight))

# 输出Python中关键字
# import keyword
# print(keyword.kwlist)
"""
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 
'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
"""

# 分支判断
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("你已经成年...")  # if内的body体，条件成立，则执行此代码块
#
#     print("已成年，这里也会执行...")   # if内的body体
# print("未成年人！")  # if条件不成立，继续详细额执行的代码

# age = 12
# if age >= 18:
#     print("成年人")
# else:
#     print("未成年人")
# print("if-else执行完毕！")

# age = 45
# if age >= 120 or age <= 0:
#     print("年龄超限")
# else:
#     print("合法的年龄段")

# age = 32
# if age >= 0 and age <= 120:
#     print("年龄正确")
# else:
#     print("年龄不正确")

# python_score = 50
# java_score = 50
# if python_score > 60 or java_score > 60:
#     print("考试通过")
# else:
#     print("考试失败")

# is_employee = True
# if not is_employee:
#     print("非本公司成员，禁止入内")
# else:
#     print("随便进...")

# holiday_name = 4
# if holiday_name == 1:
#     print("看电影")
# elif holiday_name == 2:
#     print("买苹果")
# else:
#     print("每天都是节日")

# has_ticket = True
# knife_length = 30
#
# if has_ticket:
#     print("车票检查通过")
#     if knife_length >= 30:
#         print("行李不能通过！")
#     else:
#         print("可以通过")
#
# else:
#     print("无票，不能通过！")

# 打印9行小星星，def表示定义函数
def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            col += 1
        print("")
        row += 1


#continue用法演练
j = 0
while j < 10:
    if j == 3:
        j += 1
        continue
    print(j)
    j += 1


