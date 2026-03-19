clientes = {

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

    ti = (product_id, name_product, unit_price)

    print(ti)


def creation():
