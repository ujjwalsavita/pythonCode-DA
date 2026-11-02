# st = 'Coding seekho';
# # st1 = 'Coding seekho';
# # st2 = 'Coding seekho';

# print(id(st))
# # print(id(st1))
# # print(id(st2))

# st1 = "CoDing Seekho";
# print(id(st1))

# st2 = '''CoDing seekho''';
# print(id(st2))

# st3 = '''hello haa voice aar rahi, "Hello bhai,it's me gate kholo bhai"''';
# print(st3);
# print(type(st3));

# st4 = "hello"
# print(id(st4))
# print(st4);
# print(type(st4));

# st4 = 'Hello';
# print(id(st4))
# print(st4);

# print(st4[0]);
# print(st4[1]);
# print(st4[2]);
# print(st4[::-1]);
# print(st4[0:2]);

# for x in st4:
#     print(x, end=" ")
#     print("1 2 ka 4");


# for i in range(len(st4) - 1, -1 , -1):
#     print(st4[i], end="");

# print();

# for i in range(-1, -(len(st4) + 1),-1):
#     print(st4[i],end="")

# print();
# st5 = st4 + 'Good morning';
# print (st4);
# print();
# print (st5);


st6 = "CoDing Seekho";

lis=[]
ans =""
for i in range(0,len(st6)):
    ch = st6[i];
    if ch == ' ' or ((len(st6)-1) ==  i):
        # lis.append(st6[len(st6) -1]);
        if ch != ' ':
            lis.append(ch);
        
        lis.reverse();
        print(lis);
        temp =''
        for x in lis:
            temp = temp + x;
    

        lis = []
        ans = ans + temp ;
        if ch == ' ':
            ans += ' ';
        print(ans)
    else:
        lis.append(ch);

# print(lis);
print(ans);

# print(len(st6));
# print(len(ans));

# for x in ans:
#     print(x);


