dic = {
    "name" : "Coding seekho",
    'age':1,
    ("name", "age"): "Coding seekho amar rahe"
}



dic["name"] = "Coding Seekho Jinda Baad";

print(dic);
print(type(dic));
print(dic.get("name"));
print(type(dic.items()));




# print(dic.items());


dic = {
    ("name","Coding seekho") : 7378967573
}
st, = dic.items();
print(type(st));

for x in st:
    # print(x);
    if x in dic:
        print(dic[x]);







