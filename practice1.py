num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

Choice_of_operator=input("Enter the choice of operator +, _,\n " )

if Choice_of_operator== "+":
    sum_of_digit=num1+num2
    print("Sum is :", sum_of_digit)
elif Choice_of_operator== "-":
    sub_of_digit=num1-num2
    print("Sub is :", sub_of_digit)
else:
    print("Envalid input")
