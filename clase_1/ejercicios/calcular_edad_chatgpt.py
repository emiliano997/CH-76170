from datetime import date

def calculate_age(year_of_birth):
    """
    Calculates the current age of a person given their year of birth.
    
    Parameters:
        year_of_birth (int): The person's year of birth.
    
    Returns:
        int: The person's current age.
    """
    current_year = date.today().year
    return current_year - year_of_birth

# Example usage
year_of_birth = 1996
age = calculate_age(year_of_birth)
print(f"If you were born in {year_of_birth}, your current age is {age} years.")
