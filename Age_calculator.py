from datetime import date

current_year = date.today().year
birth_year = int(input("Enter your birth year >> "))

Age = current_year - birth_year

print(f"You are {Age} old. ")
