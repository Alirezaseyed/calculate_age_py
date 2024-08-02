# Age Calculator

This repository contains a Python program to calculate the user’s age based on their birth year. The program handles various input errors such as future birth years or non-numeric inputs. It also includes unit tests to ensure the correctness of the age calculation function.

## Overview

The program consists of two main parts:

1. The main program (`improved_calculate_age.py`) which interacts with the user and calculates their age.
2. Unit tests (`improved_test_calculate_age.py`) to verify the functionality of the age calculation.

## Main Program: improved_calculate_age.py

Function: `calculate_age(birth_year)`

```python
import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    if birth_year > current_year:
        raise ValueError("سال تولد نمی‌تواند در آینده باشد!")
    if birth_year <= 0:
        raise ValueError("سال تولد باید یک عدد مثبت باشد!")
    return current_year - birth_year
This function:

	•	Retrieves the current year using the datetime module.
	•	Checks if the birth year is in the future or non-positive and raises a ValueError if so.
	•	Calculates and returns the age by subtracting the birth year from the current year.

Function: age_calculator()

This function continuously prompts the user to enter their birth year and calculates their age. Users can exit the program by typing ‘exit’.



```markdown
```python
def age_calculator():
    """
    Prompt the user for their birth year and calculate their age.

    This function continuously prompts the user to enter their birth year and calculates their age.
    The user can exit the program by entering 'exit'.
    """
    while True:
        user_input = input("Please enter your birth year (or 'exit' to quit): ")  # Prompt for birth year
        if user_input.lower() == 'exit':  # Check if the user wants to exit
            print("Exiting the program.")
            break
        try:
            birth_year = int(user_input)  # Convert input to integer
            age = calculate_age(birth_year)  # Calculate age
            print(f"Your age is {age} years.")
        except ValueError as ve:  # Handle invalid input errors
            print(f"Error: {ve}")
        except Exception as e:  # Handle any other unexpected errors
            print("An unknown error occurred. Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    age_calculator()
```
This function:

	•	Continuously prompts the user to enter their birth year.
	•	Converts the input to an integer and calculates the age using the calculate_age function.
	•	Handles errors for non-numeric input and future birth years.
	•	Allows the user to exit the program by typing ‘exit’.

# Unit Tests: test_age_calculator.py
The unit tests ensure that the calculate_age function behaves correctly for various inputs.

```markdown
```python
import unittest
import datetime

class TestAgeCalculator(unittest.TestCase):
    def test_calculate_age_valid(self):
        self.assertEqual(calculate_age(1990), datetime.datetime.now().year - 1990)

    def test_calculate_age_future(self):
        with self.assertRaises(ValueError):
            calculate_age(datetime.datetime.now().year + 1)

    def test_calculate_age_negative(self):
        with self.assertRaises(ValueError):
            calculate_age(-100)

    def test_calculate_age_zero(self):
        with self.assertRaises(ValueError):
            calculate_age(0)

if __name__ == "__main__":
    unittest.main()
```

These tests:

	•	Verify that the calculate_age function correctly calculates the age for a valid birth year.
	•	Check that a ValueError is raised for a birth year in the future.
	•	Ensure a ValueError is raised for non-positive birth years (negative or zero).



 # Running the Tests

To run the unit tests, execute the following command in the terminal:

```markdown
```bash
python test_age_calculator.py
```

# License

This code is open-source and available under the MIT License.

This code was designed by seddalii.
