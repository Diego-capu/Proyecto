# Our "database" using dictionaries
clientes = {}     # id → {name, email}
productos = {}    # id → (id, name, price)
pedidos = {}      # order_id → {client_id, product_id, quantity, total}

def register_client(c_id, name, email):
    return {
        "nombre": name,
        "correo": email
    }

def register_product(p_id, name, price):
    return (p_id, name, price)

def create_order(c_id, p_id, quantity):
    product = productos[p_id]
    unit_price = product[2]             # price is the 3rd item
    total = unit_price * quantity
    
    return {
        "client_id": c_id,
        "product_id": p_id,
        "quantity": quantity,
        "total": total
    }

def orders():
    if not pedidos:
        return "No orders yet."
    
    report = ""
    for order_id, order in pedidos.items():
        client_name = clientes[order["client_id"]]["nombre"]
        product_name = productos[order["product_id"]][1]   # name is 2nd item
        report += f"Order #{order_id} | Client: {client_name} | Product: {product_name} | Total: ${order['total']}\n"
    
    return report

def calculate_total():
    total = 0.0
    for order in pedidos.values():
        total += order["total"]
    return total

def menu_principal():                   #main menu
    while True:
        print("\n--- Order Management System ---")  #shows the available options
        print("1. Register client")
        print("2. Register product")
        print("3. Create order")
        print("4. View orders")
        print("5. Final report & Exit")

        choice = input("Choose an option: ")

        if choice == "1":     #register the clients
            cid = int(input("Client ID: "))   
            if cid in clientes:
                print("ID already exists.")
            else:
                name = input("Name: ")
                email = input("Email: ")
                clientes[cid] = register_client(cid, name, email)
                print("Client added")

        elif choice == "2":       #resgister the product
            pid = int(input("Product ID: "))
            name = input("Product name: ")
            price = float(input("Price: "))
            productos[pid] = register_product(pid, name, price)
            print("Product added:", productos[pid])

        elif choice == "3":       #create an order
            cid = int(input("Client ID: "))
            pid = int(input("Product ID: "))
            
            if cid in clientes and pid in productos:
                qty = int(input("Quantity: "))
                order_id = len(pedidos) + 1
                pedidos[order_id] = create_order(cid, pid, qty)
                print(f"Order #{order_id} created!")
            else:
                print("Client or product not found.")

        elif choice == "4":   #View the list of orders
            print("\n ORDERS LIST:")
            print(orders())

        elif choice == "5":    #Show the total report for the day
            total_money = calculate_total()
            print("\n FINAL REPORT:")
            print(f"Total orders: {len(pedidos)}")
            print(f"Total income: ${total_money}")
            print("Goodbye!")
            break

if __name__ == "__main__": #initializer
    menu_principal()
