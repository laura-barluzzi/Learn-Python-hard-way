def BMI_calculator(weight_kg, height_metres):
    BMI = weight_kg/(height_metres**2)
    print "Your body mass index is %.2f" % (BMI)


BMI_calculator(int(raw_input("What's your weight in kg?: ")), float(raw_input("What's your height in metres?: ")))

weight_kg = 60
height_metres = 1.60

BMI_calculator(weight_kg, height_metres)

