#! /usr/bin/python
import cards_tools
# # 欢迎界面
# print("*****************************************************************************")
# print("1.新建名片\n2.显示名片 \n3.查询名片\n\n0.退出系统")
# print("*****************************************************************************")

while True:
    # 显示功能菜单
    cards_tools.show_menu()
    # TODO(小明/xiaoming@163.com) 提示用户输入
    action_str = input("请选择你希望执行的操作： ")
    print("你选择的操作是： 【%s】" % action_str)

    # 0 退出，1，2,3 针对名片的操作，否则的话输入非法
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_card()
        # 查询名片
        # pass 表示一个占位符，能够保证程序结构正确
        # pass
    # 0： 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系】")
        break
    # 其他输入，输入错误
    else:
        print("你输入的不正确，请重新输入")
