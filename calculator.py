first=input("enter the first number:")
operator=input("enter the operator(+,-,*,/,%):")
second=input("enter the second number:")
if operator=="+":
    print(int(first) + int(second))
elif operator=="-":
     print(int(first) - int(second))
elif operator=="*":
     print(int(first) * int(second))
elif operator=="/":
     print(int(first) / int(second))
elif operator=="%":
     print(int(first) % int(second))
else:print("operator is not valid")