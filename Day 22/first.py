# class Abc:
#     def __init__(self):
#         print(self);
#         print("good morning");
    

# obj1 = Abc();
# obj2 = Abc();

# print(obj1);
# print(obj2);


class Abc2:
    name = "CoDing Seekho"
    def __init__(self, n):
        self.name = n;
        print(self.name);
        # print(name);
        print(Abc2.name);
        print(Abc2);

    def func(self):
        print("bhai chai piyo, ha bhai, thik bhai bana liiye");


obj1 = Abc2("Pushpa Raj");
obj1.func();

# print("*****************")

# Abc2.name = "Coding Seekho";
# obj2 = Abc2("Dost");


# print("#"*10)
# print(obj1.name);
# print(obj2.name);