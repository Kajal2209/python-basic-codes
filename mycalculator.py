first = input("enter the firsst number :")
operator = input("enter the operator(+,-,%,*) :")
second = input("enter the sencond number :")


if operator == "+":
    print(int(first) + int(second))
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
else:
    print("invalid operator")



