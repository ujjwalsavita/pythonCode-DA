lis = [453,66,57,6,86,87,9,79,89,0,9];

rotate = 19999

rotate = rotate % len(lis);
print(rotate);


for r in range(0, rotate):
    val  = lis[0];
    for i in range(1, len(lis)):
        lis[i-1] = lis[i];

    lis[len(lis) - 1] = val;


print(lis);