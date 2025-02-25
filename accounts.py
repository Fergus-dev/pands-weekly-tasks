# weekly task 03
# this program reads in an account number and outputs the the number with all but the last four digiits replaced with X's

# looking for input in form of interger first so user can't input letters
inputted_number = int(input("Please enter your account number: "))

# then converting to a string so I can slice it etc.
number_converted = str(inputted_number)

# slicing and storing the last four digits
last_four_digits = number_converted[-4:]

# I asked CoPilot for help with this last part. This code counts the number of characters leading up to the last four digits and produces an equal number of X's
hidden_digits = len(number_converted[:-4]) * "X"

# I've simply got to concatenate the two strings then to get the desired output
print(f"Your account number: {hidden_digits}{last_four_digits}")
