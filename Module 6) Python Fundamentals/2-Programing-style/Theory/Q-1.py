"""
Understanding Python's PEP 8 guidelines.

-->
    PEP 8, or Python Enchantment Proposal 8, is the official style guide for python.
    It establishes conventions for writing clean, and consistent Python code, making it 
    easier to understand, debug, and maintain.

    Key Aspects of PEP 8

    1. Code Layout 

        Indentation : Use 4 spaces per intendation level. Avoid using tabs.
        Line length : Limit lines to maximum of 79 characters to enhance readability.
        Blank lines : Use :
                            Two blank lines to seperate top-level function or class definitions.
                            One blank line to seperate logical sections within function.

    
    2.Imports

        Place imports at the top of the file.
        Group them in the following order :

            1. Standard library imports. 
            2. Third-party library imports.
            3. Local applications imports.

        Use one import per line (e.g. import os and import sys).

    
    3.Naming conventions 

        Variable and Functions : Use lowercase names with words seperated by underscores
        (snake_case).

        Classes : Use PascalCase (e.g. MyClass).

        Constants : Use all uppercase letters with words seperated by underscores (e.g. MAX_LIMIT).

        Private variables : Prefix Variable names with an underscore (e.g. _private_var).


    4. Whitespace 

        Avoid unnecessary spaces around parentheses, brackets, or braces.

        Add spaces around operators and after commas for better readability.

    
    5.Comments 

        Block comments : Use for detailed explanation of section of code.

        Inline comments : Use sparingly, keeping them breif.

        Docstrings : Use triple quotes to describe modules, classes, and functions.

    
    6. Functions and classes 

        Use descriptive names for functions ans methods.

        Include docstrings to explain their purpose and behavior.

        keep class definitions and functions concise and focused.


    7. Error handling 

        Use specific exceptions and avoid catching generic Exceptionn.

    
    PEP 8 is an essential guideline for writing professional and maintanable Python code.
    Adhering to it ensures that your code base remains clean, organized, and easy to navigate.

"""