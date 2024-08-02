while True:
    print("\033[1m\033[4mA Simple Arithmetic Calculator\033[0m\033[0m")
    print("The following operations can be performed:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    
    x=int(input("Enter your choice of operation(1/2/3/4/5):"))

    if x not in [1,2,3,4]:
        print("Please enter a valid number")
        exit()
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    if x==1:
        c=a+b
        print("The addition of",a,"and",b,"is",c)
    elif x==2:
        c=a-b
        print("The subtraction of",a,"and",b,"is",c)
    elif x==3:
        c=a*b;
        print("The multiplication of",a,"and",b,"is",c)
    elif x==4:
        if b==0:
            print("ERROR: Division by 0")
        else:
            c=a/b
            print("The division of",a,"by",b,"is",c)
    elif x==5:
        break

