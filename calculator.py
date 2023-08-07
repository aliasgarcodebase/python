input_1 = input("Please enter first number: ")
input_2 = input("Please enter second number: ")
operator_type = input("Please select type of your operator to perform: ")

input_1 = int(input_1)
input_2 = int(input_2)
if operator_type == "+":
    output = input_1+input_2
elif operator_type == "-":
    output = input_1-input_2
elif operator_type == "*":
    output = input_1*input_2
elif operator_type == "/":
    output = input_1/input_2
else:
    output = "Invalid"

print(output)