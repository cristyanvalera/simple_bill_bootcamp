
from datetime import datetime


encabezado = '''
------------------------------------
           CBC MARKET
      - LISTA DE LA COMPRA -
------------------------------------
'''

print(encabezado)
shopping = []

# Datos del cliente
name = input("Nombre del cliente: ")
document = input("Documento de identidad: ")
print()

print("Para salir del programa escriba 's'\n")
while True:
    product = input("Ingrese un producto: ")
    if product.lower() == "s":
        break
    else:
        price = float(input(f"Precio de {product}: $"))
        shopping.append({"product": product, "price": price})

detalle = f'''
------------------------------------------------------
                    -- SENIAT -- 
------------------------------------------------------
{datetime.now()}

Cliente: {name.capitalize()}
Documento: {document}
------------------------------------------------------
            -- DETALLE DE LA COMPRA -- 
------------------------------------------------------
'''

print()
print(detalle)

for prod in shopping:
    print("{}: ${}".format(prod["product"].title(), prod["price"]))

subtotal = sum(product['price'] for product in shopping)
iva = subtotal * .16
total = subtotal + iva

print("------------------------------------------------------")

print(f"SubTotal: ${subtotal}")
print(f"IVA:      ${iva}")
print(f"Total:    ${total}")