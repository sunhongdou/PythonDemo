def test(num):
    print("在函数内部，内存地址： %d" % id(num))
    # 1.定义一个字符串变量
    result = "hello"
    print("hello 的内存地址： %d" % id(result))   # hello 的内存地址： 4388320
    # 2.将字符串变量返回,返回的是数据的引用，而不是数据本身。
    return result


# 定义变量，并打印内存地址
a = 10
print("a 变量的内存地址为：%d" % id(a))   # a 变量的内存地址为：1500760336
# 调用test()函数,调用函数式，本质是传地址，引用传递。
r = test(a)
print("r的内存地址： %d" % id(r))  # r的内存地址： 4388320

