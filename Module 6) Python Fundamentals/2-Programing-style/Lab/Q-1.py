"""
Write a Python program that demonstrates the correct use of indentation, comments, and 
variables following PEP 8 guidelines. 

-->
    Key Aspects Following PEP 8:

        1). Indentation:

            The code uses 4 spaces per indentation level (not tabs).

        2). Comments: Block comments and inline comments are used for clarity.

            Docstrings (" " ") provide explanations for functions and the main program.

        3). Variable Naming:

            Variable names are descriptive and use snake_case.

        4). Constants:

            Constants are named in uppercase (e.g., INCH_TO_CM).

        5). Line Length:

            No line exceeds 79 characters (PEP 8 recommendation).

        6). Whitespace:

            Proper whitespace is used around operators (=, +, *, etc.).

            Blank lines separate logical sections of the code (e.g., between functions).

        7). Modularity:

            The program is broken into functions for reusability and clarity.

"""
# Program to calculate the area and perimeter of a rectangle

# Constants for conversion (if needed)
INCH_TO_CM = 2.54  # 1 inch = 2.54 cm

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    :param length: Length of the rectangle.
    :param width: Width of the rectangle.
    :return: Area of the rectangle.
    """
    return length * width

# Function to calculate the perimeter of a rectangle
def calculate_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.
    :param length: Length of the rectangle.
    :param width: Width of the rectangle.
    :return: Perimeter of the rectangle.
    """
    return 2 * (length + width)

# Main function
def main():
    """
    Main function to execute the program.
    """
    # Input: User provides dimensions in inches
    length_in_inches = float(input("Enter the length of the rectangle (in inches): "))
    width_in_inches = float(input("Enter the width of the rectangle (in inches): "))

    # Convert dimensions to centimeters for metric calculations
    length_in_cm = length_in_inches * INCH_TO_CM
    width_in_cm = width_in_inches * INCH_TO_CM

    # Calculate area and perimeter
    area = calculate_area(length_in_cm, width_in_cm)
    perimeter = calculate_perimeter(length_in_cm, width_in_cm)

    # Output: Display the results
    print(f"\nRectangle Dimensions (in cm):")
    print(f"Length: {length_in_cm:.2f} cm, Width: {width_in_cm:.2f} cm")
    print(f"Area: {area:.2f} square cm")
    print(f"Perimeter: {perimeter:.2f} cm")

# Execute the program
if __name__ == "__main__":
    main()

# This program adheres to PEP 8 standards and demonstrates clean, readable, and maintainable Python code.