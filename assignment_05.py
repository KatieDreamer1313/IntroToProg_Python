# ------------------------------------------------------------------------------------------ #
# Title: Assignment 5
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   KHarrison,06/06/2024,Created Script
# ------------------------------------------------------------------------------------------ #

# constants #

FILE_NAME: str = "enrollments.csv"

MENU: str = '''
------------------Student GPA------------------
    Select from the following menu:
        1. Register a Student for a Course
        2. Show current data
        3. Save data to a file
        4. Exit the program
-----------------------------------------------
'''

# global variables #

menu_choice: str = ""
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
student_data: dict = {}
students: list = []



# functions and execution #

while True:
    print(MENU)
    menu_choice = input("Please select an option from the menu: ")
    print()

    # collect user data, save in a dictionary format, then add to table "students"
    if menu_choice == "1":
        try:
            student_first_name = input("Please enter the student's first name: ")
            if not student_first_name.isalpha():
                    raise ValueError("The first name should not contain numbers.")
            
            student_last_name = input("Please enter the student's last name: ")
            if not student_last_name.isalpha():
                    raise ValueError("The last name should not contain numbers.")
            
            course_name = (input("Please enter the student's course: "))

            student_data = {"First Name": student_first_name, "Last Name": student_last_name, "Course": course_name}
            students.append(student_data)

        except ValueError as value_error_details:
            print(value_error_details)
            print(" -- Technical Error Message -- ")
            print(value_error_details.__doc__)
        except Exception as unspecified_error_details:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(unspecified_error_details,unspecified_error_details.__doc__, type(unspecified_error_details),sep = "\n")
       
    # download data from CSV, convert to dictionary format, add to table "students", print collected data
    elif menu_choice == "2":
        try:  
            with open(FILE_NAME, "r") as file:
                for row in file.readlines():
                    student_data = row.split(",")
                    student_data = {"First Name" : student_data[0], "Last Name" : student_data[1], "Course" : (student_data[2].strip())}
                    students.append(student_data)

                    print()
                    print("These students have been saved to file: ")
                    for row in students:
                        student_first_name = row["First Name"]
                        student_last_name = row["Last Name"]
                        course_name = row["Course"]
                        print(f'{student_first_name},{student_last_name},{course_name}')

        except FileNotFoundError as file_not_found_details:
            print("File must exist before running this script.\n")
            print("-- Technical Error Message --")
            print(file_not_found_details,file_not_found_details.__doc__, type(file_not_found_details),sep = "\n")
        except Exception as unspecified_error_details:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(unspecified_error_details,unspecified_error_details.__doc__, type(unspecified_error_details),sep = "\n")

    # save data collected in step 1 to CSV
    elif menu_choice == "3":
        try:
            with open (FILE_NAME, "w") as file:
                for row in students:
                    file.write(f'{row["First Name"]}, {row["Last Name"]}, {row["Course"]}\n')
        except TypeError as type_error_details:
            print("Please check that the data is a valid CSV format\n")
            print(" -- Technical Error Message -- ")
            print("Built-in Python error info: ")
            print(type_error_details, type_error_details.__doc__, type(type_error_details), sep = "\n")
        except Exception as unspecified_error_details:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(unspecified_error_details,unspecified_error_details.__doc__, type(unspecified_error_details),sep = "\n")

    # exit the program
    elif menu_choice == "4":
        break

    # catch non-menu choices
    else:
        print("Please enter a choice from options 1-4")