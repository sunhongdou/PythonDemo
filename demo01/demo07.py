# 列表的定义
name_list = ["zhangsan", "lisi", "wangwu", "zhangsan"]

# 取出列表数据,如果下标越界，就会报错 index out of range
print(name_list[0])

# 获取列表下标
print(name_list.index("zhangsan"))

# 修改列表元素值
name_list[1] = "zhaosi"
print(name_list[1])

# 追加数据
name_list.append("wangxiaoer")

# 在指定索引位置添加数据
name_list.insert(1, "xiaomei")

# 扩展列表
temp_list = ["sunwukong", "zhubajie", "shashidi"]
name_list.extend(temp_list)

# # 删除列表,如果删除的数据不存在，则报错，如果存在同名的字段，只会删除第一个元素。
# name_list.remove("wangwu")
#
# # 弹出元素,默认弹出最后一个元素
# name_list.pop()
# name_list.pop(3)   # 指定索引的元素弹出
#
# # 清空所有列表内容
# name_list.clear()

# 删除元素，将一个变量从内存中删除
# del name_list[1]

name = "账务"
del name
#print(name)  # del已经将变量从内存中删除，故这里打印报错，not defined.

# 获取列表长度
list_len = len(name_list)
print(list_len)

# 统计列表中出现次数
count = name_list.count("zhangsan")
print(count)

# 升序
name_list.sort()

# 降序
num_list = [1, 3, 2, 10, 5, 8, 4]
num_list.sort(reverse=True)
print(num_list)

# 反转
name_list.reverse()
num_list.reverse()
print(num_list)

print(name_list)
