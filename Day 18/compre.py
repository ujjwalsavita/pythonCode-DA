lis = [884,4,5,6,7,8,8,8,8,8,8,8,7,5,2,2,2,2,1,1,2,3,567,8,9,9,0,-1];
# print(len(lis));

# res = [x+2 for x in lis];
# set = {x for x in lis};
# dic = {x : x+2 for x in lis};
# print(len(res));
# print(res);
# print(set);
# print(dic);


res = [x for x in lis if x%2 == 1];
# print(res);


#  method 1
res = []

# for x in lis :
#     if x % 2 == 0:
#         res.append(x ** 2);
#     else:
#         res.append(x ** 3);

# print(res); 

# method 2 ::
# def func(x):
#     if x % 2 == 0:
#         return x ** 2;
#     else :
#         return x ** 3;

# res = map(func, lis);
# res = list(res);
# print(res); 



# method 3 ::

res = [x**2 if x%2==0 else x**3 for x in lis];
print(res);

newRes = [x*2 if x>0 else x*3 if x<0 else x+2 for x in lis];
print(newRes);




