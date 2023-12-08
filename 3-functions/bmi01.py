#!/usr/bin/python3

"""Calculate BMI (m = height, kg = weight)"""

# define the function
def bmi_calc(weight, height):
    bmi = weight // (height ** 2)
    return (bmi)

# call the function
Brendon = bmi_calc(55, 1.76)
Tom = bmi_calc(55, 1.60)

if Brendon > Tom:
    print("Brendon's bmi is heavier than Tom's")
else:
    print("Tom's bmi is heavier than Brendon's")
