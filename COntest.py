#Chef is interested in the history of SnackDown contests. He needs a program to verify if SnackDown was hosted in a given year.
#SnackDown was hosted by CodeChef in the following years: 2010, 2015, 2016, 2017 and 2019.
year = int(input("Please enter the year"))
contest_years = [2010, 2015, 2016, 2017, 2019]
if year in contest_years:
    print("The contest is held in this year")
else:
    print("The contest is not held in this year")