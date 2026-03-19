clientes = {

}

producto = {

}


def register_clients():
    client_id = int(input("Ingrese su ID: "))
    if client_id in clientes:
        print("El ID ya existe")
        return
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")

    clientes[client_id] = {

        "nombre":nombre,
        "correo":correo
    }
    print("¡Registro exitoso!")

def register_product():
    product_id = int(input("Ingrese el ID del producto: ")) 
    name_product = input("Ingrese el nombre del producto: ")  
    unit_price = float(input("Ingrese el precio: "))

    producto[product_id] = (product_id, name_product, unit_price)

    print("¡Registro exitoso!")




def menu_principal():

    while True:
        print("Menu principal")
        print("1. Registro de clientes ")
        print("2. Registro de producto ")
        print("3. Creacion de pedidos ")
        print("4. Consulta de pedidos ")
        print("5. Salir")

        option = int(input("Ingrese la opcion deseada: "))

        if option == 1:
            register_clients()
        if option == 2:
            register_product()




if __name__ == "__main__":
    menu_principal()
