




def register_clients():
    id = int(input("Ingrese su ID: "))
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")

    register = {
        "ID":id,
        "Nombre":nombre,
        "Correo":correo
    }

def register_product():
    product_id = int(input("Ingrese el ID del producto: ")) 
    name_product = input("Ingrese el nombre del producto: ")  
    unit_price = float(input("Ingrese el precio: "))

    ti = (product_id, name_product, unit_price)
