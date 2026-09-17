print("It is the fist calculater")
input1 = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /): ")
input2 = input("Enter second number: ")

if operator == "+":
    result = float(input1) + float(input2)
elif operator == "-":
    result = float(input1) - float(input2)
elif operator == "*":
    result = float(input1) * float(input2)
elif operator == "/":
    result = float(input1) / float(input2)

print("The result is: " + str(result))

