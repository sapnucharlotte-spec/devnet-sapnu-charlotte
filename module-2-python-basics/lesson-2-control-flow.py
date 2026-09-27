"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Sapnu, Charlotte G.
Date: 

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
============================================
So the control flow using if, elif, and else is used in programming to make decisions. 
The if statement is used to check if a condition is true, and if it is true, the program will run the code inside it. 
If the if condition is false, the program can use elif to check another condition or choice. 
If the if and all elif conditions are false, the else statement will run. In simple words, if means “if this is true, do this,” 
elif means “if the first choice is false, check this other choice,” and else means “if none of the choices are true, do this instead.”
============================================
KEY VOCABULARY
============================================
- condition: Is a statement or question that the program checks to see if it is true or false. It helps the program decide what action to take. 
- if / elif / else: 
- comparison operator: A symbol used to compare two values. Examples include == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to). 
- boolean expression: Represents whether something is true or false 
- indentation: A space placed at the beginning of a line of code to show which statements belong to an if, elif, or else block. In Python, indentation is important because it tells the computer which code should run together. 
============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
age = 18

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

Well, almost all of the time I’m confusing things about conditions is remembering which comparison operator to use. 
Like this when <= means less than or equal to, while >= means greater than or equal to. 
It is also important to remember that == means equal to, while = is used to assign a value to a variable. 
I want to double-check my conditions to make sure I am using the correct operator and that the condition gives the result I expect.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
This can be connected to real-life situations because we make decisions based on conditions every day. 
Let's just say if it is raining, I will bring an umbrella. If it is sunny, I might wear a hat. 
Otherwise, I may not need either one. This is similar to how if, elif, and else work in programming because the 
program checks different conditions and chooses what to do based on the result. 
"""
