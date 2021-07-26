def chart(ind):
    if ind < 18.5:
        print("You are under 'Under Weight'.")
    elif 18.5 < ind < 24.9:
        print("You are under 'Normal Weight'.")
    elif 25.0 < ind < 29.9:
        print("You are under 'Over Weight'.")
    elif 30.0 < ind < 34.9:
        print("You are under 'Obesity Class - 1'.")
    elif 35.0 < ind < 39.9:
        print("You are under 'Obesity Class - 2'.")
    else:
        print("You are under 'Obesity Class - 3'.")


system = input('''
Choose a measurement system:
1. Metric System
2. American System
Choose an option to continue: ''')
print('-----------------------------------------------------------------------------')
print()
if system == '1':
    height_cm = input("Enter height in centimeters (cm): ")
    weight = input("Enter weight in kilograms (kg): ")
    print()
    try:
        height_m = float(height_cm) / 100
        bmi = 1.3 * float(weight) / height_m ** 2.5
        print('Your bmi is %.2f.' % bmi)
        chart(bmi)
        print("\nThank You For Using. BYE!")
    except ValueError:
        print("Error Occurred, Try Again!")
elif system == '2':
    height = input("Enter height in inches (in): ")
    weight = input("Enter weight in pounds (lb): ")
    print()
    try:
        bmi = 5734 * float(weight) / float(height) ** 2.5
        print('Your bmi is %.2f.' % bmi)
        chart(bmi)
        print("\nThank You For Using. BYE!")
    except ValueError:
        print("Error Occurred, Try Again!")
else:
    print("Input Error, Try Again!")
print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")
