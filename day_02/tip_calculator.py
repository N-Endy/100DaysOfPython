# Program that calculates how much each person pays plus tip

# Get total amount
    # Use input and convert to float
# Get number of peoople to share bill
    # Use input and convert to int
# Get percentage of tip
    # Use input and convert to int
    # Divide by 100
# Calculate each amount
    # Tip is bill plus percentage
    # Total is bill plus tip
    # Individual amount is total divided by number of persons
# Round to 1 decimal place


print("Welcome to the tip calculator")
bill = float(input("What is the total bill?: $"))
num_of_person = int(input("How many people to split the bill?: "))
percent_tip = int(input("What percent tip woul you like to give? 10, 12, or 15?: ")) / 100
# Calculate total bill plus tip
total_bill = (bill + (bill * percent_tip))
# Get amount for each person
split_amount = round((total_bill / num_of_person), 1)
print(f"Each person should pay: ${split_amount}")
