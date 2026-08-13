from datetime import datetime
import pandas as pd
from src.sale import Sale


def filter_by_category(df, category):
    """Función auxiliar para filtrar un DataFrame por categoría."""
    return df[df["category"] == category]


class SalesCollection:

    def __init__(self, file):
        # Almacena el dataset base (lista de filas CSV/objetos o DataFrame)
        self.file = file

    def number_total_sales(self):
        """Ejercicio 2: Cuenta el número total de transacciones."""
        total_sales = 0
        for _ in self.file:
            total_sales += 1
        return total_sales

    def total_amount_by_client(self):
        """Ejercicio 3: Suma el importe gastado por cada cliente."""
        sales_amount_client = {}
        for i in self.file:
            client_id = int(i[1])
            amount = round(float(i[4]), 2)
            if client_id not in sales_amount_client:
                sales_amount_client[client_id] = amount
            else:
                sales_amount_client[client_id] += amount
        return sales_amount_client

    def sales_by_client(self):
        """Ejercicio 4: Contabiliza el número de ventas asociadas a cada cliente."""
        sales_client = {}
        for i in self.file:
            client_id = int(i[1])
            if client_id not in sales_client:
                sales_client[client_id] = 1
            else:
                sales_client[client_id] += 1
        return sales_client

    def average_sale_by_client(self):
        """Ejercicio 5: Calcula el gasto medio por compra de cada cliente."""
        average_sales_client = {}
        for i in self.file:
            client_id = int(i[1])
            amount = float(i[4])
            if client_id not in average_sales_client:
                average_sales_client[client_id] = [amount, 1]
            else:
                average_sales_client[client_id][0] += amount
                average_sales_client[client_id][1] += 1

        return {
            cid: round(values[0] / values[1], 2)
            for cid, values in average_sales_client.items()
        }

    def sales_client_by_country(self, result_ejercice_3):
        """Ejercicio 6: Determina el cliente con mayor gasto acumulado en cada país."""
        sales_country = {}
        for client in self.file:
            client_id = (
                client.client_id
                if hasattr(client, "client_id")
                else client["client_id"]
            )
            country = (
                client.country
                if hasattr(client, "country")
                else client["country"]
            )

            if client_id in result_ejercice_3:
                total = result_ejercice_3[client_id]
                if (
                    country not in sales_country
                    or total > sales_country[country]["total_amount_customer"]
                ):
                    sales_country[country] = {
                        "ID": client_id,
                        "total_amount_customer": round(float(total), 2),
                    }
        return sales_country

    def total_amount_by_category(self):
        """Ejercicio 7: Agrupa y suma las ventas totales por categoría de producto."""
        df = self.file
        return df.groupby("category")["amount"].sum().to_dict()

    def client_more_sales_category(self, category):
        """Ejercicio 8: Obtiene él o los clientes con más compras dentro de una categoría."""
        df_cat = filter_by_category(self.file, category)
        if df_cat.empty:
            return f"No hay ventas para la categoría '{category}'"

        counts = df_cat.groupby(["client_id", "name"]).size()
        max_sales = counts.max()
        top_clients = counts[counts == max_sales]

        return [
            {"client_id": cid, "name": name, "sales_count": int(max_sales)}
            for cid, name in top_clients.index
        ]

    def number_client_exceed_min_spending(self, min_amount):
        """Ejercicio 9: Lista los clientes que hayan superado un umbral mínimo de gasto."""
        df_spend = (
            self.file.groupby(["client_id", "name"])["amount"]
            .sum()
            .reset_index()
        )
        high_spenders = []
        for _, row in df_spend.iterrows():
            if row["amount"] > min_amount:
                high_spenders.append(row["name"])
        return high_spenders

    def monthly_cumulative_sales(self):
        """Ejercicio 10: Calcula el histórico acumulado de ventas mes a mes."""
        df = self.file
        df["date"] = pd.to_datetime(df["date"])
        df["year_month"] = df["date"].dt.to_period("M").astype(str)
        monthly_sales = df.groupby("year_month")["amount"].sum()
        cumulative_sales = monthly_sales.cumsum()
        return cumulative_sales.to_dict()