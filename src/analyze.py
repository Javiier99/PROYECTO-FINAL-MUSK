




# ! Script principal, se debe: Leer los datos, crear los objetos, hacer los 10 cálculos requeridos, general el informe JSON final


# El archivo generado por analyze.py debe devolver exactamente:
# {
# "summary": { "total_clients": , "total_sales": , "total_revenue":
# },
# "clients": [
# {
# "client_id": ,
# "name": , "total_spent":, "sale_count": ,: 
# "average_sale":
# },
# ...
# ],
# "top_client_by_country": { "Spain": ,
# "Germany": ,
# "France":
# },
# "sales_by_category": { "Electronics": , "Accessories":
# },
# "high_spending_clients": [
# ,
# ],
# "monthly_sales": { "2023-07":
# }




# total_spent --> Suma de todo lo comprado
# sale_count --> Número de ventas
# average_sale --> (total_spent / sales_count)



# top_client_by_country
# Un diccionario donde cada país tiene el cliente que más gastó.

# sales_by_category
# Totales agrupados por categoría.

# high_spending_clients
# Clientes cuyo gasto total supera un umbral (p. ej. 500€)

# monthly_sales
# Totales agrupados por mes (período YYYY-MM







# * Script completo

from client import Client
from sale import Sale
from client_collection import ClientCollection
from sales_collection import SalesCollection
import json
import pandas as pd


what_to_do = int(input("Que es lo que quieres hacer (contesta con un número) 1: Clientes 2: Ventas "))

# * Clientes
if(what_to_do == 1):
    what_to_do_client = int(input("1: Quieres buscar por un ID, 2: Quieres buscar por un pais "))
    def read_file():
                with open("data/clients.json", "r", encoding="utf-8") as file:
                    file.readline() # Leemos la primera fila para quitarnos el corchete
                    for line in file: # Empezamos a leer todo el archivo línea por línea
                        a_line = line.strip()
                        if(a_line == "]"): # en caso de que llegue al corchete de cierre, terminamos el bucle ya que no nos sirve
                            break
                        if a_line.endswith(","): # Quitamos la coma al final para romperlo y tenerlo en diferentes piezas
                            a_line = a_line[:-1]
                        client = json.loads(a_line) # Transformamos de json a objeto --> Diccionario
                        yield client # Enviamos el objeto a donde querramos, de uno en uno, para no saturar

    if(what_to_do_client == 1): # Si queremos buscar por el id
        search_client_id = int(input("Qué numero de cliente quieres buscar por id: (Debe de ser un número) "))
        client = read_file() # le damos un valor al primer elemento que saldrá de nuestro archivo
        client_collection = ClientCollection(client) # Inicializamos el objeto que creamos llamado ClientCollection
        get_client_id = client_collection.get_client_by_id(search_client_id) # como ya inicializamos, ponemos la función que queremos hacer junto con el id que el usuario quiere buscar
        print(get_client_id) # Imprimimos el resultado


    elif(what_to_do_client == 2):
        def all_country():
            # Averiguar todos los paises que hay en el json
            with open("data/clients.json", "r", encoding="utf-8") as file:
                df = pd.read_json(file) #Utilizamos pandas porque es una opción mucho más rápida
            all_country_file = list(df['country'].unique())
            country_in_file = ""
            for i in all_country_file:
                country_in_file += f", {i}"
            search_for_country = str(input(f"Los países que hay{country_in_file} escoje un pais ")).lower()
            return search_for_country

        all_country_client = all_country()
        client = read_file()
        client_collections = ClientCollection(client)
        get_client_country = client_collections.clients_by_country(all_country_client)
        print(get_client_country)



elif(what_to_do == 2):
    pass

else:
    print("No existe ese comando")



