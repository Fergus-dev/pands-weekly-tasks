# weekly task 04
# this program takes input in the form of an int
# and using if statements and while loops performs calculations depending on the even/odd value of the number
# until the number reaches 1
# Fergus McTiernan

user_input = int(input("Please enter a positive integer: "))

if user_input != int:
    print("Input invalid")
    user_input = int(input("Please enter a positive integer: "))

while user_input != 1:

    if user_input % 2 == 0:
        user_input = int(user_input // 2)
        print(user_input)
    
    else:
        user_input = int(user_input * 3 + 1)
        print(user_input)    


