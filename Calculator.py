operator = None
while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter Operator (*,/,%,+,-,**,//): ")
    if operator == "*":
        result = a * b
        print(result)
    elif operator == "/":
        result = a / b
        print(result)
    elif operator == "%":
        result = a % b
        print(result)
    elif operator == "+":
        result = a + b
        print(result)
    elif operator == "-":
        result = a - b
        print(result)
    elif operator == "**":
        result = a**b
        print(result)
    elif operator == "//":
        result = a//b
        print(result)
    else:
        print("Enter a valid Operator")
        exit()