# UID-Validation
# UID Validation Program

## Overview

This Python program validates employee Unique Identification Numbers (UIDs). Each employee must be assigned a UID that follows specific rules to ensure its uniqueness and format. The program accepts multiple test cases and checks each UID against the specified criteria, printing Valid if the UID is valid and Invalid otherwise.

## UID Validation Criteria

A valid UID must satisfy the following rules:

1. Length: The UID must contain exactly 10 characters.

2. Alphanumeric Characters Only: The UID should consist only of uppercase lette (A-Z),lowercase letters (a-z), and digits (0-9).

3. At Least Two Uppercase Characters: The UID must contain at least uppercase English alphabet characters.
4. At Least Three Digits: The UID must contain at least 3 digits (0-9).

5. Unique Characters: No character in the UID should repeat.


# Input Format

1. The first line of input contains an integer T, representing the number of test cases.

2. The following T lines contain the UIDs to be validated, one UID per line.


# Output Format

For each test case:

    - Print Valid if the UID meets all the criteria.

    - Print Invalid if the UID does not meet the criteria.

## Example

### Input

`2`

`B1CD102354`

`B1CDEF2354`

### Output

`Invalid`

`Valid`

## Explanation

1. In the first test case (B1CD102354), the UID has a repeated character (1), so it is marked as Invalid.

2. In the second test case (B1CDEF2354), the UID meets all criteria and is marked as Valid.

## How to Run

1. Ensure you have Python 3 installed on your system.

2. Download or copy the Python script into a .py file (e.g., uid_validation.py).

3. Open a terminal or command prompt and navigate to the directory where the script is saved.

4. Run the script using the following command:
   python uid_validation.py

5. The program will prompt for input:
    - First, enter the number of test cases (T).

    - Then, for each test case, input the UID to validate.

6. The program will output Valid or Invalid for each test case based on the validation rules. 