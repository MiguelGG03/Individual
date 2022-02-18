class cuenta:
    saldo = 0
    def __init__(self, nombre):
        self.nombre=nombre

    @classmethod
    def abrir(c,saldo_inicial):
        c.saldo=saldo_inicial
    def abonar(c,credito):
        c.saldo=c.saldo+credito
    def cargar(c,debito):
        c.saldo=c.saldo-debito
    def consultar(c):
        return c.saldo
    def es_acreedora(c):
        return (c.saldo>=0)
    def es_deudora(c):
        return (c.saldo<0)

n=str(input('Nombre de la cuenta:'))
c1 = cuenta(n)
print(c1.consultar())      
c1.abrir(10000)
print(c1.consultar())
c1.abonar(100)
print(c1.consultar())
c1.cargar(500)
print(c1.consultar())
if(c1.es_acreedora()):
    print(c1.nombre+' es acreedora')
c1.cargar(10000)
print(c1.consultar())
if(c1.es_deudora()):
    print(c1.nombre+' es deudora')