// Generates a password based on user's first name and birth details.
The symbol changes depending on the birth month entered //


# Password Generator

# Get user input
first_name = input("Enter your first name: ")
birth_year = int(input("Enter your year of birth: "))
birth_month = input("Enter your birth month in words: ")

# Extract first 2 letters of the name in uppercase
name_part = first_name[0:2].upper()

# Normalize month input (lowercase and strip spaces)
birth_month = birth_month.lower().strip()

# Take first 3 letters of month
month_abbr = birth_month[0:3]

# Assign symbol based on month group
if month_abbr in ["jan", "feb", "mar"]:
    symbol = "*"
    print(f'Your password is: {name_part}{symbol}{month_abbr}{birth_year}')

elif month_abbr in ["apr", "may", "jun", "jul", "aug"]:
    symbol = "#"
    print(f'Your password is: {name_part}{symbol}{month_abbr}{birth_year}')

elif month_abbr in ["sep", "oct", "nov", "dec"]:
    symbol = "@"
    print(f'Your password is: {name_part}{symbol}{month_abbr}{birth_year}')

else:
    symbol = "?" #Invalid month
    print(f'{symbol}Invalid month')

