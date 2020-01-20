print('Calculate your body mass index')
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))
bmi = weight / height * height
if bmi < 18.5:
    print('You are under weight!')
elif bmi < 25:
    print('You are at the ideal weight!')
elif bmi < 30:
    print('You are overweight!')
elif bmi < 40:
    print('You are obese!')
else:
    print('You are morbidly obese!')