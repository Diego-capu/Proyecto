clientes = {

}

producto = {

}

orders = {

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
    print(f"{producto}")

    print("¡Registro exitoso!")

def order(product_id: int, client_id: int):
    if product_id not in producto:
        return        
                 
    cantidad = int(input("Ingrese la cantidad"))

    price = producto[product_id]       
    total = price * cantidad

    
    
    orders = {
        "client_id": client_id,
        "product_id": product_id,
        "quantity": cantidad,
        "total": total
    }
    

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
        elif option == 2:
            register_product()
        elif option == 3:
            order()

if __name__ == "__main__":
    menu_principal()
