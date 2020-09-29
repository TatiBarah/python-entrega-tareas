# Se busca que el programa permita agregar tantos clientes como sea necesario, además de imprimir el costo acumulado hasta el momento

listaRegistro = []
respuesta = input("¿Deseas agregar al primer cliente? (Sí o No): ")
costoTotal = 0.0

# Bucle para agregar clientes e imprimir el costo total hasta el momento
while respuesta == "Sí":
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    costo = input("Costo ($0.00): ")
    costo = float(costo)
    registro = {"cliente": cliente, "producto": producto, "costo": costo}
    listaRegistro.append(registro)
    costoTotal += costo
    print("")
    print("El costo total de los productos registrados es: $" + str(costoTotal))
    print("")
    respuesta = input("¿Deseas seguir agregando clientes? (Sí o No): ")
    print("")

# Imprimir todos los registros y el costo al finalizar el ingreso de datos si la respuesta es no
if respuesta == "No":
    print("Los registros son:")
    for registro in listaRegistro:
        print(registro)
    print("El costo total es $" + str(costoTotal))
# Si ingresa una respuesta que no sea aceptada, dar un mensaje de error
else:
    print("Has introducido una respuesta equivocada")
