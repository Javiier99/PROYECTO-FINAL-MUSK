
# ! Script principal, se debe: Leer los datos, crear los objetos, hacer los 10 cálculos requeridos, general el informe JSON final

# * Script completo

from client import Client
from sale import Sale
from client_collection import ClientCollection
from sales_collection import SalesCollection
import json
import csv
import pandas as pd





# * Abrir todos los archivos necesarios
# 1 Leer archivos con su libreria

def read_file_client():
    try:
        with open("data/clients.json", "r", encoding="utf-8") as file:
            file = json.load(file)
            return file
    except Exception as e:
        print(f"Ha ocurrido un error {e}")


def read_file_sales():
    try:
        with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
            read_files = csv.reader(file) 
            header = next(read_files)
            return list(read_files)
    except Exception as e:
        print(f"Ha ocurrido un error {e}")


# 1 Usar Pandas

def read_file_client_pd():
    try:
        with open("data/clients.json", "r", newline="", encoding="utf-8") as file:
            file_date = pd.read_json(file)
            df = pd.DataFrame(file_date)
            return df
    except Exception as e:
        print(f"Ha ocurrido un error {e}")
        
def read_file_sales_pd():
    try:
        with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
            file_date = pd.read_csv(file)
            df = pd.DataFrame(file_date)
            return df
    except Exception as e:
        print(f"Ha ocurrido un error {e}")





# # 1 Ejercicio 1
# print("Ejercicio 1")

# file_ejercice_1 = read_file_client()
# n_client_total = ClientCollection(file_ejercice_1)
# result_ejercice_1 = n_client_total.n_total_client()
# print(result_ejercice_1)
# print("")

# # 1 Ejercicio 2
# print("Ejercicio 2")

# file_ejercice_2 = read_file_sales()
# n_sales_total = SalesCollection(file_ejercice_2)
# result_ejercice_2 = n_sales_total.number_total_sales()
# print(result_ejercice_2)
# print("")


# 1 Ejercicio 3
# print("Ejercicio 3")
# file_ejercice_3 = read_file_sales()
# n_sales_total = SalesCollection(file_ejercice_3)
# result_ejercice_3 = n_sales_total.total_amount_by_client()
# print(result_ejercice_3)
# print("")


# # 1 Ejercicio 4
# print("Ejercicio 4")

# file_ejercice_4 = read_file_sales()
# n_sales_for_client = SalesCollection(file_ejercice_4)
# result_ejercice_4 = n_sales_for_client.sales_by_client()
# print(result_ejercice_4)
# print("")



# # 1 Ejercicio 5
# print("Ejercicio 5")

# file_ejercice_5 = read_file_sales()
# n_sales_average_for_client = SalesCollection(file_ejercice_5)
# result_ejercice_5 = n_sales_average_for_client.average_sale_by_client()
# print(result_ejercice_5)
# print("")



# # 1 Ejercicio 6
# print("Ejercicio 6")

# file_ejercice_6 = read_file_client()
# create_objet_sales = SalesCollection(file_ejercice_6)
# result_ejercice_6 = create_objet_sales.sales_client_by_country(result_ejercice_3)

# print(result_ejercice_6)
# print("")

# # * Ejercicio 7
# print("Ejercicio 7")

# file_ejercice_7 = read_file_sales_pd()
# send_costumer = SalesCollection(file_ejercice_7)
# result_ejercice_7 = send_costumer.total_amount_by_category()


# print(result_ejercice_7)
# print("")

# # * Ejercicio 8
# print("Ejercicio 8")

# df_sales = read_file_sales_pd()
# df_client = read_file_client_pd()
# df_merged = pd.merge(df_sales, df_client, on= "client_id", how="inner")
# df_object = SalesCollection(df_merged)
# result_ejercice_8 = df_object.client_more_sales_category("Electronics")


# print(result_ejercice_8)
# print("")


# # * Ejercicio 9
# print("Ejercicio 9")

# df_sales = read_file_sales_pd()
# df_client = read_file_client_pd()
# df_merged = pd.merge(df_sales, df_client, on= "client_id", how="inner")
# df_object = SalesCollection(df_merged)
# min_amount = 500
# result_ejercice_9 = df_object.number_client_exceed_min_spending(min_amount)

# print(result_ejercice_9)
# print("")


# * Ejercicio 10
print("Ejercicio 10")

df_sales = read_file_sales_pd()
df_client = read_file_client_pd()
df_merged = pd.merge(df_sales, df_client, on= "client_id", how="inner")
df_object = SalesCollection(df_merged)
result_ejercice_10 = df_object.monthly_cumulative_sales()

print(result_ejercice_10)
print("")




















# summary = {
#     "total_clients": total_clients_val,
#     "total_sales": total_sales_val,
#     "total_revenue": total_revenue_val,
# }

# clients = [
#     {
#         "client_id": client_id_val,
#         "name": name_val,
#         "total_spent": total_spent_val,
#         "sale_count": sale_count_val,
#         "average_sale": average_sale_val,
#     }
# ]

# top_client_by_country = (dict_top_clients)

# sales_by_category = (dict_categories)

# high_spending_clients = list_high_spenders

# monthly_sales = dict_monthly


# data = {
#     "summary": summary,
#     "clients": clients,
#     "top_client_by_country": top_client_by_country,
#     "sales_by_category": sales_by_category,
#     "high_spending_clients": high_spending_clients,
#     "monthly_sales": monthly_sales,
# }