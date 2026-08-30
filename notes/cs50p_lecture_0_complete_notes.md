# CS50P: Lecture Notes & Setup Guide

---

## Lecture 0: Functions and Variables

`print()` is a built-in function in Python used to output data to the screen.

```python
print("Hello, World!")
```

* `"Hello, World!"` is the **argument** passed into the `print` function.
* The **side effect** is displaying that argument on the screen (the actual return value of `print()` is `None`).

```python
name = "Hello, World!"
print(name)
```

Here, `name` is a **variable** holding the string `"Hello, World!"`.

---

### Taking User Input

`input()` is a built-in function that prompts the user and returns their input as a string:

```python
# Ask user for their name
name = input("What is your name? ")

# Say hello using string concatenation
print("Hello, " + name)

# Or pass multiple arguments (print inserts a space by default)
print("Hello,", name)
```

---

### Official Documentation for `print()`

```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

* **Arguments vs. Parameters:** A *parameter* is the variable listed inside the function definition (e.g., `sep`, `end`). An *argument* is the actual value you pass into the function call.
* `sep` and `end` are **named parameters** (or keyword arguments):
  * `sep=' '`: What separates multiple objects (defaults to a space).
  * `end='\n'`: What prints at the end of the line (defaults to a newline).

**Customizing `end`:**
```python
# Overriding end to keep the output on the same line
print("Hello, ", end="")
print(name)
# Output: Hello, {name}
```

**Customizing `sep`:**
```python
print("Hello", name, sep="???")
# Output: Hello???{name}
```

---

### Escape Characters & Format Strings

The backslash `\` acts as an **escape character** to prevent syntax errors when using quotes inside strings:

```python
# Escaping double quotes inside double quotes
print("Hello, \"friend\"")

# Alternative: use single quotes on the outside
print('Hello, "friend"')
```

**F-Strings (Formatted String Literals):**
Use `f"..."` to embed variables directly inside the string using curly braces `{}`:

```python
print(f"Hello, {name}")
```

---

### String Methods

Methods are built-in functions associated with specific data types. Common methods for the `str` type include:

```python
# Remove leading and trailing whitespace
name = name.strip()

# Capitalize only the very first letter of the string
name = name.capitalize()

# Capitalize the first letter of each word
name = name.title()

# Method chaining: executes sequentially from left to right
name = name.strip().title()

# Split a string into multiple variables based on a separator
first, last = name.split(" ")
```

To make your code cleaner and more concise, you can chain methods directly onto `input()`:

```python
name = input("What is your name? ").strip().title()
print(f"Hello, {name}")
```

---

## Integers (`int`)

Python includes built-in arithmetic operators for numerical data:
* `+` (addition)
* `-` (subtraction)
* `*` (multiplication)
* `/` (division)
* `%` (modulo / remainder)

### Interactive Mode (REPL)
To run code interactively line by line, type `python` in your terminal. When you see the `>>>` prompt, interactive mode is active:

```python
>>> 2 + 2
4
>>> 2 / 2
1.0
>>> 2 * 3
6
>>> 2 - 2
0
>>> print("Hello Leyon")
Hello Leyon
```

### Type Conversion (`int()`)
By default, `input()` always returns a **string (`str`)**:

```python
x = input("Enter x: ")  # User enters 1
y = input("Enter y: ")  # User enters 2

z = x + y
print(z)  # Output: "12" (string concatenation, not arithmetic)
```

To perform math on user input, convert strings into integers using the `int()` function:

```python
# Converting after input
z = int(x) + int(y)  # Returns 3

# Or nesting functions to write more concise code:
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(x + y)
```
*The innermost function (`input()`) runs first to receive text from the user, and the outer function (`int()`) immediately casts that text to an integer.*

---

## Floats (`float`)

A `float` is a real number with a decimal point.

```python
x = float(input("Enter x: "))
y = float(input("Enter y: "))
```

### Rounding & Formatting Floats
Use `round(number, ndigits=None)` to round a number to a specific precision:

```python
# Rounding to the nearest integer
z = round(x + y)

# Rounding to two decimal places
z = round(x / y, 2)
print(z)
```

### Number Formatting with F-Strings

**Adding comma separators to large numbers:**
```python
z = 1000000
print(f"{z:,}")
# Output: 1,000,000
```

**Specifying decimal precision:**
```python
x = float(input("Enter x: "))
y = float(input("Enter y: "))

z = x / y
print(f"{z:.2f}")
```
*Both `round(x / y, 2)` and `f"{z:.2f}"` achieve the same rounded visual output, showing that Python often offers multiple valid ways to solve the same problem.*

---

## Defining Functions (`def`)

You can define custom, reusable functions using the `def` keyword:

```python
def hello():
    print("hello")

hello()  # Output: hello
```

### Parameters and Default Values
Functions can accept parameters inside their parentheses:

```python
# Using a parameter
def hello(to):
    print(f"Hello, {to}")

name = input("Enter your name: ")
hello(name)
```

You can also assign a **default value** to a parameter so it runs even if no argument is passed:

```python
def hello(to="World"):
    print(f"Hello, {to}")

hello()         # Output: Hello, World
hello("Leyon")  # Output: Hello, Leyon
```

---

### Structure and Execution Order (`main()`)

Python reads scripts from top to bottom. Calling a custom function before defining it raises a `NameError`:

```python
# Raises NameError: name 'hello' is not defined
hello()

def hello():
    print("Hello, World")
```

To structure programs cleanly without worrying about definition order, place your core program logic inside a `main()` function and call `main()` at the bottom:

```python
def main():
    name = input("Enter your name: ")
    hello(name)

def hello(to="World"):
    print(f"Hello, {to}")

main()
```

---

### Variable Scope

**Scope** refers to the context in which a variable exists. A variable defined inside a function is local to that function and cannot be accessed outside of it:

```python
def main():
    name = input("Enter your name: ")
    hello()

def hello():
    # Raises NameError: name 'name' is not defined
    print(f"Hello, {name}")

main()
```
*Because `name` was initialized inside `main()`, `hello()` has no access to it unless it is passed explicitly as an argument.*

---

### Return Values (`return`)

Functions can perform a **side effect** (like printing directly to the terminal) or hand back a **return value** for the caller to use:

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()
```
*Using `return` makes functions modular and reusable, allowing their results to be stored in variables, passed into other functions, or used in further calculations.*
