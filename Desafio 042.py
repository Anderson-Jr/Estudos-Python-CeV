from emoji import emojize
a = float(input('Enter the value of the first side of the triangle: '))
b = float(input('Enter the value of the second side of the triangle: '))
c = float(input('Enter the value of the third side of the triangle: '))
if a + b > c and a + c > b and b + c > a:
    print(emojize('It is a possible triangle! :small_red_triangle:', use_aliases=True))
    if a == b == c:
        print('It is a equilateral triangle')
    elif a != b and b != c and c != a:
        print('It is a scalene triangle')
    else:
        print('It is a isosceles triangle!')
else:
    print('It is not a possible triangle!')
