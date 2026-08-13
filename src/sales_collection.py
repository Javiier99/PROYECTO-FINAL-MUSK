

from sale import Sale
import pandas as pd

# ! Manejar toda la logica de las ventas

class SalesCollection:
    def __init__(self, a_line_file):
        self.a_line_file = a_line_file

    def sales_by_client(self): #Ventas por cada cliente
        sales_client = {} # creamos un diccionario para poder guardar cada venta que ha realizado cada cliente
        for i in self.a_line_file: # Dado que tenemos en el otro archivo un yield, necesitamos que lo vaya recorriendo poco a poco
            client_id = i[1] # i[1] es el lugar donde se encuentran los ID
            if client_id not in sales_client: # Hay que dividir entre los ID que tenemos y los que no tenemos, en caso de que client_id no se encuentre en sales_client, se crea uno nuevo con un valor de 1, en caso contrario, se le suma 1
                sales_client[client_id] = 1
            else:
                sales_client[client_id] += 1

        return f"Los clientes han tenido estas Ventas: {sales_client}"



    def total_amount_by_client(self): # Suma de importes de un cliente
        
        sales_amount_client = {} 
        for i in self.a_line_file:
            client_id = i[1]
            amomunt_id = round(float(i[4]),2)
            if client_id not in sales_amount_client:
                sales_amount_client[client_id] = {"revenues_sales" : amomunt_id}
            else:
                sales_amount_client[client_id]["revenues_sales"] += amomunt_id
        return sales_amount_client

        

    def total_amount_by_category(self): # Suma de importes por categoría de cliente
        
        df = self.a_line_file
        sales_total = {}
        result = df.groupby('category')['amount'].sum()
        return result


        # Código sin pandas
        # sales_amount_category = {} 
        # for i in self.a_line_file:
        #     category = i[3]
        #     amomunt = round(float(i[4]),2)
        #     if category not in sales_amount_category:
        #         sales_amount_category[category] = amomunt
        #     else:
        #         sales_amount_category[category] += amomunt
        # sales_amount_category = {value: round(key, 2) for value, key in sales_amount_category.items()}
        # return f"El dinero total por categoría es: {sales_amount_category}"



    def average_sale_by_client(self): #Media de gasto de un cliente
        average_sales_client = {} # creamos un diccionario para poder guardar cada venta que ha realizado cada cliente
        for i in self.a_line_file: # Dado que tenemos en el otro archivo un yield, necesitamos que lo vaya recorriendo poco a poco
            client_id = i[1] # i[1] es el lugar donde se encuentran los ID
            if client_id not in average_sales_client: # Hay que dividir entre los ID que tenemos y los que no tenemos, en caso de que client_id no se encuentre en sales_client, se crea uno nuevo con un valor de 1, en caso contrario, se le suma 1
                average_sales_client[f"{client_id}"] = [i[4], 1]
            else:
                average_sales_client[f"{client_id}"][1] += 1
                pass
        average_sales_client = {value: round(float(key[0])/key[1], 2) for value, key in average_sales_client.items()} # Hacemos len para calcular la media de ventas
        return f"Los clientes han tenido estas ventas medias: {average_sales_client}"

    def number_total_sales(self):
        total_sales = 0
        for i in self.a_line_file:
            total_sales += 1
        return total_sales

    def sales_client_by_country(self, result_country, total_importe_cliente):
        sales_country = {}
        for country in result_country:
            for client_id in country['ID']:
                for key, value in total_importe_cliente.items():
                    if(int(key) == int(client_id)):
                        if(country['country'] not in sales_country):
                            sales_country[country['country']] = {"total_amount_customer" : round(float(value['revenues_sales']), 2),"ID" : client_id }
                        else:
                            if(round(float(sales_country[country['country']]["total_amount_customer"]),2) < round(float(value['revenues_sales']))):
                                sales_country[country['country']] = {"total_amount_customer" : round(float(value['revenues_sales']), 2),"ID" : client_id}

        return sales_country


    def client_more_sales_category(self):
        df_category = self.a_line_file["category"].unique()
        result = [] 

        for category in df_category:
            df_cat = self.a_line_file[self.a_line_file["category"] == category]

            count = df_cat.groupby(["client_id", "name"]).size()

            total_sales = count.max()

            top_clients = count[count == total_sales]

            names = [f"{nombre} (ID: {cid})" for cid, nombre in top_clients.index]
            clientes_str = ", ".join(names)

            result.append(f"Categoría '{category}': {clientes_str} con {total_sales} venta(s)")

        return result


    def number_client_exceed_min_spending(self, min_amount):
        df_spend = (self.a_line_file.groupby(["client_id", "name"])["amount"].sum().reset_index())

        df_filtred = df_spend[df_spend["amount"] > min_amount]

        total_clients = len(df_filtred)

        return (f"Total de clientes que superan los {min_amount}€: {total_clients}\n\n" f"Detalle:\n {df_filtred.to_string}")
    


























