
# statement
# Statement of Exercise 6: 
#  Given a current year, create a program that shows me 
# the leap years that will occur in the next 30 years 

def year_check(current_year : int):
    years_to_check = [ current_year + i for i in range(1,31)]
    for x in years_to_check:
        if x % 4 == 0:
            if x % 100 == 0:
                if x % 400 == 0:
                    print(f"{x} is a leap year")
                else:
                    print(f"{x} is not a leap year")
            else:
                print(f"{x} is a leap year")

year_check(2026)





