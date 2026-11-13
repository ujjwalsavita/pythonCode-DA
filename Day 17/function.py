def helloBoloBhaiyaKo(name):
    print("hello Bhaiya",name);

helloBoloBhaiyaKo("lala ji");



def add(x, y):
    return x+y;

sum = add(2,3);
print(sum);

def calculator(x,y,op):
    if op == '+':
        return x+y;

    elif op == '-':
        return x-y;

    elif op == '*':
        return x*y;
    elif op == '/':
        return x // y;



print(calculator(55,76,'+'));
print(calculator(55,76,'-'));
print(calculator(55,76,'*'));
print(calculator(55,76,'/'));

def greet(name="guest ji"):
    print('hello {}'.format(name))

greet("pushpa ji")
greet()





# lis = [2,3,4,5,'t','y6',7,8,9,90];

# for idx, val in enumerate(lis):
#     print(idx, val);

# for val in lis:
#     print(val);

# for idx in range(0, len(lis)):
#     print(lis[idx])
