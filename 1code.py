# Advent of Code 2019, Day 1
# kaleidoscopica
# https://adventofcode.com/2019/day/1

# Objective: Find the sum of the fuel requirements for all of the modules on the spacecraft


# Define the main function
def main():

    # Initialize an array to hold the puzzle inputs, read in from file
    fuel_storage = []
    # Initialize an array to hold the fuel totals after calculations
    fuel_totals = []
    # Initialize an integer to hold the sum of fuel requirements
    fuel_sum = 0
    
    # Open the file we've stored our puzzle inputs in
    file = open('1inputs.txt', 'r')

    # Read the first line from the file
    line = file.readline()

    # Pass the values from file into our fuel_storage array,
    # as long as an empty string was not returned from readline
    while line != '':
        amount = int(line)
        fuel_storage.append(amount)
        line = file.readline()

    # Close the file
    file.close()

    # Call the calculate_fuel function to perform calculations
    calculate_fuel(fuel_storage, fuel_totals)

    # Iterate through the values the calculate_fuel function stored
    # in fuel_totals, to tally their total as the sum of fuel requirements
    for item in fuel_totals:
        fuel_sum += item

    # Printing this value shows us the sum of fuel requirements
    # I.e. it's the answer to Day 1, Part 1
    print(fuel_sum)


# Defines the calculate_fuel function
# This function calculates the amount of fuel necessary to launch
# a model by taking its mass as input, and performing some operations
def calculate_fuel(fuel_storage, fuel_totals):

    # Initialize a variable to store our values in while performing operations
    value = 0

    # Iterate through the array and perform calculations
    for item in fuel_storage:
        # Perform calculations
        # Divide by 3 and round down
        value = int(item / 3)

        # Subtract 2 from the previous value
        value -= 2
	
        # Append fuel value to fuel_totals array
        fuel_totals.append(value)


# Call the main function
main()
