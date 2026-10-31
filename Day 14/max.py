lis = [3,35,3,564,65,7,64,8,564,59,5,3,6,2,4,5];


# max = -1
# for x in lis:
#     if x > max:
#         max = x;
# else:
#     print("Max element in the list is ", max);

# pos = [];
# for i in range(0, len(lis)):
#     if max == lis[i]:
#         pos.append(i+1);
# print("Maximum value is present at ",pos);



#***********************SECOND MAXIMUM *******************

# for i in range(0, len(lis)):
#     if max == lis[i]:
#         lis[i] =0;

# max = -1
# for x in lis:
#     if x > max:
#         max = x;
# else:
#     print("Max element in the list is ", max);



# lis.sort();
# print(lis);

# st = set(lis);
# ans = list(st);
# ans.sort();
# print(ans[-2]);


print(lis);

first = -1;
second = -1;
for x in lis:
    if x > first:
        second = first;
        first =  x;
    elif x > second and x != first:
        second = x;


print(second);