num = int(input("Enter a number to check it is armstrong or not"));
mum = num;
count = 0;
# digit count kar rahe hai
while num > 0:
    count += 1 ;
    num //= 10;

num = mum;
arm = 0
while num > 0:
    di = num % 10;
    arm += di ** count;
    num //= 10;

if mum == arm:
    print("yes");
else: 
    print("No");


