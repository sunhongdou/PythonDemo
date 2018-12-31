# 字典定义,字典是一种无序的数据集合
xiaoming = {"name": "xiaoming",
            "age": 18,
            "gender": "boy",
            "height": 1.87}

# 从字典中取值,如果键不存在，则报错
print(xiaoming["name"])

# 增加字典中数值,键不存在就是新增，键存在就是修改
xiaoming["tel"] = 12124

# 修改字典值
xiaoming["name"] = "xiaoxiaoming"

# 删除键,如果键不存在就是报错
#xiaoming.pop("age")

# 统计字典中的键值对数量
print(len(xiaoming))

# 合并字典
temp_dir = {"addr": "hebei", "age": 13}
# 如果合并的字典中包含已经存在的键值对时，会覆盖原有的键值对
xiaoming.update(temp_dir)

# 清空字典
#xiaoming.clear()

# 遍历字典,每次遍历出来的key就是键
for k in xiaoming:
    print("%s-%s" % (k, xiaoming[k]))  # name-xiaoxiaoming  age-13 ...
print(xiaoming)
print("----------------------------------------------------------------------------")
# list & map
card_list = [
    {"name": "zhangsan",
     "qq": 25435345,
     "tel": 4534523},
    {"name": "lisi",
     "qq": 97897,
     "tel": 40987523},
]

for card_info in card_list:
    print(card_info)



