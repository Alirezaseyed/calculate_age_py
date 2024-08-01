# Age Calculator

This repository contains a Python program to calculate the user’s age based on their birth year. The program handles various input errors such as future birth years or non-numeric inputs. It also includes unit tests to ensure the correctness of the age calculation function.

##Overview

The program consists of two main parts:

	1.	The main program (age_calculator.py) which interacts with the user and calculates their age.
	2.	Unit tests (test_age_calculator.py) to verify the functionality of the age calculation.


 ##Main Program: age_calculator.py

Function: calculate_age(birth_year)

This function calculates the user’s age based on their birth year.


### Python
```markdown
```python
import datetime

def calculate_age(birth_year):
    """
    Calculate age based on birth year.

    Args:
        birth_year (int): Year of birth.

    Returns:
        int: Current age.

    Raises:
        ValueError: If the birth year is in the future or not positive.
    """
    current_year = datetime.datetime.now().year  # Get the current year
    if birth_year > current_year:  # Check if the birth year is in the future
        raise ValueError("Birth year cannot be in the future!")
    if birth_year <= 0:  # Check if the birth year is positive
        raise ValueError("Birth year must be a positive number!")
    return current_year - birth_year  # Calculate and return age





