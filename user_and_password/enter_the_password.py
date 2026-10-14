import time

atts = 0 # Documents attempts done (starts at 0)
max_atts = 5 # Gives maximum value of attempts
correct_user = "%My_User%" # Correct username
correct_pass = "%My_Password%" # Correct password
print("------------------------")
user_entered = input("Enter your username here: \n\n") # Prompts user to enter username
print("------------------------")
pass_entered = input("Enter your password here: \n\n") # Prompts user to enter password
print("------------------------\n\n")

while (correct_pass != pass_entered or correct_user != user_entered) and (atts < max_atts): # Loop that checks if units entered are correct and if attempts have exceeded the maximum attempts
        atts+=1
        print("!!!Username or password is/are incorrect!!!\n\n")
        print("------------------------")
        user_entered = input("Enter your username here: \n\n") # Prompts user to enter username
        print("------------------------")
        pass_entered = input("Enter your password here: \n\n") # Prompts user to enter password
        print("------------------------\n\n")
if correct_pass == pass_entered and correct_user == user_entered: # Statement that checks if correct units have been entered
    print("!!!Password correct, access granted!!!\n\n")
    print(f"Attempts used: {atts}\n\n")
else: # Statement that executes if maximum attempts is reached
    print("!!!Maximum attempts used. Access denied for 60 seconds!!!\n\n")

    for countdown1 in reversed(range(1,61)): # Counts down from 60 to 1
        time.sleep(1)
        print(f"{countdown1}... ")

    atts = 0 # Resets attempts done (starts at 0)
    print("------------------------")
    user_entered = input("Enter your username here: \n\n") # Prompts user to enter username
    print("------------------------")
    pass_entered = input("Enter your password here: \n\n") # Prompts user to enter password
    print("------------------------\n\n")

    while (correct_pass != pass_entered or correct_user != user_entered) and (atts < max_atts): # Loop that checks if units entered are correct and if attempts have exceeded the maximum attempts
        atts+=1
        print("!!!Username or password is/are incorrect!!!\n\n")
        print("------------------------")
        user_entered = input("Enter your username here: \n\n") # Prompts user to enter username
        print("------------------------")
        pass_entered = input("Enter your password here: \n\n") # Prompts user to enter password
        print("------------------------\n\n")
    if correct_pass == pass_entered and correct_user == user_entered: # Statement that checks if correct units have been entered
        print("!!!Password correct, access granted!!!\n\n")
        print(f"Attempts used: {atts}\n\n")
    else:
        # Locks user out of account after max attempts are reached in second chance
        print("!!!Maximum attempts used. Access denied!!!\n\n")
        print("You have been identified as a hacker. You are now locked from this account.\n\n")