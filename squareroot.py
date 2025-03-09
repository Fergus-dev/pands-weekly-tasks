# weekly task 06
# square root approximator
# Fergus McTiernan
# Sources used:
#               https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#               https://en.wikipedia.org/wiki/Newton%27s_method
#               https://web.ma.utexas.edu/users/m408n/CurrentWeb/LM4-8-2.php
#               https://www.youtube.com/watch?v=FpOEx6zFf1o
#               https://www.google.com/search?q=newton+method+of+square+root+approximation+in+python&sca_esv=248c1a1232d6ce85&rlz=1C1GCEA_enIE1148IE1148&sxsrf=AHTn8zqJPWSiAIVYQx-e_FcUQlPLIzBdBw%3A1741521741439&ei=TYPNZ6q7GrW0hbIP6Lj0iAo&ved=0ahUKEwjqlZGG-vyLAxU1WkEAHWgcHaEQ4dUDCBA&uact=5&oq=newton+method+of+square+root+approximation+in+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiNG5ld3RvbiBtZXRob2Qgb2Ygc3F1YXJlIHJvb3QgYXBwcm94aW1hdGlvbiBpbiBweXRob24yBRAhGKABMgUQIRigAUjpFVDjB1ibFHACeAGQAQCYAYIBoAGhBqoBBDEwLjG4AQPIAQD4AQGYAg2gAuIGwgIKEAAYsAMY1gQYR8ICBRAhGJ8FwgIHECEYoAEYCpgDAIgGAZAGCJIHBDEyLjGgB5s0&sclient=gws-wiz-serp#fpstate=ive&vld=cid:6687d5ef,vid:xdlIFw5EM4w,st:0


# defining function for guessing squareroot
def sqrt(n):
    assumed_approx = 0.5 * n
    better_approx = 0.5 * (assumed_approx + (n / assumed_approx))

    while better_approx != assumed_approx:
        assumed_approx = better_approx
        better_approx = 0.5 * (assumed_approx + (n / assumed_approx))

    print(f"The approximate square root of {user_input} is {better_approx}")
        

# prompt user for input in form of positive number. Look for absoloute values only by first converting user input (string) into a float type.
user_input = abs(float(input("Please enter a positive number: ")))
print(f"You entered {user_input}")
sqrt(user_input)