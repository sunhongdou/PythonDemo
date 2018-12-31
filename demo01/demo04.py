# 方法定义
# def say_hello():
#     print("hello")
#     print("hello")
#     print("hello")


# say_hello()


# def sum_2_num():
#     num1 = 10
#     num2 = 20
#     sum = num1 + num2
#     print("%d + %d = %d" % (num1, num2, sum))


# sum_2_num()

# 函数传参
# def sum_2_num(num1, num2):
#     result = num1 + num2
#     print("%d + %d = %d" % (num1, num2, result))
#
#
# sum_2_num(20, 30)

# i = 0
# sum = 0
# while i < 5:
#     sum += i
#     i += 1
# print(sum)

# def sum(num1, num2):
#     return num1 + num2
#
#
# result = sum(1, 2)
# print(result)

# def test():
#     print("*" * 10)
#
#
# def test2():
#     print("-" * 10)
#     test()
#     print("-" * 10)
#
#
# test2()

def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    """
    打印多行分割线
    :param char: 分割线使用的分隔符
    :param times: 分隔符次数
    """
    i = 0
    while i < 5:
        """"打印多行分割线"""
        print_line(char, times)
        i += 1


print_lines("-", 50)




