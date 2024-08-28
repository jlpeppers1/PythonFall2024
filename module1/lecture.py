# Create variable name set to "Enrico Fermi". 
name = "Enrico Fermi"

print(name)
print(type(name))
# At some point later in the program, set name to a list of integers.
# Valid Python!
name = [3, 4, 5, 6, 7]

print(name)
print(type(name))
print(type(name[0]))

# Snake case compliant variable names. 
capital_of_iowa = "Des Moines"
hours_in_day = 24
days_in_july = 31
eye_for_an_eye = False
dark_side_of_the_moon = 1973

# non-compliant variable names, but will still work.
capitalOfIowa = "Des Moines"
hoursInDay = 25
DaysInJuly = 31
Eye4AnEye = False
DarksideOftheMoon = 1973

a_var = "Joe"
print(f'My name is {a_var}')
#My name is Joe
print("My name is",a_var)
#My name is Joe
print("My","name","is",a_var)
#My name is Joe
print("My" + " " + "name is" + " " + a_var)
#My name is Joe


# How to get user input
input("Please enter your name:")

#How to do something with input
a_name = input("Please enter your name:")
print("Hello " + a_name)

a_age = input("Please enter your age:")
int_a_age = int(a_age)
print("In 5 years you will be " + str(int_a_age + 5))