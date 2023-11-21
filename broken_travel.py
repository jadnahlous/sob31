# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))  # I added ( instead of '.' and then replaced ' with "

if year <= 1900:  # added :
    print("Woah, that's the past!")  # replaced ' with "
elif 1900 <= year <= 2020:  # replaced && with putting year between 1900 and 2020 else we could have also put and
    #  in addition, I added = so whenever it is 1900 or 2020 it would still print out the same values
    print("That's totally the present!")
else:  # replaced elif with else
    print("Far out, that's the future!!")
