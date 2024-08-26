inventario = [{"nombre":"McFlury","precio":2.50, "stock":10}]

def menu_principal():
    """
    Muestra el menú principal 
    """
    while True:
        print("\nMenú Principal")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente otra vez.")

def agregar_producto():
    """
    Agrega un nuevo producto al inventario.
    """
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, ingrese un valor numérico válido para el precio.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, ingrese un valor entero válido para la cantidad.")
    
    producto = {"nombre": nombre, "precio": precio, "stock": cantidad}
    
    inventario.append(producto)
    
    print(f"Producto {nombre} agregado al inventario.")

def mostrar_inventario():
    """
    Muestra todos los productos del inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['stock']}")

def encontrar_producto(nombre):
    """
    Encuentra un producto por nombre en el inventario y lo devuelve.
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def vender_producto():
    """
    Vende un producto, actualiza el inventario y muestra el total de la venta.
    """
    nombre = input("Ingrese el nombre del producto que desea vender: ")
    producto = encontrar_producto(nombre)
    
    if producto:
        while True:
            try:
                cantidad = int(input(f"¿Cuántas unidades de {nombre} desea vender?: "))
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
                if cantidad <= producto["stock"]:
                    producto["stock"] -= cantidad
                    total = cantidad * producto["precio"]
                    print(f"Venta realizada. Total: ${total:.2f}")
                    
                    if producto["stock"] == 0:
                        print(f"El producto {nombre} se ha agotado.")
                    break
                else:
                    print("No hay suficiente stock en inventario.")
                    break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Por favor, ingrese un valor entero válido para la cantidad.")
    else:
        print("Producto no encontrado en el inventario.")

menu_principal()