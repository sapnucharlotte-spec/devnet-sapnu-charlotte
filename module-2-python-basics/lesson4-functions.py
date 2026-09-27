"""
Module 2 — Lesson 4: Functions
Student: Sapnu, Charlotte G. 
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
So functions are blocks of code that are created to perform a specific task. 
They help programmers avoid writing the same code repeatedly. A function can receive information, process it, and return a result. 
It always starts with the “def” keyword followed by the function’s name and parentheses. 
When a function called “greet()” can be used to display a greeting. In short, the functions make programs easier to organize, understand, and reuse.
============================================
KEY VOCABULARY
============================================
- def: Used to create or define a function. 
- function: A reusable block of code that performs a specific task. 
- parameter: A variable that receives information inside a function.
- argument: The actual value given to a function when it is called. 
- return: Send a result back from the function. 
- local variable: A variable created inside a function.
- global variable: A variable that can be accessed from different parts of a program.
============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
def quote(name):
    print("Live with love, " + name + ".")

def score(num):
    print(50 + num)

quote("Luka")
score(47)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
Functions are easy to understand by themselves, but I think I might get confused when 
I combine them with loops or if-else statements. I’m struggling to understand it right away because there are more 
parts of the code to follow. I need to practice how functions work together with other concepts. 
============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
Well, functions can be useful in real life because they are like instructions for doing a specific task. I would like this to connect to a recipe as a 
function because you can follow the same steps whenever you want to make the same food. 
"""
