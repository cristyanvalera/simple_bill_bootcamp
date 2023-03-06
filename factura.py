from datetime import datetime

inventory = [
    {"id": 1, "name": "cafe", "price": 12.04, "stock": 25},
    {"id": 2, "name": "azucar", "price": 8.75, "stock": 30},
    {"id": 3, "name": "mantequilla", "price": 7.50, "stock": 24},
    {"id": 4, "name": "queso", "price": 14.99, "stock": 34},
    {"id": 5, "name": "harina", "price": 3.45, "stock": 48},
]

def show_products(inventory):
    for product in inventory:
        id, name, price = product["id"], product["name"], product["price"]
        print(f"{id} - {name.title():15} ${price}")
    print("Escoja el producto de su elección.")

def calc_totals(shopping_car):
    subtotal = sum(product['price'] for product in shopping_car)
    iva = subtotal * .16
    total = subtotal + iva
    return subtotal, iva, total

def show_shooping(shopping_car):
    for product in shopping_car:
        name, price = product["name"], product["price"]
        print("{:<26} ${:<9}".format(name.title(), price))

header = '''
------------------------------------
             SENIAT
           CBC MARKET
          J-40563258-8
  CALLE 18, ENTRE CARRERAS 5 Y 6
       GUANARE - PORTUGUESA
------------------------------------'''

print(header)
print(f"     {datetime.today()}")
print("------------------------------------")

client = input("Nombre del cliente: ").capitalize()
document = input("Documento del cliente: ")

print('''
------------------------------------
    -- MENU DE PRODUCTOS --
------------------------------------''')

show_products(inventory)

shopping_car = []
subtotal = 0
iva = 0
total = 0

print("-----------------------------------")
print("Para salir del programa escriba 'q'\n")

while True:
    buscar = input("--> ").lower()
    if buscar == "q":
        break

    for product in inventory:
        if buscar == product["name"] or buscar == str(product["id"]):
            shopping_car.append({
                "name": product["name"], 
                "price": product["price"],
            })
            print(product["name"], product["price"])

subtotal, iva, total = calc_totals(shopping_car)

print(header)
print(f"Cliente: {client}")
print(f"Documento: {document}")
print("-----------------------------------")

show_shooping(shopping_car)

print("-----------------------------------")
print(f"SubTotal:", " " * 16, f"${subtotal:.2f}")
print(f"IVA 16%: ", " " * 16, f"${iva:.2f}")
print("-----------------------------------")
print("Total:    ", " " * 15, f"${total:.2f}")
