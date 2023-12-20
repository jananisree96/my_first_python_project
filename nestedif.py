# Nested If Program to Check Voting and Driving Eligibility

# Get the age as input from the user
age = int(input("Enter your age: "))

# Check eligibility to vote
if age >= 18:
    print("You are eligible to vote.")
    
    # Check eligibility to drive
    if age >= 16:
        print("You are also eligible to drive.")
    else:
        print("You are not eligible to drive.")
        
else:
    print("You are not eligible to vote or drive.")

