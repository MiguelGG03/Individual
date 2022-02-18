import math
lado=float(input('Longitud del lado: '))
altura=float(input('Longitud de la altura: '))
c=float(math.sqrt((lado)**2-(altura)**2))
base=2*c
area=(base*altura)/2
print('El area de el triangulo es '+str(area))