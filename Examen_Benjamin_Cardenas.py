productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
} 

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese una opción: "))
            if 1 <= op <= 6:
                return op
            print("Debe seleccionar una opción válida (1 al 6)")
        except ValueError:
            print('Debe ingresar un número entero')

def buscar_codigo(codigo, dicc_stock):
    return codigo.upper() in dicc_stock

def unidades_categorias(categoria, dicc_productos, dicc_stock):
    total = 0
    for codigo in dicc_productos:
        if dicc_productos[codigo][1].lower() == categoria.lower():
            total += dicc_stock[codigo][1]
    
    print(f"El total de unidades disponibles para la categoría '{categoria}' es: {total}")

def busqueda_precio(p_min, p_max, dicc_productos, dicc_stock):
    lista = []
    for codigo in dicc_stock:
        precio = dicc_stock[codigo][0]
        unidades = dicc_stock[codigo][1]

        if p_min <= precio <= p_max and unidades != 0:
            nombre = dicc_productos[codigo][0]
            lista.append(f"{nombre}--{codigo}")
    
    lista.sort()
    if len(lista) == 0:
        print("No hay productos en ese rango de precio con stock disponible.")
    else:
        print('Los productos encontrados son:', lista)

def actualizar_precios(codigo, nuevo_precio, dicc_stock):
    codigo = codigo.upper()
    if buscar_codigo(codigo, dicc_stock):
        dicc_stock[codigo][0] = nuevo_precio
        return True
    return False

def agregar_productos(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, dicc_productos, dicc_stock):

    codigo = codigo.upper()
    if buscar_codigo(codigo, dicc_stock):
        return False
    
    dicc_productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    dicc_stock[codigo] = [precio, unidades]
    return True

def eliminar_producto(codigo, dicc_productos, dicc_stock):
   
    codigo = codigo.upper()

    if buscar_codigo(codigo, dicc_stock):
        del dicc_productos[codigo]
        del dicc_stock[codigo]
        return True
    return False

while True:
    print("\n=========== MENU PRINCIPAL ===========")
    print("1. Unidades por categoría")
    print('2. Búsqueda de productos por rango de precio')
    print('3. Actualizar precios de productos')
    print('4. Agregar producto')
    print('5. Eliminar producto')
    print('6. Salir')

    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese la categoría que desea consultar: ")
        unidades_categorias(categoria, productos, stock)

    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese el precio mínimo: "))
                p_max = int(input('Ingrese el precio máximo: '))
                if p_min > p_max:
                    print("El precio mínimo no puede ser mayor al máximo.")
                    continue
                break
            except ValueError:
                print("Debe ingresar valores en números enteros.")
        
        busqueda_precio(p_min, p_max, productos, stock)

    elif opcion == 3:
        codigo = input('Ingrese el código del producto: ')
        try:
            nuevo = int(input("Ingrese el nuevo precio: "))
            if actualizar_precios(codigo, nuevo, stock):
                print("Precios de los productos actualizados de manera exitosa.")
            else:
                print("El código del producto no existe.")
        except ValueError:
            print("El precio debe ser un número entero.")
    
    elif opcion == 4:
        print("\n--- Registrar Nuevo Producto ---")
        codigo = input("Código (ej. M007): ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        marca = input("Marca: ")
        try:
            peso_kg = float(input("Peso en KG: "))
            es_importado = input("¿Es importado? (s/n): ").lower() == 's'
            es_para_cachorro = input("¿Es para cachorro? (s/n): ").lower() == 's'
            precio = int(input("Precio: "))
            unidades = int(input("Unidades iniciales en stock: "))
            
            if agregar_productos(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, productos, stock):
                print("Producto agregado correctamente.")
            else:
                print("Error: El código de producto ya existe.")
        except ValueError:
            print("Error: Tipos de datos inválidos para los campos numéricos.")
    
    elif opcion == 5:
        codigo = input('Ingrese el código del producto a eliminar: ')
        if eliminar_producto(codigo, productos, stock):
            print("El producto ha sido eliminado exitosamente de los registros.")
        else:
            print("El código solicitado no existe.")

    else:
        print("Programa finalizando.... Muchas gracias.")
        break
