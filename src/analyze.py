import json
import os
import sys
import pandas as pd

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from src.client_collection import ClientCollection
from src.functional_util import (
    read_file_client,
    read_file_client_pd,
    read_file_sales,
    read_file_sales_pd,
)
from src.sales_collection import SalesCollection


def generate_report():
    file_client = read_file_client()
    file_sales = read_file_sales()

    df_sales = read_file_sales_pd()
    df_client = read_file_client_pd()
    df_merged = pd.merge(df_sales, df_client, on="client_id", how="inner")

    client_col = ClientCollection(file_client)
    sales_col = SalesCollection(file_sales)
    sales_col_pd = SalesCollection(df_merged)

    result_ejercice_1 = client_col.n_total_client()
    result_ejercice_2 = sales_col.number_total_sales()
    result_ejercice_3 = sales_col.total_amount_by_client()
    result_ejercice_4 = sales_col.sales_by_client()
    result_ejercice_5 = sales_col.average_sale_by_client()

    sales_client_obj = SalesCollection(file_client)
    result_ejercice_6 = sales_client_obj.sales_client_by_country(
        result_ejercice_3
    )

    send_costumer = SalesCollection(df_sales)
    result_ejercice_7 = send_costumer.total_amount_by_category()

    min_amount = 500
    result_ejercice_9 = sales_col_pd.number_client_exceed_min_spending(
        min_amount
    )
    result_ejercice_10 = sales_col_pd.monthly_cumulative_sales()

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