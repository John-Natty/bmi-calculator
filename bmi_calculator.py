#!/usr/bin/env python3
"""A simple BMI calculator for beginners."""


def get_category(bmi):
    """Return a simple health category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity"


try:
    # Ask the user for their weight.
    weight = float(input("Enter your weight in kilograms: "))

    # Ask the user for their height.
    height = float(input("Enter your height in meters: "))

    # Weight and height must be positive numbers.
    if weight <= 0 or height <= 0:
        print("Please enter numbers greater than 0.")
    else:
        # Calculate BMI using the standard formula.
        bmi = weight / (height * height)

        # Find the health category for this BMI.
        category = get_category(bmi)

        # Print the BMI rounded to 2 decimals.
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Health category: {category}")

except ValueError:
    # This runs if the user types something that is not a number.
    print("Invalid input. Please enter numbers only, like 70 or 1.75.")
