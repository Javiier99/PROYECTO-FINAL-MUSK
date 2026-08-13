
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


# # 1 Ejercicio 3
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


# # * Ejercicio 10
# print("Ejercicio 10")

# df_sales = read_file_sales_pd()
# df_client = read_file_client_pd()
# df_merged = pd.merge(df_sales, df_client, on= "client_id", how="inner")
# df_object = SalesCollection(df_merged)
# result_ejercice_10 = df_object.monthly_cumulative_sales()

# print(result_ejercice_10)
# print("")





import pandas as pd
from src.client_collection import ClientCollection
from src.sales_collection import SalesCollection

# NOTA: Importa tus funciones auxiliares de lectura según las tengas definidas
# (por ejemplo: from src.functional_util import read_file_client, read_file_sales, etc.)


def generate_report():
    # ---------------------------------------------------------
    # Carga de datos inicial (evitamos leer múltiples veces)
    # ---------------------------------------------------------
    file_client = read_file_client()
    file_sales = read_file_sales()

    df_sales = read_file_sales_pd()
    df_client = read_file_client_pd()
    df_merged = pd.merge(df_sales, df_client, on="client_id", how="inner")

    # Instanciamos los objetos principales
    client_col = ClientCollection(file_client)
    sales_col = SalesCollection(file_sales)
    sales_col_pd = SalesCollection(df_merged)

    # ---------------------------------------------------------
    # EJECUCIÓN DE LOS 10 CÁLCULOS
    # ---------------------------------------------------------

    # Ejercicio 1: Número total de clientes
    result_ejercice_1 = client_col.n_total_client()

    # Ejercicio 2: Número total de ventas
    result_ejercice_2 = sales_col.number_total_sales()

    # Ejercicio 3: Total de ingresos por cliente
    result_ejercice_3 = sales_col.total_amount_by_client()

    # Ejercicio 4: Número de ventas por cliente
    result_ejercice_4 = sales_col.sales_by_client()

    # Ejercicio 5: Ingreso promedio por venta de cada cliente
    result_ejercice_5 = sales_col.average_sale_by_client()

    # Ejercicio 6: Cliente con mayor gasto por país
    # Instanciamos SalesCollection con clientes según tu estructura previa
    sales_client_obj = SalesCollection(file_client)
    result_ejercice_6 = sales_client_obj.sales_client_by_country(
        result_ejercice_3
    )

    # Ejercicio 7: Total de ventas por categoría
    send_costumer = SalesCollection(read_file_sales_pd())
    result_ejercice_7 = send_costumer.total_amount_by_category()

    # Ejercicio 8: Cliente con más ventas en una categoría específica
    result_ejercice_8 = sales_col_pd.client_more_sales_category("Electronics")

    # Ejercicio 9: Número de clientes que superan un gasto mínimo
    min_amount = 500
    result_ejercice_9 = sales_col_pd.number_client_exceed_min_spending(
        min_amount
    )

    # Ejercicio 10: Ventas acumuladas mes a mes
    result_ejercice_10 = sales_col_pd.monthly_cumulative_sales()

    # ---------------------------------------------------------
    # CONSTRUCCIÓN DEL INFORME ESTRUCTURADO (Página 9 del PDF)
    # ---------------------------------------------------------

    # 1. Mapeo del bloque "clients"
    # Cruzamos los cálculos por cliente (3, 4 y 5) en la lista requerida
    clients_list = []
    for client in file_client:
        c_id = client.client_id if hasattr(client, "client_id") else client["client_id"]
        c_name = client.name if hasattr(client, "name") else client["name"]

        # Extraemos totales o asignamos 0 si no existen
        total_spent = (
            result_ejercice_3.get(c_id, 0)
            if isinstance(result_ejercice_3, dict)
            else 0
        )
        sale_count = (
            result_ejercice_4.get(c_id, 0)
            if isinstance(result_ejercice_4, dict)
            else 0
        )
        average_sale = (
            result_ejercice_5.get(c_id, 0)
            if isinstance(result_ejercice_5, dict)
            else 0
        )

        clients_list.append(
            {
                "client_id": c_id,
                "name": c_name,
                "total_spent": total_spent,
                "sale_count": sale_count,
                "average_sale": average_sale,
            }
        )

    # Suma total de todos los ingresos
    total_revenue = (
        sum(df_sales["amount"])
        if "amount" in df_sales.columns
        else sum(result_ejercice_3.values())
    )

    # Dict final con la estructura exacta del PDF
    report = {
        "summary": {
            "total_clients": result_ejercice_1,
            "total_sales": result_ejercice_2,
            "total_revenue": total_revenue,
        },
        "clients": clients_list,
        "top_client_by_country": result_ejercice_6,
        "sales_by_category": result_ejercice_7,
        "high_spending_clients": result_ejercice_9,
        "monthly_sales": result_ejercice_10,
    }

    # ---------------------------------------------------------
    # GUARDAR JSON
    # ---------------------------------------------------------
    with open("data/report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    return report


if __name__ == "__main__":
    generate_report()


