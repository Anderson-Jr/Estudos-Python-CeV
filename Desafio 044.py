price = float(input('What is the price of the product? \nR$'))
print('[1] In cash \n[2] Cash on card \n[3] 2x on card \n[4] 3x or more on more')
option = int(input('What is the option payment? \n'))
if option == 1:
    price = price * 0.9
elif option == 2:
    price = price * 0.95
elif option == 3:
    price = price
elif option == 4:
    price = price * 1.2
print(f'The new price of the product is R${price}')