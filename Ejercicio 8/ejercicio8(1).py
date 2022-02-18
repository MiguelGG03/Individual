importe=float(input('Precio sin impuestos:'))
porcentaje_IVA=0.21
precio=importe*(1+porcentaje_IVA)
print('Precio final es '+str(precio))