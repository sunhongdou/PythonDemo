# 定义列表,列表中也可以存储不同类型的数据，但是很少用到。
name_list = ["zhangsan", "lisi", "wangwu", "zhaoliu"]

# 循环遍历列表  for in
for my_name in name_list:
    print("我的名字叫 %s" % my_name)

# 定义元祖，可以存储不同类型的数据
info_tuple = ("zhangsan", 18, 1.78)

# 定义空元祖
empty_tuple = ()

# 打印类型
print(type(info_tuple))

# 定义单个元祖，需要在数据后面加一个逗号，否则Python中的解释器会认为是内容的类型。
single_tuple = (5,)
print(type(single_tuple))

# 打印元祖中的元素
print(info_tuple[0])

# 元祖中取值
print(info_tuple[0])

# 索引
print(info_tuple.index("zhangsan"))

# 统计元素出现的次数
print(info_tuple.count("zhangsan"))

# 统计元祖的长度
print(len(info_tuple))

# 遍历元祖
for my_info in info_tuple:
    print(my_info)

# 格式化打印的本质用的就是元祖
print("%s 的年龄是 %d 身高是 %.2f" % ("xiaoming", 12, 1.78))

xiao_ming = ("xiaoming", 12, 1.78)
print("%s 的年龄是 %d 身高是 %.2f" % xiao_ming )

# 使列表中的数据不被修改，可以使用tuple()
num_list = [1, 2, 4, 6]
print(type(tuple(num_list)))   # list  --> tuple

num_tuple = (1, 2, 3, 4)
print(type(list(num_tuple)))   # tuple --> list




