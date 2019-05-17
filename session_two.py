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

length_from_input = float(input('Enter length'))
width_from_input = float(input('Enter width'))
area_from_user = length_from_input * width_from_input
print('The area of the squared room of length', length_from_input, 'and width' , width_from_input, 'is', area_from_user)

# computing Loan payment
# Exercice 4

annual_interest_rate = float(input('Enter annual interest rate: '))
monthly_interest_rate  = annual_interest_rate / 1200

number_of_years = float(input('Enter number of years as an integer: '))

loan_amount = float(input('Enter loan amount: '))

monthly_payment = loan_amount * monthly_interest_rate / (1
  - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))
total_payment = monthly_payment * number_of_years * 12


print('The monthly payment is' + str(int(monthly_payment * 100) / 100))
print('The total payment is' + str(int(total_payment * 100) /100))

# Password check
# Exercice 5

password = 'ILoveCats'
login = 'ChubbyCat01'

user_login = input('login?')
user_password = input('password?')

if login == str(user_login) and password == str(user_password):
	print('Acces granted')
else :
	print('Denied')

# Check number divisor
# Exercice 6

user_number = input('Please enter a number:')

if int(user_number)% 5  == 0 :
	print('HiFive')
elif int(user_number)% 2 == 0 :
	print('hiEven')
else:
	print('nop')

# Grading Students
# Exercice 7

student_grade = input('Enter student grade')

if student_grade >= 90:
	print('A')
elif student_grade < 90 and student_grade >= 80:
	print('B')
elif student_grade < 80 and student_grade >= 70:
	print('C')
elif student_grade < 70 and student_grade >= 60:
	print('D')
elif student_grade < 60:
	print('D')
else:
	print('impossible value')

# Determining leap year
# Exercice 8

user_input_year = input('please input year?')
year = int(user_input_year)
leap_year = False
if year % 400 == 0:
    leap_year = True
elif year % 4 == 0:
	if year % 100 != 0:
         leap_year = True
else:
    leap_year = False

if leap_year:
    print("The year entered is a leap year.")
else:
    print("The year entered is not a leap year.")

# Determining Zodic Sign
# # Exercice 8

user_sign_input = input('please your year of birth?')
zodiacYear = user_sign_input % 12
if zodiacYear == 0:
    print("monkey")
elif zodiacYear == 1:
    print("rooster")
elif zodiacYear == 2:
    print("dog")
elif zodiacYear == 3:
    print("pig")
elif zodiacYear == 4:
    print("rat")
elif zodiacYear == 5:
    print("ox")
elif zodiacYear == 6:
    print("tiger")
elif zodiacYear == 7:
    print("rabbit")
elif zodiacYear == 8:
    print("dragon")
elif zodiacYear == 9:
    print("snake")
elif zodiacYear == 10:
    print("horse")
else:
    print("sheep")




