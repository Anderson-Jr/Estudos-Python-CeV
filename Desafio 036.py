house = float(input("What is house value? \nR$"))
salario = float(input("How much money do you get?\nR$"))
years = int(input("How old are do you want to pay?\n"))
mouths = years * 12
prestacao = house / mouths
if prestacao > salario * 0.3:
    print("The loan was denied because of the low salary! ")
    print("You need more money")
    print(f"For the loan be successfully you need earn R${prestacao / 0.3:.2f} monthly")
else:
    print("The loan was approved!")
    print(f"The monthly fee will be R${prestacao:.2f}")
