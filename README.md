# Even and Odd Checker using *args in Python

This is a beginner friendly Python program that checks whether multiple inputs are **even or odd** using a function and `*args`.

## 📌 About the Program
The program defines a function `check_even_odd(*args)` which accepts **any number of arguments**.  
It checks each argument:
- If the value is an integer, it determines whether it is **even or odd**
- If the value is not an integer, it prints **invalid input**

This helps beginners understand:
- Functions
- `*args`
- Loops
- Conditional statements
- Type checking using `isinstance()`

## 🧠 Code Explanation
- `*args` allows passing multiple values to the function
- `isinstance(i, int)` ensures only integers are processed
- `% 2` is used to check even or odd numbers
