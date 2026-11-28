class Hello:
    def __init__(self,n):
        self.__name = n

    def getAttr(self):
        print(self.__name);

    def setAttr(self, new):
        self.__name = new;


s1= Hello("Coding seekho");
s1.getAttr();

# s1.name = "coding seekho inst."

s1.getAttr();
s1.getAttr();

s1.setAttr("coding SEEKHO");
s1.getAttr();


print(s1.name);
