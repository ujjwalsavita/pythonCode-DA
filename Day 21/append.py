file = open("file.txt",'a');

file.seek(0);
print(file.tell())

print(file.tell());
file.write(" Books leni, exam pass hai")
print(file.tell())