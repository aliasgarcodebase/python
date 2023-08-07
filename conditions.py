age = input("Please enter your age")
age = int(age)
if age >= 18:
    print("You are eligible to vote")
    print("You can vote")
elif age < 18 and age > 3 :
    print("You are too young")
else :
    print("You are small baby")

print("Thank you...")