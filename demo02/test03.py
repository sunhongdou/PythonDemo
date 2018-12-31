# 交换数据
a = 1
b = 2

# 方法一：
# c = a
# a = b
# b = c
# print(a, b)

# 方法二：
# a = a + b
# b = a - b
# a = a - b
# print(a, b)

# 方法三：
a, b = b, a   # 右侧为元组,多个变量返回，可以省略括号  a, b =（b, a）
print(a, b)