"""
Understanding the role of break, continue, and pass in Python loops. 

--> Here is the explanation for the role of break, continue, and pass in Python loops:

1. The break Statement
The break statement is used to terminate a loop prematurely when a specific condition is met.

It immediately stops the loop's execution, and control moves to the first statement after the loop.

It is primarily used to optimize loop execution by stopping unnecessary iterations once the desired condition is satisfied.

Works with both for and while loops.

2. The continue Statement
The continue statement skips the rest of the code in the current iteration and proceeds to the next iteration of the loop.

Unlike break, it does not terminate the loop; instead, it jumps to the next cycle of the loop.

It is useful when certain iterations need to be ignored while ensuring that the loop continues to execute other iterations.

Applicable in both for and while loops.

3. The pass Statement
The pass statement is a null operation; it does nothing when executed.

It acts as a placeholder in the code where a statement is syntactically required but no operation is necessary.

Often used during code development to define empty loops, functions, or classes, allowing the program to run without errors.

Key Differences

break: Exits the loop entirely.

continue: Skips the current iteration and moves to the next.

pass: Does nothing and serves as a placeholder.
"""