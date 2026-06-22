# Ethan Scoggan
# June 21 2026
# P1HW1 - Math Expressions
# This program takes user inputs to perform exponentiation, addition, and subtraction calculations.

print("-----Calculating Exponents-----")
print()  

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print()  

exponent_result = base ** exponent

print(f"{base} raised to the power of {exponent} is {exponent_result} !!")
print()  


print("-----Addition and Subtraction-----")
print()  

starting_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))
print()  

final_total = starting_num + add_num - sub_num

print(f"{starting_num} + {add_num} - {sub_num} is equal to {final_total}")