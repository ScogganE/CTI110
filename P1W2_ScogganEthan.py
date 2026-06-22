# Ethan Scoggan
# June 21, 2026
# P1HW2 - Travel Expenses
# This program calculates and displays travel expenses by taking a user's budget, destination, and estimated spending for gas, accomodation, and food.

# Pseudocode:
# 1. Print program title: "This program calculates and displays travel expenses"
# 2. Input: Prompt user for budget (integer)
# 3. Input: Prompt user for travel destination (string)
# 4. Input: Prompt user for gas expense (integer)
# 5. Input: Prompt user for accomodation expense (integer)
# 6. Input: Prompt user for food expense (integer)
# 7. Calculate: Sum all expenses (gas + accomodation + food)
# 8. Calculate: Subtract total expenses from budget to get remaining balance
# 9. Output: Print header "------------Travel Expenses------------"
# 10. Output: Print Location, Initial Budget, Fuel, Accomodation, Food, and Remaining Balance

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
print()

gas = int(input("How much do you think you will spend on gas? "))
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
print()

total_expenses = gas + accomodation + food
remaining_balance = budget - total_expenses

print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accomodation: {accomodation}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remaining_balance}")