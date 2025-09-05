# rogram to take 2 inputs for day and month and calculate the day of the year.

day = int(input("enter day :"))
month = int(input("enter month :"))

day_of_the_year = ((month-1)*30+day)

print("Day of the year is ",day_of_the_year)