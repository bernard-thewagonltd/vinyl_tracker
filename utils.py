import os
from datetime import datetime

def clear_screen():
    # Clear the screen
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')


def validate_year(year_str):
    # Validate that year is a 4-digit number between 1900 and the current year + 1
    current_year = datetime.now().year
    max_year = current_year + 1  # Allow next year for pre-orders

    try:
        year = int(year_str)
        if year < 1900:
            return False, None, f"Year must be 1900 or later (got {year})"
        elif year > max_year:
            return False, None, f"Year cannot be later than {max_year} (got {year})"
        else:
            return True, str(year), None
    except ValueError:
        return False, None, f"Year must be a valid number (got '{year_str}')"


def get_valid_year(prompt="Year: ", current_value=None):
    # Prompt user for a valid year with validation
    while True:
        if current_value:
            user_input = input(f"{prompt}[{current_value}]: ").strip()
            if not user_input:  # Keep current value
                return current_value
        else:
            user_input = input(prompt).strip()
            if not user_input:
                print("Year is required.")
                continue

        is_valid, year_value, error_msg = validate_year(user_input)
        if is_valid:
            return year_value
        else:
            print(f"Invalid year: {error_msg}")
            print("Please try again.")


def validate_trackcount(trackcount_str):
    # Validate that track count is a positive integer
    try:
        trackcount = int(trackcount_str)
        if trackcount <= 0:
            return False, None, f"Track count must be greater than 0 (got {trackcount})"
        elif trackcount > 999:
            return False, None, f"Track count seems unrealistic (got {trackcount})"
        else:
            return True, trackcount, None
    except ValueError:
        return False, None, f"Track count must be a valid number (got '{trackcount_str}')"


def get_valid_trackcount(prompt="Number of tracks: ", current_value=None):
    # Prompt user for a valid track count with validation
    while True:
        if current_value:
            user_input = input(f"{prompt}[{current_value}]: ").strip()
            if not user_input:  # Keep current value
                return current_value
        else:
            user_input = input(prompt).strip()
            if not user_input:
                print("Track count is required.")
                continue

        is_valid, trackcount_value, error_msg = validate_trackcount(user_input)
        if is_valid:
            return trackcount_value
        else:
            print(f"Invalid track count: {error_msg}")
            print("Please try again.")


def validate_non_empty_string(value, field_name):
    # Validate that a string is non-empty and not too long
    cleaned = value.strip()
    if not cleaned:
        return False, None, f"{field_name} cannot be empty"
    elif len(cleaned) > 200:
        return False, None, f"{field_name} is too long (max 200 characters)"
    else:
        return True, cleaned, None


def get_valid_string(prompt, field_name, current_value=None):
    # Prompt user for a valid string with validation
    while True:
        if current_value:
            user_input = input(f"{prompt}[{current_value.title()}]: ").strip()
            if not user_input:  # Keep current value
                return current_value
        else:
            user_input = input(prompt).strip()

        is_valid, cleaned_value, error_msg = validate_non_empty_string(user_input, field_name)
        if is_valid:
            return cleaned_value
        else:
            if current_value and not user_input:
                # If they pressed enter with a current value, keep it
                return current_value
            print(f"Invalid input: {error_msg}")
            print("Please try again.")


def validate_date(date_str):
    # Validate that date is in YYYY-MM-DD format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True, date_str, None
    except ValueError:
        return False, None, f"Date must be in YYYY-MM-DD format (got '{date_str}')"

