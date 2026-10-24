row = int(input("Enter the number of rows "));


for i in range(1, row + 1):
    # space
    for k in range(1, row - i + 1):
        print(" ", end=" ");

    c = 1;

    # pattern
    for j in range(1, 2*i):
        if j <= i:
            print(j, end=" ");
        else : 
            print(i - c, end=" ");
            c = c + 1;

    print()

