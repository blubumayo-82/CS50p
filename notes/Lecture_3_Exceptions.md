# Exceptions

Defensive programming means anticipating that users will provide unexpected input or trigger edge cases, and handling those failures gracefully rather than letting the program crash.

---

## 1. Types of Errors

### SyntaxError
Occurs when code violates Python's grammatical rules. Python detects this during parsing **before** running the code.

```python
print("Hello, World)
```
* **Cause:** Missing closing quotation mark.
* **Fix:** Correct the typo in your source code.

### Runtime Errors
Occurs **while the program is running** due to unexpected behavior or invalid inputs:

```python
x = int(input("What's x? "))
print(f"x is {x}")
```
* If the user enters `"cat"`, `int()` cannot convert the string to a base-10 integer.
* **Result:** `ValueError: invalid literal for int() with base 10: 'cat'`.

---

## 2. Handling Errors: `try` and `except`

Use `try` and `except` to intercept runtime errors before they crash the application.

```python
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

### Best Practice: Scope of `try`
Only wrap the **fewest lines of code possible** that could reasonably fail. Having too many statements inside `try` makes debugging harder.

---

## 3. The `NameError` Trap

Attempting to tighten the `try` block prematurely can create a variable scoping problem:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```

* **Why it raises `NameError`:**
  * Assignment happens **right-to-left**: `int(input(...))` is evaluated *before* storing anything into `x`.
  * If `int()` raises a `ValueError`, the assignment to `x` never takes place.
  * When Python reaches `print(f"x is {x}")`, `x` does not exist in memory, triggering:  
    `NameError: name 'x' is not defined`.

---

## 4. The `else` Block

The `else` block executes **only if no exceptions occurred** inside the preceding `try` block.

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

* If `int(...)` raises `ValueError` $\rightarrow$ enters `except`, skips `else`.
* If `int(...)` succeeds $\rightarrow$ skips `except`, executes `else`.

---

## 5. Defensive Re-prompting with `while True`

To prevent the program from ending on bad input, wrap the input flow in an infinite loop:

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```

---

## 6. Functional Decomposition: Iterative Refactoring

### Step A: Returning after `break`
```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()
```

### Step B: Returning inside `else`
`return` automatically breaks the loop and exits the function simultaneously:
```python
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
```

### Step C: Direct evaluation (`return int(...)`)
Evaluation happens inside-out: if `int()` fails, the line aborts before `return` can execute, jumping directly to `except`:
```python
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
```

---

## 7. Silent Failure with `pass`

If you want to reject bad input without printing a warning message, use the `pass` keyword:

```python
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
```
* `pass` acts as an explicit no-op (does nothing), allowing the loop to cycle back quietly.

---

## 8. Reusable Function Design: Dynamic Prompts

Hardcoding strings inside helper functions limits their usefulness. Accept a `prompt` argument instead:

```python
def main():
    x = get_int("What's x? ")
    y = get_int("What's y? ")
    print(f"Sum: {x + y}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
```

---

## 9. Manually Triggering Exceptions (`raise`)

Python also allows developers to deliberately raise exceptions when business rules are violated:

```python
def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                raise ValueError("Number must be greater than zero")
            return n
        except ValueError:
            print("Invalid positive integer")
```