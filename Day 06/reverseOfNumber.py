num = int(input("enter a number "));

rev = 0;
mum = num

while num > 0:
    di = num % 10;
    rev = rev * 10 + di;
    num //= 10

print("Reverse of the ",mum, " is ", rev);