num = int(input("Enter a fixed number "));

attemps = int(input("Enter how many attemps you want"));

print()
print()

for x in range(0 , attemps ):
    n = int(input("Enter your number "));

    if n == num :
        print("yes ap jit gaye dost ");
        break
    elif num > n :
        print("my number is greater ");
    else:
        print("my number is smaller");
else:
    print("yes, ap 7 cr jit gaye");


# print(type (ord('9')))
# print(type (chr(57)))



