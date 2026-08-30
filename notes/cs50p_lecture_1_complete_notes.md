# CS50P: Lecture Notes & Setup Guide

---

## Lecture 1: Conditionals

Conditionals allow programs to make decisions by executing specific blocks of code depending on whether a given condition is true or false.

### Comparison Operators

Python supports standard comparison operators that evaluate to a **Boolean** (`True` or `False`):

* `>` Greater than
* `>=` Greater than or equal to
* `<` Less than
* `<=` Less than or equal to
* `==` Equal to
* `!=` Not equal to

---

### `if`, `elif`, and `else`

An `if` statement evaluates a Boolean expression. If the expression evaluates to `True`, its indented block runs:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
```

Using three separate `if` statements forces Python to evaluate all three conditions every single time, even if the first condition is already `True`.

To create mutually exclusive branches and avoid unnecessary checks, use `elif` (else if):

```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
```

If `x < y` is `True`, Python skips the remaining `elif` checks. Furthermore, if `x` is neither less than nor greater than `y`, it must be equal. You can simplify this using a final `else` catch-all:

```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

---

### Logical Operators: `or` and `and`

#### Using `or`
The `or` keyword evaluates to `True` if **at least one** condition is true:

```python
if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```

Instead of testing both `<` and `>`, simplify using the `!=` (not equal) operator:

```python
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```

Or test for equality first:

```python
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
```

#### Using `and`
The `and` keyword evaluates to `True` only if **both** conditions are true:

```python
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```

Python supports chained comparisons (similar to standard mathematical notation):

```python
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```

Because `elif` blocks only evaluate if preceding conditions failed, you can simplify the logic even further:

```python
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```
*If `score` is not $\ge 90$, the program checks if it is $\ge 80$, meaning values $90$ and above have already been ruled out.*

---

### Modulo Operator and Pythonic Functions

The modulo operator `%` calculates the remainder of a division. It is often used to check parity (even vs. odd):

```python
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

To make this check reusable, encapsulate it inside a helper function:

```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
```

#### Writing Pythonic Code
**Pythonic** refers to writing idiomatic Python that leverages the language's distinct features cleanly.

1. **Ternary Operator (Conditional Expression):**
```python
def is_even(n):
    return True if n % 2 == 0 else False
```

2. **Direct Boolean Evaluation (Most Elegant):**
Because `n % 2 == 0` is already a Boolean expression that evaluates to `True` or `False`, you can return it directly:

```python
def is_even(n):
    return n % 2 == 0
```

---

### `match` Statements

Python 3.10 introduced `match` statements, which function similarly to `switch` statements in other languages.

Instead of writing repetitive `elif` chains:

```python
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

Use `match` and `case` with the pipe operator `|` (acting as `or`) to combine cases, and `_` as a catch-all default case:

```python
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```