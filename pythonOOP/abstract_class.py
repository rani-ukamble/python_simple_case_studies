# 

class Demo:
    def show(self):
        print("Hello  demo")

class Child(Demo):
    def show(self):
        print("Hello child")

c1 = Child
print(c1)
# c1.show()

# d1 = Demo()
# d1.show()
