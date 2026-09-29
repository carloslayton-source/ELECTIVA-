#Situacion: Una tienda necesita analizar su inventario. Cree un Porgrama que trabaje con la siguiente lista.

productos =[
    {"nombre":"Teclado","precio":80000,"cantidad":3},
    {"nombre":"Mouse","precio":50000,"cantidad":5},
    {"nombre":"Monitor","precio":700000,"cantidad":2},
    {"nombre":"Camara","precio":120000,"cantidad":1}
]

def calcular_total(precio, cantidad):
    return precio * cantidad

for producto in productos:
    total = calcular_total(producto["precio"], producto["cantidad"])
    producto["total"] = total
    print(producto["nombre"], producto["total"])

bajo_stock = []
for producto in productos:
     if producto["cantidad"] <= 2:
        bajo_stock.append(producto["nombre"])
        
valor_total_inventario = 0
for producto in productos:
    valor_total_inventario += producto["total"]

print(f"Valor Total del inventario:{valor_total_inventario}")
print(f"Productos con bajo stock:{bajo_stock}")