# SDEV 220 - CatalanoMatteo_M02_01.py - M02 Lab - Case Study: if...else and while
# Catalano Matteo
# 24/03/2023
# The program accepts student names and GPAs, and tests if the student qualifies for the Dean's List or the Honor Roll.
# Variables descriptions:
# last_name: a string variable that stores the last name of the student entered by the user
# first_name: a string variable that stores the first name of the student entered by the user
# gpa: a float variable that stores the GPA of the student entered by the user
# exit_code: a string constant that contains the exit code used to terminate the program loop (in this case, "ZZZ")


exit_code = "ZZZ"
# Loop through student records until user enters "ZZZ" for the last name.
while True:
    last_name = input("Enter the student's last name (enter ZZZ to quit): ")

    # Exit the loop if the user enters "ZZZ".
    if last_name == exit_code:
        break

    # Get the student's first name and GPA.
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    # Test if the student qualifies for the Dean's List.
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    # Test if the student qualifies for the Honor Roll.
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    # If the GPA is below 3.25, the student has not qualified for any academic award.
    else:
        print(f"{first_name} {last_name} has not qualified for any academic award.")