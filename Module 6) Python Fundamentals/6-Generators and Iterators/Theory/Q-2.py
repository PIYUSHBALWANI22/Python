"""
Difference between yield and return.

--> When comparing yield and return in Python, the diffrence extend beyond just syntax, they shape how a function
    behaves and interacts with its caller.

    1) Execution Flow 

            return : 

                Immediate Termination : When a function encounters a return statement, it immediately exits, sending back a single
                value (or None if no value is provided).

                One-Time Response : The function's computation is completed in one go.
                Subsequent calls to the function start fresh, the state of previous executions is lost.

            yield : 

                Pausing Execution : Instead of exiting completely, yield pauses the function, yielding a value to the caller while 
                preserving the function's local state (including local variables and the current position in the code).

                Lazy Evaluation : The function becomes a generator. Each call to next() resumes execution right after the last yield,
                allowing a function to produce a series of values over time.

    2) Use cases and Behavior 

            return :

                Final Result : Best used when you have a single, complete outcome to provide from a function.

                Standard Functions : Commonly used in a regular functions, where the entire procesing is meant to be done, and then
                the result is returened to the caller.

            yield : 

                Iterative Data Production : Ideal when you want to produce a stream of data without needing to compute or store everything
                at once.

                Generators : Functions using yield return generartor objects, which are iterators that produce items one by one on demand.
                This is especially useful for large datasets or infinite sequences.

    3) Memory and Performance Implications 

            return: 

                In-Memory Results : The entire result is produced and returned at once. For large amounts of data, this can be costly in
                terms of memory since everything is stored in memory before use.

            yield :

                Memory Efficieny : Only one value is produced at a time, reducuing memory usage. Each value is generated on the fly, which 
                is often more efficient when dealing with huge datasets or streams. 

    4) Conceptual Diffrences 

        State preservation : 

            return : The function's state is not maintained after the function finishes executing.

            yield : The function's state is saved between yields, allowing the function to resume where it left off.

        Control Flow :

            return : Ends the function entirely once executed. No further code in the function is processed after a return.

            yield : Split's the function's execution into multiple parts, each capable of outputting a seprate value. The
            generator function can be seen as a "paused" process that continues when requested.

    5) Practical Implications 

        Consider a function that process items in a large file : 

            Using return, you might read all the items into a list and then return the list. This could be efficient if the file is large.

            Using yield, you can process each item one by one and yield it immediately to the caller. This approach means you never hold
            the entire file in memory at once.    
"""