from datetime import datetime
import pandas as pd
from src.sale import Sale


def filter_by_category(df, category):
    return df[df["category"] == category]


class SalesCollection:

    def __init__(self, file):
        self.file = file

    def number_total_sales(self):
        return len(self.file)

    def total_amount_by_client(self, client_id=None):
        """Si recibe client_id, devuelve la suma de ese cliente.

        Si no, devuelve el dict completo.
        """
        sales_amount_client = {}

        # Si self.file es un DataFrame
        if isinstance(self.file, pd.DataFrame):
            df = self.file
            if client_id is not None:
                return float(df[df["client_id"] == client_id]["amount"].sum())
            return df.groupby("client_id")["amount"].sum().to_dict()

        # Si self.file es lista de objetos / rows
        for i in self.file:
            cid = (
                i.client_id
                if hasattr(i, "client_id")
                else (int(i[1]) if isinstance(i, (list, tuple)) else i["client_id"])
            )
            amount = (
                i.amount
                if hasattr(i, "amount")
                else (
                    float(i[4]) if isinstance(i, (list, tuple)) else i["amount"]
                )
            )

            if cid not in sales_amount_client:
                sales_amount_client[cid] = amount
            else:
                sales_amount_client[cid] += amount

        if client_id is not None:
            return sales_amount_client.get(client_id, 0)

        return sales_amount_client

    def sales_by_client(self, client_id=None):
        """Si recibe client_id, devuelve la lista/número de ventas de ese cliente.

        Si no, el dict completo.
        """
        sales_client = {}

        # Si self.file es un DataFrame
        if isinstance(self.file, pd.DataFrame):
            df = self.file
            if client_id is not None:
                return df[df["client_id"] == client_id]
            return df.groupby("client_id").size().to_dict()

        for i in self.file:
            cid = (
                i.client_id
                if hasattr(i, "client_id")
                else (int(i[1]) if isinstance(i, (list, tuple)) else i["client_id"])
            )

            if cid not in sales_client:
                sales_client[cid] = []
            sales_client[cid].append(i)

        if client_id is not None:
            return sales_client.get(client_id, [])

        return {cid: len(sales) for cid, sales in sales_client.items()}

    def average_sale_by_client(self):
        amounts = self.total_amount_by_client()
        counts = self.sales_by_client()

        if isinstance(counts, dict):
            return {
                cid: round(amounts[cid] / counts[cid], 2)
                for cid in amounts
                if cid in counts and counts[cid] > 0
            }
        return {}

    def sales_client_by_country(self, result_ejercice_3):
        """Devuelve el NOMBRE del cliente con más gasto por país."""
        sales_country = {}
        max_spent = {}

        for client in self.file:
            cid = (
                client.client_id
                if hasattr(client, "client_id")
                else client["client_id"]
            )
            name = (
                client.name if hasattr(client, "name") else client["name"]
            )
            country = (
                client.country
                if hasattr(client, "country")
                else client["country"]
            )

            if cid in result_ejercice_3:
                total = result_ejercice_3[cid]
                if country not in max_spent or total > max_spent[country]:
                    max_spent[country] = total
                    sales_country[country] = name

        return sales_country

    def total_amount_by_category(self):
        df = self.file
        return df.groupby("category")["amount"].sum().to_dict()

    def client_more_sales_category(self, category):
        df_cat = filter_by_category(self.file, category)
        if df_cat.empty:
            return []
        counts = df_cat.groupby(["client_id", "name"]).size()
        max_sales = counts.max()
        top_clients = counts[counts == max_sales]
        return [
            {"client_id": cid, "name": name, "sales_count": int(max_sales)}
            for cid, name in top_clients.index
        ]

    def number_client_exceed_min_spending(self, min_amount):
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
        df = self.file.copy()
        df["date"] = pd.to_datetime(df["date"])
        df["year_month"] = df["date"].dt.to_period("M").astype(str)
        monthly_sales = df.groupby("year_month")["amount"].sum()
        return monthly_sales.to_dict()