print("This program converts temperatures from Celsius to Fahrenheit.")

score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))
average = (score1 + score2 + score3) / 3
print("The average score is:", average)

for _ in range(5):
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is {fahrenheit}F")

print("Celsius to Fahrenheit Conversion Table")
print("Celsius\tFahrenheit")
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}\t{fahrenheit}")

# Get user input
principal = float(input("Enter the amount to invest: "))
rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
years = int(input("Enter the number of years: "))

# Calculate future value
future_value = principal * (1 + rate) ** years

# Print result
print(f"After {years} years, your investment will be worth: ${future_value:.2f}")

# Get user input
annual_investment = float(input("Enter the amount to invest each year: "))
rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
years = int(input("Enter the number of years: "))

# Calculate total accumulation
total_amount = 0
for year in range(years):
    total_amount = (total_amount + annual_investment) * (1 + rate)

# Print result
print(f"After {years} years, your total accumulation will be: ${total_amount:.2f}")

# Get user input
principal = float(input("Enter the initial investment amount: "))
rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
periods = int(input("Enter the number of times interest is compounded per year: "))
years = 10

# Calculate future value with compounding
future_value = principal
for _ in range(years * periods):
    future_value *= (1 + rate / periods)

# Print result
print(f"After {years} years, your investment will be worth: ${future_value:.2f}")

# Get user input
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is {celsius:.2f}°C.")

# Get user input
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.62
print(f"{kilometers} kilometers is approximately {miles:.2f} miles.")

print("This program converts pounds to kilograms.")
# Get user input
pounds = float(input("Enter weight in pounds: "))
kilograms = pounds * 0.453592
print(f"{pounds} pounds is approximately {kilograms:.2f} kilograms.")

print("Welcome to the interactive calculator! Type 'exit' to quit.")

while True:
    expression = input("Enter a mathematical expression: ")
    if expression.lower() == 'exit':
        break
    try:
        result = eval(expression)
        print(f"The result is: {result}")
    except Exception as e:
        print("Invalid expression. Please try again.")
