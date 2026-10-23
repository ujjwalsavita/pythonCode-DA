row = int(input("Enter row number "));

for i in range(1, row + 1):
    # space
    for k in range(1, i):
        print(" ", end=" ");

    # studetns
    for j in range(1, row - i + 2):
        print("*", end=" ")

    print();