def fun(x, y,q="or bhai", z="han ji"):
    print(x)
    print(y)
    print(z)
    print(q)

# fun("good morning",y="hello",z="Push ji",q='samoseeeeeee');


# def fun1(x, lis=[]):
#     lis.append(x);
#     print(lis);
def fun1(x):
    lis=[]
    lis.append(x);
    print(lis);

# fun1(1);
# fun1(2);
# fun1(3);



def fun2(*x):
    print(type(x));


# fun2(2,3,7,8,9,6,5,6,43,4,6,7,78,8,8,9,9,99,7,5,4,4,5);

def fun3(**p):
    print(type(p));

fun3(x=1,z=9,y=8,q=9);

