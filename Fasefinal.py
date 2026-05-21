# =====================================================================
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema 2: Gestión de Precios y Promociones en Menú de Restaurante
# =====================================================================

def calcular_precio_final(precio_base, categoria_actual, categoria_objetivo, umbral_precio):
    """
    Módulo encargado de aplicar la lógica de negocio para la promoción.
    Retorna el precio final del producto.
    """
    # Condición: Categoría objetivo COINCIDE Y el precio base es MAYOR al umbral
    if categoria_actual == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        # Si no cumple las condiciones, se mantiene el precio base
        precio_final = precio_base
        
    return precio_final


def main():
    # 1. Matriz de productos: [Nombre del Producto, Categoría, Precio Base]
    # Se incluyen 6 productos de diversas categorías (Entradas, Platos Fuertes, Postres)
    menu = [
        ["Ceviche de Camarón", "Entradas", 18000],
        ["Hamburguesa Gourmet", "Platos Fuertes", 28000],
        ["Filete de Mero", "Platos Fuertes", 35000],
        ["Arroz con Pollo", "Platos Fuertes", 19000],
        ["Volcán de Chocolate", "Postres", 12000],
        ["Limonada Cerezada", "Bebidas", 8000]
    ]
    
    # 2. Parámetros de la promoción (Lógica de Negocio)
    # Ejemplo: 15% de descuento a "Platos Fuertes" que cuesten MÁS de 20,000 pesos
    categoria_promo = "Platos Fuertes"
    umbral_precio_promo = 20000
    
    # 3. Impresión de Resultados (Salida)
    print("=" * 65)
    print(f"   REPORTE DE MENÚ - PROMOCIÓN EN {categoria_promo.upper()}")
    print(f"   (15% de desc. a productos con precio mayor a ${umbral_precio_promo:,})")
    print("=" * 65)
    print(f"{'Producto':<25} {'Categoría':<15} {'P. Base':<12} {'P. Final':<12}")
    print("-" * 65)
    
    # Recorremos la matriz fila por fila utilizando un ciclo repetitivo
    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        
        # Llamamos al módulo/función para calcular el precio de cada ítem
        precio_final = calcular_precio_final(precio_base, categoria, categoria_promo, umbral_precio_promo)
        
        # Formateamos la salida para que se vea organizada en columnas y con separadores de miles
        print(f"{nombre:<25} {categoria:<15} ${precio_base:<11,} ${int(precio_final):<11,}")
        
    print("=" * 65)

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    main()
    