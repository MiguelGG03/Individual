ci=float(input('Capital inicial:'))
t=int(input('Periodo en meses:'))
interes=float(input('Porcentaje de interes mensual(xx.xx...)%:'))
i=interes/100
interes_f=(ci*(1+i)**t)-ci
print('El interes final generado es de '+str(interes_f))