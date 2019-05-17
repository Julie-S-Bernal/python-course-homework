# Algorythm to python code:
# Exercice 1

miles = 100
kilometers = miles * 1.609
print(kilometers)

# Area of rectangular room
# Exercice 2

length = 3
width = 4
area = length * width
print(area)

# Dynamic Area
# Exercice 3

length_from_input = float(input("Enter length"))
width_from_input = float(input("Enter width"))
area_from_user = length_from_input * width_from_input
print('The area of the squared room of length', length_from_input, 'and width' , width_from_input, 'is', area_from_user)

# computing Loan payment
# Exercice 4

annual_interest_rate = float(input("Enter annual interest rate, e.g., 8.25: "))
monthly_interest_rate  = annual_interest_rate / 1200

number_of_years = float(input("Enter number of years as an integer, e.g., 5: "))

loan_amount = float(input("Enter loan amount, e.g., 120000.95: "))

monthly_payment = loan_amount * monthly_interest_rate / (1
  - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))
total_payment = monthly_payment * number_of_years * 12


print("The monthly payment is " + str(int(monthly_payment * 100) / 100))
print("The total payment is " + str(int(total_payment * 100) /100))

# Password check
# Exercice 5


