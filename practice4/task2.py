class MyClass:
    def __init__(self, param1, param2, param3):
        """Constructor"""
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def print_attrs(self, num):
        print(self.__dict__['param' + num.__str__()])


myClass = MyClass(1, 117, 'S')
print(myClass.__dict__)
eval("myClass." + input())
