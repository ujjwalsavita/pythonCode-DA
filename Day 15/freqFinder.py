lis =[23,4,5,6,7,7,8,98,64,3,2,2,4,6,88,8,7];

st = set();
# for x in lis:
#     # print(x,lis.count(x));
#     val = (x, lis.count(x))
#     st.add(val);


# # print(st);
# for x in st:
#     print(x);


# for x in lis:
#     count = 0;
#     for y in lis:
#             if x == y :
#                 count += 1;

#     val = (x, lis.count(x))
#     st.add(val);
 
# print(st);



freq_dict = {}

# 2. Loop and count
for x in lis:
    freq_dict[x] = freq_dict.get(x, 0) + 1;
   
print(freq_dict)




