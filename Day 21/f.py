# file = open(r"C:\\Users\\ujjwa\\Desktop\\coding seekho\\Lucknow\\DAB3\\Day 20\\data.txt", 'w');

file = open("data.txt", 'w');
print(file.tell());
file.write("Good evening, bahut thand hai.\n");
print(file.tell());

lis = ['Shubham\n', 'Vishal\n','Sachin\n','Prabhat\n' ,'Shyam\n'];

count = 1;
for x in lis:
    file.write('{}.{}'.format(count,' '))
    file.write(x);
    count += 1;

print(file.tell()); 

file.seek(32);
file.write("pintu lala")




file.close();


with open("file.txt", 'w') as fi:
    print(fi.write("Hello papa ji, paise chahiye ta books"));
    pass



print("hello bhai ji kaise \n hai ap")


file.write("\n very nice.")