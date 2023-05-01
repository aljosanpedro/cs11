CURRENT_YEAR = 2023
VALID_YEARS = range(1900,2999,1)


age_now = int(input("Age in 2023: "))
future_year = int(input("Any year from 1900 to 2999: "))


birth_year = CURRENT_YEAR - age_now
future_age = future_year - birth_year 


print()
print(f"Your age in {future_year}: {future_age}")

if birth_year > future_year:
    print(f"You weren't born yet in year {valid_year}")

if future_age > 100:
    print("Magnificent!")
