import json
import os
import sys
import pandas as pd

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)
# Ahora sí importamos las funciones normalmente:

from src.functional_util import (
    read_file_client,
    read_file_client_pd,
    read_file_sales,
    read_file_sales_pd,
)
from src.sales_collection import SalesCollection
from src.client_collection import ClientCollection

def generate_report():
    # Carga de datos inicial (evitamos leer múltiples veces)
    # Leer el archivo de forma normal
    file_client = read_file_client()
    file_sales = read_file_sales()

    # Usando Pandas
    df_sales = read_file_sales_pd()
    df_client = read_file_client_pd()
    df_merged = pd.merge(df_sales, df_client, on="client_id", how="inner")

    # Enviamos las tablas obtenidos a las distintos archivos con su clase
    client_col = ClientCollection(file_client)
    sales_col = SalesCollection(file_sales)
    sales_col_pd = SalesCollection(df_merged)

    # Ejercicios
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

    #  Ejercicio 6: Cliente con mayor gasto por país
    # Instanciamos SalesCollection con clientes según tu estructura previa
    sales_client_obj = SalesCollection(file_client)
    result_ejercice_6 = sales_client_obj.sales_client_by_country(result_ejercice_3)

    # Ejercicio 7: Total de ventas por categoría
    send_costumer = SalesCollection(read_file_sales_pd())
    result_ejercice_7 = send_costumer.total_amount_by_category()

    # Ejercicio 8: Cliente con más ventas en una categoría específica
    result_ejercice_8 = sales_col_pd.client_more_sales_category("Electronics")

    # Ejercicio 9: Número de clientes que superan un gasto mínimo
    min_amount = 500
    result_ejercice_9 = sales_col_pd.number_client_exceed_min_spending(min_amount)

    # Ejercicio 10: Ventas acumuladas mes a mes
    result_ejercice_10 = sales_col_pd.monthly_cumulative_sales()



    # Construcción del informe según nos marca en el ejemplo página 9 pdf

    # 1. Mapeo del bloque "clients"
    # Cruzamos los cálculos por cliente (3, 4 y 5) en la lista requerida
    clients_list = []
    for client in file_client:
        c_id = (
            client.client_id
            if hasattr(client, "client_id")
            else client["client_id"]
        )
        c_name = client.name if hasattr(client, "name") else client["name"]

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
                "total_spent": round(total_spent, 2),
                "sale_count": sale_count,
                "average_sale": average_sale,
            }
        )

    total_revenue = sum(df_sales["amount"])

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

    os.makedirs("data", exist_ok=True)
    with open("data/report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    return report


if __name__ == "__main__":
    generate_report()