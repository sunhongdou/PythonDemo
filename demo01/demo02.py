"""
个人信息：
姓名：张三
性别：男
年龄：20
身高：1.70
"""
# Python会根据右侧的值自动推导出变量的类型
name = "张三"   # 类型：字符串 str
sex = '男'
age = 20    # 类型：int
height = 1.70   #类型：浮点型 float

# 查看数据类型
print(type(age))

# int & long  python3.0 整合了所有的long，打印出来都是int
print(type(2 ** 32))   # int
print(type(2 ** 64))   # int

# 不同类型之间的运算
print(2.1+1)
print(2.1-True)   # TRUE = 1
print(2+True)

firstName = "Jone"
lastName = "Tony"
print(firstName+lastName)  # JoneTony  字符串拼接，整型和字符串是无法拼接的。

print(firstName*3)

# 键盘输入 input()
input("请输入数字：")

num = input("please intput num:")
print(num)

# 类型转换
print(type(int("123")))





