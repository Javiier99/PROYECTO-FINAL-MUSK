

from sale import Sale
import pandas as pd
from datetime import datetime

# ! Manejar toda la logica de las ventas

def filter_by_category(df, category):
    return df[df["category"] == category]

class SalesCollection:
    def __init__(self, file):
        self.file = file



    # * Esta bien
    # Ejercicio 2
    def number_total_sales(self): # Contar de 1 en 1 los clientes
        total_sales = 0
        for i in self.file:
            total_sales += 1
        return total_sales

    # Ejercicio 3
    
    def total_amount_by_client(self): # Suma de importes de un cliente
        sales_amount_client = {} 
        for i in self.file:
            client_id = int(i[1])
            amomunt = round(float(i[4]),2)
            if client_id not in sales_amount_client:
                sales_amount_client[client_id] = amomunt
            else:
                sales_amount_client[client_id] += amomunt
        return sales_amount_client

    # Ejercicio 4

    def sales_by_client(self): #Ventas por cada cliente
        sales_client = {} # creamos un diccionario para poder guardar cada venta que ha realizado cada cliente
        for i in self.file: # Dado que tenemos en el otro archivo un yield, necesitamos que lo vaya recorriendo poco a poco
            client_id = int(i[1]) # i[1] es el lugar donde se encuentran los ID
            if client_id not in sales_client: # Hay que dividir entre los ID que tenemos y los que no tenemos, en caso de que client_id no se encuentre en sales_client, se crea uno nuevo con un valor de 1, en caso contrario, se le suma 1
                sales_client[client_id] = 1
            else:
                sales_client[client_id] += 1

        return sales_client

    # Ejercicio 5

    def average_sale_by_client(self): #Media de gasto de un cliente
        average_sales_client = {} # creamos un diccionario para poder guardar cada venta que ha realizado cada cliente
        for i in self.file: # Dado que tenemos en el otro archivo un yield, necesitamos que lo vaya recorriendo poco a poco
            client_id = int(i[1]) # i[1] es el lugar donde se encuentran los ID
            amount = float(i[4])
            if client_id not in average_sales_client: # Hay que dividir entre los ID que tenemos y los que no tenemos, en caso de que client_id no se encuentre en sales_client, se crea uno nuevo con un valor de 1, en caso contrario, se le suma 1
                average_sales_client[client_id] = [amount, 1]
            else:
                average_sales_client[client_id][0] += amount
                average_sales_client[client_id][1] += 1
        average_sales = {cid: round(values[0] / values[1], 2)for cid, values in average_sales_client.items()}
        return average_sales

    # Ejercicio 6
    def sales_client_by_country(self, result_ejercice_3):
        sales_country = {}

        for client in self.file:
            client_id = client["client_id"]
            country = client["country"]
            if client_id in result_ejercice_3: # Cruce de ID con las cantidades del Ejercicio 3
                total = result_ejercice_3[client_id]
                if country not in sales_country or total > sales_country[country]["total_amount_customer"]: # Nos quedamos con el ID que más ha gastado de cada país
                    sales_country[country] = {
                        "ID": client_id,
                        "total_amount_customer": round(float(total), 2)
                    }
        return sales_country

    # Ejercicio 7

    def total_amount_by_category(self): # Suma de importes por categoría de cliente
        df = self.file
        sales_total = {}
        result = df.groupby('category')['amount'].sum().to_dict()
        return result


    # Ejercicio 8

    def client_more_sales_category(self, category):
        df_cat = filter_by_category(self.file, category)
        if df_cat.empty:
            return f"No hay ventas para la categoría '{category}'"
        counts = df_cat.groupby(["client_id", "name"]).size()

        max_sales = counts.max()
        top_clients = counts[counts == max_sales]

        top_list = [{"client_id": cid, "name": name, "sales_count": int(max_sales)} for cid, name in top_clients.index ]

        return top_list

    def number_client_exceed_min_spending(self, min_amount):
        df_spend = (self.file.groupby(["client_id", "name"])["amount"].sum().reset_index())

        high_spenders = []

        for indice, row in df_spend.iterrows():
            if row["amount"] > min_amount:
                high_spenders.append(row["name"])

        return high_spenders


    def monthly_cumulative_sales(self):
        df = self.file
        
        df["date"] = pd.to_datetime(df["date"]) # Convertimos directamente a datetime con Pandas

        df["year_month"] = df["date"].dt.to_period("M").astype(str) # Extraemos el periodo YYYY-MM
        monthly_sales = df.groupby("year_month")["amount"].sum() # Agrupamos por mes y calculamos

        cumulative_sales = monthly_sales.cumsum() # Calculamos el acumulado
        return cumulative_sales.to_dict()

























