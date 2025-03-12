"""
How to take user input using the input() function.

-->
    The input() function in python allows you to take input from the user during program execution.
    The data entered by the user is returened as string.

    Syntax :
            Variable=input(prompt)

    Steps to use input()

        1. Display a prompt :

            You can pass a message as a prompt to inform the user what input is expected.

                for e.g. name=input("Enter your name : ")

        2.Convert input into other Datatypes :

            By default, input() return a string. To work with numbers or other types, you
            need to convert the input explicitly.

                for e.g. age=int(input("Enter your age : "))
                         height=float(input("Enter your height : "))

        The input() function is a simple and flexible way to take user input in python.
        By converting input to the required data type and validating it properly, you can 
        create interactive and userfriendly programs.
"""