# The program greets user and describes what's the purpose of the program.
print("Welcome to the Unit Converter. Here you can convert kilometres into miles.")

# The program asks user to enter number of kilometers.
# User enters the amount of kilometers
while True:
    km = float(input("Please, enter a number of kilometers you wish to convert into miles: "))

    conversion_factor = 0.621371
    miles = km * conversion_factor

#The program converts these kilometers into miles and prints them.
    print("The conversion of " + str(km) + " kilometers into miles is: " + str(miles) + " miles.")

# The program asks user if s/he'd want to do another conversion.
    choice = input("Do you want to do another conversion? Yes/No ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break















