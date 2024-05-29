print("-------------------BIENVENIDOS A BURGER KING -------------")
nombre=input("Ingrese su Nombre:")
cedula=int(input("Ingrese su Numero de Cedula:"))
correo=input("Igrese su Correo Electronico:")
N_hamburguesas=int(input("Ingrese el numero de hamburguesas que desa adquirir:"))

print("Ingrese uno de los siguientes tipos de Haburguesas:")
print("1) sencilla")
print("2) Doble")
print("3) Triple")

t_hamburguesa=int(input("Ingrese la opción:"))
if t_hamburguesa==1 or t_hamburguesa==2 or t_hamburguesa==3:
    match t_hamburguesa:
        case 1:
            precio=N_hamburguesas*1.50
        case 2:
            precio=N_hamburguesas*2.50
        case 3:
            precio=N_hamburguesas*3.50
    print("Ingrese Forma de Pago:")
    print("1) Tarjeta de Crédito")
    print("2) Efectivo")
    t_tarjeta=int(input("Ingrese la opción:"))
    if t_tarjeta==1 or t_tarjeta==2:
        match t_tarjeta:
            case 1:
                recargo=precio*0.05
                pf=precio+recargo
                print(f"Genia,{nombre} el precio final es{round(pf,2)}")
                print(f"La factura se enviara a su corre{nombre},{correo}") 
            case 2:
                pf=precio*1
                print(f"Genial,{nombre} el precio final es{round(pf,2)}")
                print(f"La factura se enviara a su correo {nombre},{correo}")
    else:
         print("No existe esta forma de pago")
         print("Muchas Gracias")
else:
    print("Este tipo de haburguesa no existe")
    print("Muchas Gracias")
