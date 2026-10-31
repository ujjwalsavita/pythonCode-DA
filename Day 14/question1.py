# lis = [];
# n = int(input("Enter how many number you want to insert into the list"));

# for x in range(1,n+1):
#     num = int(input("Enter number"));
#     lis.append(num);

# print(lis);



lis = [2,2,5,7,8,2,2,7656,355,5,78,88,9,234,6,64,3,88,6,8,90,7765,976,88];
print(len(lis));
target = 8808;

# pos = lis.index(target)
# print(pos);


# for x in lis:
#     if(x == target):
#         print("yes!! we won the game");
#         break;
# else:
#     print("oopsss! we lost the game");

# for i in range(0,len(lis)):
#     if(lis[i] == target):
#         print("yes! we won the game , \ntarget is present at ", i+1);
#         break;
# else:
#     print("oopsss! we lost the game");


pos = -1;
for i in range(0,len(lis)):
    if(lis[i] == target):
        pos = i;


if pos == -1:
    print("target is not present");
else:
    print("yes! we won the game , \ntarget is present at ", pos + 1);
    



