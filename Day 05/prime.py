# num = int(input("Enter a number"));

# if num <= 1:
#     print("Entered number is not prime");

# else:
#     for x in range(2, num):
#         if num % x == 0:
#             print("Entered number is not prime");
#             break
#     else:
#         print("Enter number is prime");



num = int(input("Enter a number"));

if num <= 1:
    print("Entered number is not prime");

else:
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            print("Entered number is not prime");
            break
    else:
        print("Enter number is prime");