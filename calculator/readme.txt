# Calculator App

This is a simple command-line calculator application written in Python. It allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

*   **Addition (+):** Adds two numbers.
*   **Subtraction (-):** Subtracts the second number from the first.
*   **Multiplication (*):** Multiplies two numbers.
*   **Division (/):** Divides the first number by the second. Handles division by zero errors gracefully.

## How to Use

To use the calculator, you need to run the Python script from your terminal.

### Running the Application

1.  **Navigate to the directory:** Open your terminal or command prompt and navigate to the directory where the `calculator.py` (or similar name) file is located.

    ```bash
    cd path/to/calculator/app
    ```

2.  **Execute the script:** Run the script using the Python interpreter.

    ```bash
    python calculator.py
    ```

### Interacting with the Calculator

Once the application is running, it will prompt you to enter the first number, the operator, and then the second number.

**Example Usage:**

```
Enter first number: 10
Enter operator (+, -, *, /): +
Enter second number: 5
Result: 15.0
```

**Another Example (Multiplication):**

```
Enter first number: 7
Enter operator (+, -, *, /): *
Enter second number: 3
Result: 21.0
```

**Division by Zero Handling:**

```
Enter first number: 10
Enter operator (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero!
```

**Invalid Operator Handling:**

```
Enter first number: 5
Enter operator (+, -, *, /): ^
Enter second number: 2
Error: Invalid operator. Please use +, -, *, or /.
```

The calculator will continue to prompt for operations until the program is manually stopped (e.g., by pressing `Ctrl+C`).