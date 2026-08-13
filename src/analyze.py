
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




# Lo que tengo que hacer son los 10 calculos que me piden y usar todos los datos de leer archivo en otro sitio


# * Script completo

from client import Client
from sale import Sale
from client_collection import ClientCollection
from sales_collection import SalesCollection
import json
import csv
import pandas as pd


what_to_do = int(input("Que es lo que quieres hacer (contesta con un número) 1: Clientes, 2: Ventas, 3: Exportar, 4: 10 Calculos Obligatorios "))

# # * Clientes
# if(what_to_do == 1):
#     try:
#         def read_file_client():
#             with open("data/clients.json", "r", encoding="utf-8") as file:
#                 file.readline() # Leemos la primera fila para quitarnos el corchete
#                 for line in file: # Empezamos a leer todo el archivo línea por línea
#                     a_line = line.strip()
#                     if(a_line == "]"): # en caso de que llegue al corchete de cierre, terminamos el bucle ya que no nos sirve
#                         break
#                     if a_line.endswith(","): # Quitamos la coma al final para romperlo y tenerlo en diferentes piezas
#                         a_line = a_line[:-1]
#                     client = json.loads(a_line) # Transformamos de json a objeto --> Diccionario
#                     yield client # Enviamos el objeto a donde querramos, de uno en uno, para no saturar
#     except Exception as e:
#         print(f"Ha ocurrido un error {e}")

        
#     what_to_do_client = int(input("1: Quieres buscar por un ID, 2: Quieres buscar por un pais "))

#     if(what_to_do_client == 1): # Si queremos buscar por el id
#         search_client_id = int(input("Qué numero de cliente quieres buscar por id: (Debe de ser un número) "))
#         client = read_file_client() # le damos un valor al primer elemento que saldrá de nuestro archivo
#         client_collection = ClientCollection(client) # Inicializamos el objeto que creamos llamado ClientCollection
#         get_client_id = client_collection.get_client_by_id(search_client_id) # como ya inicializamos, ponemos la función que queremos hacer junto con el id que el usuario quiere buscar
#         print(get_client_id) # Imprimimos el resultado


#     elif(what_to_do_client == 2): # Si queremos buscar por pais
#         def all_country():
            
#             try: # Averiguar todos los paises que hay en el json, para ello debemos de preparar lo que tenemos que enviar a sales collection
#                 with open("data/clients.json", "r", encoding="utf-8") as file:
#                     df = pd.read_json(file) #Utilizamos pandas porque es una opción mucho más rápida
#                 all_country_file = list(df['country'].unique())
#                 country_in_file = "" #Hay que saber todos los paises que son
#                 for i in all_country_file:
#                     country_in_file += f", {i}"
#                 search_for_country = str(input(f"Los países que hay{country_in_file} escoje un pais ")).lower()
#                 return search_for_country

#             except Exception as e:
#                 print(f"Ha ocurrido un error {e}")

#         all_country_client = all_country()
#         client_country = read_file_client()
#         client_collections = ClientCollection(client_country)
#         get_client_country = client_collections.search_clients_by_country(all_country_client)
#         print(get_client_country)

# # * Ver toda la parte de ventas

# elif(what_to_do == 2):
#     try:
#         def read_file_sales():
#             with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
#                 read_files = csv.reader(file) # Lee el archivo de 1 en 1
#                 header = next(read_files) # Quitamos el header
#                 for i in read_files: #Lee todo el archivo a medida que lo vayan cesitando
#                     yield i # Lo enviamos con Yield para no sobrecargar el servidor
#         # Utilizaré los dos siguientes códigos para todo, y así evitamos diplicidad en el código
#         save_data = read_file_sales() # Lee el archivo completo
#         all_object_class = SalesCollection(save_data) # Creamos el objeto con lo que vayamos enviando

#     except Exception as e:
#         print(f"Ha ocurrido un error {e}")
#     print("")
#     print("")
#     what_to_do_sales = int(input("Contesta con un número: 1: Quieres saber la cantidad de compra por ID, 2: Saber el total de dinero que han comprado por ID, 3: Saber el total de dinero obtenido por categorías, 4: Venta Media por cliente "))
#     print("")
#     print("")
#     try:
#         def read_file():
#             with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
#                 read_files = csv.reader(file) # Lee el archivo de 1 en 1
#                 header = next(read_files) # Quitamos el header
#                 for i in read_files: #Lee todo el archivo a medida que lo vayan cesitando
#                     yield i # Lo enviamos con Yield para no sobrecargar el servidor

#         # Utilizaré los dos siguientes códigos para todo, y así evitamos diplicidad en el código
#         save_data = read_file() # Lee el archivo completo
#         all_object_class = SalesCollection(save_data) # Creamos el objeto con lo que vayamos enviando
#     except Exception as e:
#         print(f"Ha ocurrido un error {e}")

#     if(what_to_do_sales == 1): #  Saber la cantidad de compra por cliente
#         result = all_object_class.sales_by_client()
#         print(result)

#     elif(what_to_do_sales == 2): # Saber el total de dinero que han comprado por ID
#         result = all_object_class.total_amount_by_client()
#         print(result)

#     elif(what_to_do_sales == 3): # Saber el dinero total obtenido por categoría
#         result = all_object_class.total_amount_by_category()
#         print(result)

