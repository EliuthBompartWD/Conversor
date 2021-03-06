###

print("""
Bienvenido al conversor de divisas para Argentina. 
Podras seleccionar entre el precio oficial o blue.
Tanto para el D贸lar 馃挼馃挼馃挼馃挼 como para el Euro. 馃挾馃挾馃挾馃挾 
""")

print("""
Selecciona alguna de las opciones para realizar una operacion:

1: COMPRAR DOLAR BLUE | 2: VENDER DOLAR BLUE | 3: COMPRAR EURO BLUE 
4: VENDER EURO BLUE | 5: PRECIO DOLAR BLUE | 6: PRECIO DOLAR OFICIAL
7: PRECIO EURO BLUE | 8: PRECIO EURO OFICIAL 
""")

###
import requests
# Llamada a la API
response = requests.get('https://api.bluelytics.com.ar/v2/latest')
response_json = response.json()

# Variables
accion = input("驴Que accion deseas realizar? ")
dolar_oficial = response_json["oficial"]
dolar_blue = response_json["blue"]
euro_oficial = response_json["oficial_euro"]
euro_blue = response_json["blue_euro"]
date = response_json["last_update"]

def conversor(moneda,operacion,precio):
    print("\n")
    print("Fecha de actualizacion del precio:",date)
    print("\n")
    if operacion == "comprar":
        dinero = round(float(input(f"驴Cuantos {moneda} quieres {operacion}? ")),2)
        result =  dinero * precio
        x = str(result)
        return "$" + x + " pesos" 
    elif operacion == "vender":
        dinero = round(float(input(f"驴Cuantos {moneda} quieres {operacion}? ")),2)
        result = dinero * precio
        x = str(result)
        return "$" + x + " pesos" 
    else:
        x = str(precio)
        result = "$" + x + " pesos"
        return result

if accion == "1":
        print(conversor("D贸lares","comprar",dolar_blue["value_sell"]))
elif accion == "2":
        print(conversor("D贸lares","vender",dolar_blue["value_buy"]))
elif accion == "3":
        print(conversor("Euros","comprar",euro_blue["value_sell"]))
elif accion == "4":
        print(conversor("Euros","vender",euro_blue["value_buy"]))
elif accion == "5":
        print(conversor("D贸lar","precio",dolar_blue["value_avg"]))
elif accion == "6":
        print(conversor("D贸lar","precio",dolar_oficial["value_avg"]))
elif accion == "7":
       print(conversor("Euro","precio",euro_blue["value_avg"]))
elif accion == "8":
        print(conversor("Euro","precio",euro_oficial["value_avg"]))
else:
        print("Debes seleccionar algunas de las opciones para poder continuar")
