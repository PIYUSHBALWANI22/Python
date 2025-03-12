"""
Using loops with collections (lists, tuples, etc.). 

--> 1) Purpose of using loops with collections 

            Collections like lists and tuples store multiple elements in a single variable.

            Loops help to iterate through these collections, making it possible to process, modify, or analyze each
            element without writing repitive code manually.

    2) Types of loops for iteration

            For loop : A common choice for iterating through the elements of a collection. It automatically picks each 
                       item one by one.

            While loop : Can also be used, through it requires manual indexing and conditions to prevent infinite looping.

    3) Benifits  

            Automates tasks on large collections.

            Simplifies operations like searching, filtering, aggregating, or transforming data.

            Enhances code readability and maintainability.

    4) Iterating over list

            e.g. numbers = [1, 2, 3, 4, 5]
                 for number in numbers:
                        print(number)  # Outputs each number

    5) Iterating over tuples 

            Works similarly to lists, but tuples are immutable.

            e.g. coordinates = (10, 20, 30)
            for point in coordinates:
                print(point)  # Outputs each coordinate

    6) Enumarating with index 

            Sometimes, the index of elements is also required. The enumrate() function is handy for this.

            e.g. fruits = ['apple', 'banana', 'cherry']
                 for index, fruit in enumerate(fruits):
                     print(f"Index: {index}, Fruit: {fruit}")


    7) Nested loops 

            Useful for collection of collections, such as lists of lists.

            e.g.
                matrix = [[1, 2], [3, 4]]
                for row in matrix:
                    for item in row:
                        print(item)

    8) Using while loops 

            A while loop with collections usually requires indexing.

            e.g. i = 0
                while i < len(numbers):
                    print(numbers[i])
                    i += 1

"""