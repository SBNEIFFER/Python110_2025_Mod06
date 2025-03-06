# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
# SNeiffer, 3/2/2025, Created Script
# ------------------------------------------------------------------------------------------ #
import json
from typing import TextIO

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
students: list = []  # a table of student data


class FileProcessor:
    """
    A collection of presentation layer functions that work with JSON files
    """

    @staticmethod
    def write_data_to_file(file_name: str, student_table: list):
        """
        This function writes user captured data to the JSON file
        Returns: None

        SNeiffer, 3/2/2025, Created function

        Returns: None
        """
        # global FILE_NAME
        # global students
        file: TextIO
        try:
            file = open(FILE_NAME, "w")
            json.dump(student_table, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_table:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("Please ensure the data is in JSON format.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error.", e)
        finally:
            if file.closed == False:
                file.close()


    @staticmethod
    def read_data_from_file(student_table: list[dict], file_name: str):
        """
        This function extracts data from a JSON file

        Sneiffer, 3/2/2025, Created function

        Returns: student table
        """
        try:
            file = open(file_name, "r")
            student_table += json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running script.", e)
        except Exception as e:
            IO.output_error_messages("There was an unhandled error.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_table


class IO:
    """
    A collection of presentation layer functions that manage user input and output
    """

    @staticmethod
    def input_student_data(student_table: list):
        """
        This function captures the student information from the user

        SNeiffer, 3/2/2025, Created function

        Returns: str
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_table.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("You entered invalid data.", e)
        except Exception as e:
            IO.output_error_messages("There was an unhandled exception!", e)
        return student_table


    @staticmethod
    def output_student_courses(student_table: list):
        """
        This function displays the current student data

        SNeiffer, 3/2/2025, Created function

        Returns: None
        """
        print("-" * 50)
        for student in student_table:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)


    @staticmethod
    def input_menu_choice():
        """
        This function captures the users menu choice

        SNeiffer, 3/2/2025, Created function

        Returns: User's choice as string
        """
        menu_choice = "0"
        try:
            menu_choice = input("What would you like to do: ")
            if menu_choice not in ("1","2","3","4"):
                raise Exception("Please choose a valid menu option.")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return menu_choice


    @staticmethod
    def output_menu(menu: str):
        """
        This function prints the menu options to the user

        SNeiffer, 3/2/2025, Created function

        Returns: None
        """
        print()
        print(menu)
        print()


    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays custom error message to the user

        SNeiffer, 3/2/2025, Created function

        Returns: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')


#Extracting data from the JSON file

student_table = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_table = students)

while True:

    #Displaying menu options to the user

    IO.output_menu(menu = MENU)

    #Capturing user's menu option as a string

    menu_choice = IO.input_menu_choice()

    #Displaying current student data if the user's menu option is equal to '1'

    if menu_choice == '1':
       student_table = IO.input_student_data(student_table = students)

    #Capturing student firstname, lastname, and course name input from user if their menu option is equal to '2'

    elif menu_choice == '2':
        IO.output_student_courses(student_table = students)

    #Writing all data to JSON file if user's menu option is equal to '3'

    elif menu_choice == '3':
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_table = students)

    #Exiting the program is user's menu option is equal to '4', notifies user that program ends

    elif menu_choice == '4':
        print("Program ended.")
        break

    #Displays message if user's menu choice is equal to anything other than '1' , '2', '3', '4'

    else:
        print("Please only choose option 1, 2, or 3.")