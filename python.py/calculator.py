print('          "welcome to simple calculator"          ')

print("For Addition enter          (a)")
print("For Subtraction enter       (s)")
print("For Multiplication enter    (m)")
print("For Division enter          (d)")

v = str(input(" enter your interest here : --> "))
if(v == "a" or v == "s" or v == "m" or v == "d"):

    x = float(input("enter first number : ---> "))
    y = float(input("enter second number : ---> "))

    if(v == "a"):
        v = x + y
        print("Addition of ",x," and ",y," is ",v,".")
        print("             Thank u for using me             ")
    elif(v == "s"):
        v = x - y
        print("Subtraction of ",y," from ",x," is ",v,".")
        print("             Thank u for using me             ")
    elif(v == "m"):
        v = x * y
        print("Multiplication of ",x," and ",y," is ",v,".")
        print("             Thank u for using me             ")
    elif(v == "d"):
        v = x / y
        print("Division of ",x," and ",y," is ",v,".")
        print("             Thank u for using me             ")
else:
    print(" Sorry u have enter wrong letter")
