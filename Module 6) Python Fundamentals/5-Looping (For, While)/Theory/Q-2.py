"""
How loops work in Python. 

--> 1) The for Loop :

            The python for loop is more than just a counter-- Its and iterator. Instead of manually controlling
            an index, the loop directly goes through each element of an iterable(like list, tuples strings, or even 
            file objects.)

        How it works :

            Iteration : When you write a for loop, python internally calls the iter() function on the iterable. It then uses the it then
                        uses the iterator's __next__() method to fetch each element until it rasies a stopIteration exception (which signals
                        the end).
            
            Syntax and Indentation : The block of code inside the loop must be indented--this tells python what's part of loop.


    2) The while loop : 

            The while loop continues to execute as long as its condition is True. It's perfect when you don't know in advance how many times
            you need to itrate--just that you need to keep going until the goal is met.

        How it works :

            Condition based : Before every iteration, the loop evaluates a condition. If it's True, the loop body executes. If it's False,
            the loop stops.

            Manual control : With while loops, you often need to update the evaluates the value involved in the condition to avoid creating
            an infinite loop.

    3) Loop control tools : 

            Python enhances loop functionality with a few useful kwywords :

                break : Immediately exits the loop.

                continue : Skips to the new iteration.

                pass : A placeholder that does nothing , its sytacially needed when a statement is required but no action is desired.

                else : Clause on loops : for and while loops can have an else block that runs if the loops completes normally (i.e it wasn't
                terminated by a break).
"""