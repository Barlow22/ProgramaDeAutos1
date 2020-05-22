def precioMarca(marca):
    if marca == 'ford':
        return 100000
    elif marca == 'chevrolet':
        return 120000
    elif marca == 'fiat':
        return  80000
def precioPuertas(puertas):
    if puertas == '2':
        return 50000
    elif puertas == '4':
        return 65000
    elif puertas == '5':
        return  78000
def precioColor(color):
    if color == 'blanco':
        return 10000
    elif color == 'azul':
        return 20000
    elif color == 'negro':
        return  30000
clientes = 0
while clientes < 5:

#Pedir nombre y apellido del cliente
    nombreCliente = input('Ingrese su nombre y apellido: ')
#Consultar marca, puertas y color
    marca = input('Elija su marca: Ford, Chevrolet o Fiat. ').lower()
    puertas = input('¿Cuantas puertas queres? 2, 4, o 5. ')
    color = input('Por ultimo ¿que color te gustaria? Blanco, azul o negro. ').lower()
    precioDeMarca = precioMarca(marca)
    precioDePuertas = precioPuertas(puertas)
    precioDeColor = precioColor(color)

#imprimir datos de cada compra y el precio total
    precioTotal = precioDeMarca + precioDePuertas + precioDeColor
    print('Nombre Comprador: ' + nombreCliente + '\n' + 'Precio total de compra: $' + str(precioTotal))
    clientes += 1


