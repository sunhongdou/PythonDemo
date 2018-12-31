def measure():
    temp = 39
    wetness = 10
    # 元组-可以包含多个数据，可以使用元组使函数一次返回多个数值,即使用元组进行封装，如果返回的是元组，小括号是可以省略的。
    #return (temp, wetness)
    return temp, wetness


# result的类型：元组
result = measure()  # 单个接收器，实用元组中的数据，还要再拆箱一次。还需要知道元组的下标，使用不便。
print(result)

# 需要单独处理温度和湿度，不推荐
print(result[0], result[0])

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素，可以使用多个变量，一次接收函数的返回结果
# 使用多个变量接收时，变量的个数和返回值的个数要一致。
gl_temp, gl_wetnese = measure()   # 元组多返回值，对应多个接收器
print(gl_temp, gl_wetnese)