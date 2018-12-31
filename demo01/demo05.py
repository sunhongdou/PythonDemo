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


name = "zhangsan"