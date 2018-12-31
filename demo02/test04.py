gl_num = 10
gl_list = [1, 2, 3]

def demo(num, num_list):
    print("函数内部代码")
    num = 100
    print(num)  # 100
    # num_list = [4, 5, 6]
    # print(num_list)  # [4, 5, 6]

    num_list.append(4)
    print(num_list)  # [1, 2, 3, 4]  列表是可变的
    print("函数执行完成")


demo(gl_num, gl_list)
print(gl_num, gl_list)   # 10 [1, 2, 3]  如果使用了apend以后，列表值会变化：10 [1, 2, 3, 4]


print("-"*100)
g_num = 50
g_list = [1, 2, 3]
def demo1(num, list):
    print("函数开始")
    # += 运算： num = num + num 
    num += num
    print(num)  # num: 100

    # 列表变量使用+= 不会做相加再赋值的操作，本质上在调用extend()方法
    # list += list  # 等同于list.extend(list)
    # print(list)  # [1, 2, 3, 1, 2, 3]

    # 列表如果写为这样，就是相当于重新创建一个变量
    list = list + list
    print(list)  # [1, 2, 3, 1, 2, 3] 但是全局的g_list: [1, 2, 3]
    print("函数执行完成")


demo1(g_num, g_list)
print(g_num)  # g_num: 50
print(g_list)  # [1, 2, 3, 1, 2, 3]