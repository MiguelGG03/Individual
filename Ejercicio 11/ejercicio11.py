def inf(a,b):
    if(a<b):
        return a
    else:
        return b

def sup(a,b):
    if(a>b):
        return a
    else:
        return b

c_semanas=52
c_horas_s=35
c_horas_m_1=8
precio_h1=1.25
precio_h2=1.5
salario_m=float(input('Salario mensual:'))
h_extra=int(input('Cuantas horas extra:'))
precio_h=salario_m/(c_horas_s*4)
resultado=precio_h*(inf(h_extra,c_horas_m_1)*precio_h1+sup(h_extra-c_horas_m_1,0)*precio_h2)
print('El pago por horas extras es '+str(resultado))