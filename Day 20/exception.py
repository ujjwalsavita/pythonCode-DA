
try:
    numa= int(input("Enter a number"));
    numb= int(input("Enter a number"));

    if numa > numb:
        print(numa/numb);
    elif numb > numa:
        print(numb/numa);
    else:
        print(numa/numb);
except ZeroDivisionError as e:
    # print("kuch to problem hai");
    print("kya bhia inta padhna ke baad input galat le rahe hai ap",e);
except ValueError:
    print("kya bhia inta padhna ke baad input galat le rahe hai ap");
else:
    print("good job koi exception nahi aya hai");
finally:
    print("Process Completed successfully");


print("ula ulaa");
print("set of lines")