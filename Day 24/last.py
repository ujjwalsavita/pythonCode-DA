class Hello:
    def __init__(self, name):
        self.name = name;

    def sayHello(self):
        print(f'hello {self.name} sir, Good morning');

    @classmethod
    def SayHello(cls):
        print(f'i am a class method')

    @staticmethod
    def Saygood():
        print("good morning bhaiya ji");


# h = Hello();
# h1 = Hello("Coding seekho");
# h1.Saygood()
# Hello.Saygood();
# h1.Saygood();

# Hello.SayHello()
# h1.sayHello()



class GoodMoring:
    def __init__(self,name, nam):
        self.__name = name;
        self.__nam = nam;
    
    @property
    def hello(self):
        print(self.__name);
        print(self.__nam)

    
    def setAttr(self, newName, newPrivateName):
        self.__nam = newPrivateName
        self.__name = newName

    @property
    def name(self):
        return self.__name;

    @name.setter
    def name(self, n):
        self.__name = n;

    


# gd = GoodMoring("Coding seekho", "Jinda baad");
# print(gd.__nam);
# gd.hello();
# gd.hello # method is call like the attributes, due to the @property
# gd.setAttr("CoDing Seekho","Amar rahe")
# gd.hello

# gd.name = "CODING SEEKHO"
# gd.hello

# def announce(func):
#     def wrapper():
#         print("Before the function runs...")
#         func()
#         print("After the function runs...")
#     return wrapper

# @announce
# def say_hello():
#     print("Hello!")

# say_hello()



def announce(func):
    def wrapper():
        print("Before the function runs...")
        func()
        print("After the function runs...")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = announce(say_hello)

say_hello()
