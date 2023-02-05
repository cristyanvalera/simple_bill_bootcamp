
clientes = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]

descuentos = {'Alex': 36, 'Bob': 8, 'Carol': 95, 'Dave': 97, 'Flow': 2, 'Katie': 32, 'Nate': 91}

clientela_10 = {cliente:descuento for (cliente, descuento) in descuentos.
items() if descuento < 30}

print(clientela_10)




# dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
# temp = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]

# temp_semanal = {dias:temp for (dias, temp) in zip(dias, temp)}
# print(temp_semanal)

# <nombre_diccionario> = {<new_key>:<new_value> for (key,value) in <dict>.items() if <condition>}

