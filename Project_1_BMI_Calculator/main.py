print("Welcome to the BMI Calculator!")
# 1st input: enter height in meters e.g: 1.65
height = input("1st input: enter height in meters: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("2nd input: enter weight in kilograms: ")

BMI1 = float(weight)
BMI2 = (float(height)**2)
BMI = BMI1/BMI2
BMI = int(BMI)
print (BMI)
