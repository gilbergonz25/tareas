import json

inventario = []


def add_item():
    item = input("Ingrese el nombre del artículo: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    inventario.append({'item': item, 'cantidad': cantidad, 'precio': precio})
    print("Artículo agregado al inventario.")

def search_item():
    item = input("Ingrese el nombre del artículo a buscar: ")
    for i in inventario:
        if i['item'] == item:
            print("Artículo encontrado: ", i)


def update_item():
    item = input("Ingrese el nombre del artículo a actualizar: ")
    for i in inventario:
        if i['item'] == item:
            print("Artículo encontrado: ", i)
            field = input("Ingrese la propiedad a actualizar (cantidad o precio): ")
            value = input("Ingrese el nuevo valor: ")
            if field == "cantidad":
                i['quantity'] = int(value)
            elif field == "precio":
                i['precio'] = float(value)
            else:
                print("Propiedad inválida.")
            print("Artículo actualizado.")


def delete_item():
    item = input("Ingrese el nombre del artículo a eliminar: ")
    for i in inventario:
        if i['item'] == item:
            inventario.remove(i)
            print("Artículo eliminado del inventario.")


def show_inventario():
    print(json.dumps(inventario, indent=4))


while True:
    print("\nMenú:")
    print("1. Agregar artículo")
    print("2. Buscar artículo")
    print("3. Actualizar artículo")
    print("4. Eliminar artículo")
    print("5. Mostrar inventario")
    print("6. Salir")
    choice = input("Ingrese su elección: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        search_item()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        show_inventario()
    elif choice == "6":
        break
    else:
        print("Elección inválida.")
