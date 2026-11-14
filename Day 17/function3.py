def square(x):
    return x**2;
print(square(5));



square2 = lambda x: x**2;
print(square2(6));






def fun2(x):
    print(x(4));


# fun2(square())
fun2(square)



def fun3():
    def hello():
        print("hello ji or batao kya haal chal hai");

    return hello;

helloooo = fun3();

helloooo();


lis = [2,3,4,5,6,78,89,9,990,87];
res = []
# def sq(x):
#     return x**2;

# for y in lis:
#     res.append(sq(y));

# z = map(sq, lis);



z = map(lambda x :x**2, lis);

print(res);
print(list(z));


lis2= ['10','20','30']

w = map(int, lis2)
print(list(w));


lis3 = [435,5,5,6,67,7,7,8,88,89,9,9,990,0,0,0,6];

v = filter(lambda x : x % 2 == 0, lis3);
print(v)
print(list(v))

from functools import reduce
b = reduce(lambda a,b: a+b, lis3,10);
print(b);
