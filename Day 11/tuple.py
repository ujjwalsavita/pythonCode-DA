tup1 = (12,)

print(type(tup1));
print(type(tup1[0]));

tup2 = 2,3,4,6,7,8,9,9,9
print(type(tup2));

tup3 = (2)
print(type(tup3));

a = b = c = 2,3,4,5,5
print(type(a));
print(type(b));
print(type(c));

print(a is b);
print(c is b);
print(c is a);


d = e,f,g,h = 2,3,4,5
# print(a);
print(e);
print(f);
print(g);
print(h);

print(d);
print(type(d));


i= j, *k = 4,6,7,8,9,90,9

print(j);
print(k);

tup4 = (2,4,6,7,8,8,32,7,8,89,5,3,2,6,6,8,8);
print(tup4[8])

# for x in tup4:
#     print(x, end=" ");

# for i in range(0, len(tup4)):
#     print(tup4[i], end=' ');

# print(tup4)

# i = 0;

# while True:
#     if i >= len(tup4):
#         break;

#     print(tup4[i], end=' ');
#     i = i+ 1;

# print(tup4[::-1])
# print(tup4[::3])

# tup4[0]= 20
# print(tup4);


# tup5= ("Coding seekho", 1,"5.7");
# print(tup5);

# print(tup4.count(5));
# print(tup4.index(5));
# tup4.reverse();
# tup4.sort();
# print(tup4);


# tup6 = tup4;
# print(tup4 is tup6)
# tup6 = tup4.copy()
# print(tup4 is tup6)

import copy

tup6 = copy.deepcopy(tup4);
print(tup4 is tup6)
