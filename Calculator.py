num1=int(input("Enter the number:"))
num2=int(input("Enter the second number:"))
print("Below are the operations to perform on a calculator")
print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division")
str=input("Enter your choice:")
match str :
    case "Addition":
        print(f"The addition of {num1} and {num2} is {num1+num2}")
    case "Substraction":
        print(f"The substraction of {num1} and {num2} is {num1-num2}")
    case "Multiplication":
        print(f"The multiplication of {num1} and {num2} is {num1*num2}")
    case "Division":
        print(f"The division of {num1} and {num2} is {num1//num2}")

