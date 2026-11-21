file = open("data.txt",'r');

# content = file.read();
# print(content)

print(file.tell());
print(file.seek(6))
print(file.tell());

for line in file:
    # print(file.tell());
    # print(line.tell());
    print(line.strip());

print(file.tell());