#     elif(what_to_do_sales == 4): # Valor Media por cliente # Creo que se refiere al valor porque entonces no hay otra cosa2
#         result = all_object_class.average_sale_by_client()
#         print(result)

# # * Exportar

# elif(what_to_do == 3):
#     what_to_do_export = int(input("1: Exportar clientes, 2: Exportar  ventas"))
    
#     if(what_to_do_export == 1):
#         try:
            
#                 with open("data/clients.json", "r", encoding="utf-8") as file:
#                     read_file = pd.read_json(file)
#                     table_pd_file = pd.DataFrame(read_file)
#                     print(table_pd_file)
#         except Exception as e:
#             print(f"Ha ocurrido un error {e}")
#         pass
#     elif(what_to_do_export == 2):
#         pass
#     else:
#         print("Ese comando no existe")



# Aquí se haran los 10 calculos que pide
if(what_to_do == 4):
    print("")
    print("")
    what_do_you_whant = int(input("1: Número total de clientes, 2: Número total de ventas, 3: Total Ingreso por cliente, 4: Número de ventas por cliente, 5: Ingreso promedio por venta de cada cliente, 6: Cliente con mayor gasto por pais, 7: Total de ventas por categoría, 8: cliente con más ventas en una categoría específica, 9: Número de clientes que superen un gasto mínimo, 10: Ventas acumuladas mes a mes "))
    print("")
    print("")

    if(what_do_you_whant == 1 or what_do_you_whant == 6): # Aquí debo de poner todo lo que se lea con cliente
        # * Abrir todos los archivos necesarios
        try:
            def read_file_client():
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
        except Exception as e:
            print(f"Ha ocurrido un error {e}")
    if(what_do_you_whant == 2 or what_do_you_whant == 3 or what_do_you_whant == 4 or what_do_you_whant == 5 or what_do_you_whant == 6): # Aquí debo de poner todo lo que se lea con ventas
        try:
            def read_file_sales():
                with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
                    read_files = csv.reader(file) # Lee el archivo de 1 en 1
                    header = next(read_files) # Quitamos el header
                    for i in read_files: #Lee todo el archivo a medida que lo vayan cesitando
                        yield i # Lo enviamos con Yield para no sobrecargar el servidor
            # Utilizaré los dos siguientes códigos para todo, y así evitamos diplicidad en el código
            save_data = read_file_sales() # Lee el archivo completo
            all_object_class = SalesCollection(save_data) # Creamos el objeto con lo que vayamos enviando
        except Exception as e:
                    print(f"Ha ocurrido un error {e}")
    if(what_do_you_whant == 7 or what_do_you_whant == 8 or what_do_you_whant == 9): # Aquí debo de poner todo lo que se lea con cliente pandas
        try:
            def read_file_sales():
                with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
                    file_date = pd.read_csv(file)
                    df = pd.DataFrame(file_date)
                    return df

        except Exception as e:
            print(f"Ha ocurrido un error {e}")
    if(what_do_you_whant == 8 or what_do_you_whant == 9): # Aquí debo de poner todo lo que se lea con Venta pandas
        try:
            def read_file_client():
                with open("data/clients.json", "r", newline="", encoding="utf-8") as file:
                    file_date = pd.read_json(file)
                    df = pd.DataFrame(file_date)
                    return df

        except Exception as e:
            print(f"Ha ocurrido un error {e}")


    # * Todos los calculos

    if(what_do_you_whant == 1): # Calculo del número total de clientes
        file = read_file_client()
        n_client_total = ClientCollection(file)
        result = n_client_total.n_total_client()
        print(result)
    elif(what_do_you_whant == 2):
        result = all_object_class.number_total_sales()
        print(result)
    elif(what_do_you_whant == 3):
        result = all_object_class.total_amount_by_client()
        print(result)
    elif(what_do_you_whant == 4):
        result = all_object_class.sales_by_client()
        print(result)
    elif(what_do_you_whant == 5):
        result = all_object_class.average_sale_by_client()
        print(result)
    elif(what_do_you_whant == 6):
        file = read_file_client() 
        search_country = ClientCollection(file)
        result_country = search_country.client_by_country()
        total_importe_cliente = all_object_class.total_amount_by_client()
        result = all_object_class.sales_client_by_country(result_country, total_importe_cliente)
        print(result)
    elif(what_do_you_whant == 7):
        df = read_file_sales()
        send_costumer = SalesCollection(df)
        result = send_costumer.total_amount_by_category()
        print(result)
    elif(what_do_you_whant == 8):
        df_sales = read_file_sales()
        df_client = read_file_client()
        df_merged = pd.merge(df_sales, df_client, on= "client_id", how="inner")
        df_object = SalesCollection(df_merged)
        result = df_object.client_more_sales_category()
        print(result)
    elif(what_do_you_whant == 9):
        df_sales = read_file_sales()
        df_client = read_file_client()
        df_merged = pd.merge(df_sales, df_client, on= "client_id", how="inner")
        df_object = SalesCollection(df_merged)
        min_amount = 500
        result = df_object.number_client_exceed_min_spending(min_amount)
        print(result)
    elif(what_do_you_whant == 10):
        df_sales = read_file_sales()
        df_client = read_file_client()
        df_merged = pd.merge(df_sales, df_client, on= "client_id", how="inner")
        df_object = SalesCollection(df_merged)
        min_amount = 500
        result = df_object.number_client_exceed_min_spending(min_amount)
        print(result)




else:
    print("No existe ese comando")























