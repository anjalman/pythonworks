

number = int(input("Enter a number to reverse: "))

# Initialize variables
reversed_number = 0
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number //= 10  # Remove the last digit from the original number

# Output: Display the result
print(f"The reversed number is {reversed_number}")



number=int(input("enter the number:"))
