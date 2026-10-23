row = int(input("enter the number of rows"));

for i in range(1, row + 1):
    # space
    for k in range(1, row - i + 1):
        print("  ", end=" ");

    # students
    for j in range(1, i+ 1):
        print("* ", end=" ");

    print();
    