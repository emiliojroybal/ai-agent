# Calculator Script Explanation and Usage

This document provides a detailed explanation of the calculator script and instructions on how to use it.

## How the Calculator is Scripted

The calculator application is primarily composed of two Python files: `main.py` and `pkg/calculator.py`.

### `main.py`

This file serves as the entry point for the calculator application.

-   **Imports**: It imports the `Calculator` class from `pkg.calculator` and a utility function `format_json_output` from `pkg.render` (though `pkg/render.py` content was not provided, its purpose can be inferred).
-   **Command-line Argument Handling**:
    -   When `main.py` is executed, it checks if any command-line arguments are provided.
    -   If no arguments (meaning no expression to evaluate) are given, it prints a usage message demonstrating how to run the calculator.
    -   If arguments are present, it concatenates them to form the `expression` string.
-   **Expression Evaluation**:
    -   An instance of the `Calculator` class is created.
    -   The `evaluate` method of this `Calculator` instance is called with the user-provided `expression`.
    -   It handles potential `None` returns from `evaluate` (indicating an empty or whitespace-only expression) and prints an appropriate error.
    -   If a valid result is obtained, it uses `format_json_output` to present the expression and its result in a structured (presumably JSON) format.
-   **Error Handling**: A `try-except` block is used to catch and print any general exceptions that might occur during the evaluation process.

### `pkg/calculator.py`

This file contains the core logic for evaluating arithmetic expressions through the `Calculator` class.

-   **`Calculator` Class**:
    -   **`__init__(self)`**:
        -   Initializes `self.operators`: A dictionary mapping operator symbols (`+`, `-`, `*`, `/`) to lambda functions that perform the respective arithmetic operations.
        -   Initializes `self.precedence`: A dictionary defining the precedence level of each operator. Higher numbers indicate higher precedence (e.g., multiplication and division have higher precedence than addition and subtraction).
    -   **`evaluate(self, expression)`**:
        -   This is the public method called by `main.py` to start the evaluation process.
        -   It first checks if the `expression` is empty or consists only of whitespace. If so, it returns `None`.
        -   It then `strip()`s leading/trailing whitespace and `split()`s the expression into `tokens` (e.g., "3 + 5" becomes `['3', '+', '5']`).
        -   It calls the private method `_evaluate_infix` to handle the actual evaluation of these tokens.
    -   **`_evaluate_infix(self, tokens)`**:
        -   This method implements a variant of the Shunting-yard algorithm to evaluate infix expressions.
        -   It uses two lists: `values` to store numerical operands and `operators` to store operator symbols.
        -   It iterates through each `token` in the input list:
            -   **If the token is an operator**: It compares its precedence with the operator at the top of the `operators` stack. If the operator on the stack has higher or equal precedence, it applies that operator (`_apply_operator`) before pushing the current token onto the `operators` stack.
            -   **If the token is a number**: It attempts to convert the token to a `float` and pushes it onto the `values` stack. A `ValueError` is raised if the token cannot be converted.
        -   After processing all tokens, any remaining operators in the `operators` stack are applied to the `values` stack.
        -   Finally, it asserts that only one value (the result) remains in the `values` stack; otherwise, it raises a `ValueError` for an invalid expression.
        -   The single remaining value is returned as the result.
    -   **`_apply_operator(self, operators, values)`**:
        -   This is a helper method used by `_evaluate_infix` to perform an arithmetic operation.
        -   It pops an operator from the `operators` stack.
        -   It pops the two most recent operands (`b` then `a`) from the `values` stack.
        -   It performs the operation using the stored lambda function for the popped operator (`self.operators[operator](a, b)`).
        -   The result of the operation is pushed back onto the `values` stack.
        -   It includes checks to ensure there are enough operands available before attempting an operation.

## How to Use the Calculator

To use the calculator, you need to execute the `main.py` script from your terminal and provide the arithmetic expression as a command-line argument.

**Basic Usage:**

```bash
python main.py "<expression>"
```

**Example:**

To calculate "3 + 5", you would run:

```bash
python main.py "3 + 5"
```

**Supported Operators:**

The calculator supports the following basic arithmetic operators:

-   `+` (Addition)
-   `-` (Subtraction)
-   `*` (Multiplication)
-   `/` (Division)

**Output:**

The script will print the result of the evaluation, typically in a JSON format (as inferred from `format_json_output` in `main.py`).

**Example Output (for `python main.py "3 + 5"`):**

```json
{"expression": "3 + 5", "result": 8.0}
```

(Note: The exact JSON format might vary slightly based on the `pkg/render.py` implementation.)

**Error Handling:**

-   If you run the script without an expression, it will print usage instructions.
-   If the expression is invalid (e.g., contains unknown tokens, has mismatched operators/operands), it will print an error message.