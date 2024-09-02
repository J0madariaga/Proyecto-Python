# Definir los precios de los libros
precios = {
    'Cocina': 5500,
    'Arte': 4500,
    'Religioso': 6500,
    'Novelas': 5000
}

# Función para calcular descuentos
def calcular_descuento(cantidad_libros):
    # Descuento por 4 libros, uno de cada tipo
    if all(cantidad_libros[tipo] >= 1 for tipo in precios):
        return 0.20
    
    # Descuento por 2 libros, uno de dos tipos diferentes
    tipos_con_libros = sum(1 for cantidad in cantidad_libros.values() if cantidad >= 1)
    if tipos_con_libros == 2:
        return 0.15
    
    # Descuento por 4 libros del mismo tipo
    if any(cantidad == 4 for cantidad in cantidad_libros.values()):
        return 0.10
    
    # Descuento por 2 libros del mismo tipo
    if any(cantidad == 2 for cantidad in cantidad_libros.values()):
        return 0.05
    
    # No hay descuento
    return 0.0

# Inicializar variables
clientes = []
max_libros = 0
max_descuento = 0

# Input del número de clientes
n = int(input("Ingrese el número de clientes: "))

for i in range(n):
    print(f"\nCliente {i+1}:")
    libros = {
        'Cocina': int(input("Cantidad de libros de Cocina: ")),
        'Arte': int(input("Cantidad de libros de Arte: ")),
        'Religioso': int(input("Cantidad de libros de Religioso: ")),
        'Novelas': int(input("Cantidad de libros de Novelas: "))
    }
    
    total_libros = sum(libros.values())
    descuento = calcular_descuento(libros)
    precio_total = sum(libros[tipo] * precios[tipo] for tipo in libros)
    precio_con_descuento = precio_total * (1 - descuento)
    
    clientes.append({
        'libros': libros,
        'total_libros': total_libros,
        'descuento': descuento,
        'precio_final': precio_con_descuento
    })
    
    if total_libros > max_libros:
        max_libros = total_libros
        
    if descuento > max_descuento:
        max_descuento = descuento

# Mostrar resultados
print("\nResultados:")

# Mostrar la cantidad total de libros comprados por cliente, categorizados por tipo de libro
for i, cliente in enumerate(clientes):
    print(f"\nCliente {i+1}:")
    print(f"  Libros comprados:")
    for tipo, cantidad in cliente['libros'].items():
        print(f"    {tipo}: {cantidad}")
    print(f"  Total de libros: {cliente['total_libros']}")
    print(f"  Descuento aplicado: {cliente['descuento'] * 100}%")
    print(f"  Precio final: ${cliente['precio_final']:.2f}")

# Determinar y mostrar el cliente que más libros compró
clientes_max_libros = [i+1 for i, cliente in enumerate(clientes) if cliente['total_libros'] == max_libros]
print(f"\nEl cliente que más libros compró fue el Cliente(s): {', '.join(map(str, clientes_max_libros))} con {max_libros} libros.")

# Determinar y mostrar el cliente o los clientes que obtuvieron más descuento
clientes_max_descuento = [i+1 for i, cliente in enumerate(clientes) if cliente['descuento'] == max_descuento]
print(f"El cliente que obtuvo el mayor descuento fue el Cliente(s): {', '.join(map(str, clientes_max_descuento))} con un {max_descuento * 100}% de descuento.")

