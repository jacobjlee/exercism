## Installation
1. Clone the repository
2. Navigate to the `python` directory
3. Create a virtual environment and activate it
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
4. Install Dependencies from requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

<br/>

## Usage
To test the project using pytest, follow these steps:

1. Navigate to the `python` directory
2. Run pytest to execute all test cases:
    ```bash
    pytest
    ```

    This command will automatically discover and execute all test files in the current directory and its subdirectories.

3. If you want to test a file from a specific directory, you can specify it as an argument to pytest. For example, to test files from the `specific-directory`, run:
    ```bash
    pytest specific-directory
    ```
