# 面向对象的编程思想，先定义个类
class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建对象，可以使用同一个类，创建出不同的对象
tom = Cat()
tom.drink()
tom.eat()
print("-"*50)

# 再创建一个对象,即两个引用，两个内存地址不同
lazy_tom = Cat()
lazy_tom.eat()
lazy_tom.drink()

print(tom)  # <__main__.Cat object at 0x0162FEB0>
# 打印地址
addr = id(tom)
print("%x" % addr)  # %x 十六进制  162feb0
