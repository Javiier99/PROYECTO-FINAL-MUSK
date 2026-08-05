

from sale import Sale

# ! Manejar toda la logica de las ventas

class SalesCollection:
    def __init__(self, a_line_file):
        self.a_line_file = a_line_file

    def sales_by_client(self):
        sales_client = {} # creamos un diccionario para poder guardar cada venta que ha realizado cada cliente
        for i in self.a_line_file: # Dado que tenemos en el otro archivo un yield, necesitamos que lo vaya recorriendo poco a poco
            client_id = i[1] # i[1] es el lugar donde se encuentran los ID
            if client_id not in sales_client: # Hay que dividir entre los ID que tenemos y los que no tenemos, en caso de que client_id no se encuentre en sales_client, se crea uno nuevo con un valor de 1, en caso contrario, se le suma 1
                sales_client[client_id] = 1
            else:
                sales_client[client_id] += 1

        return f"Los clientes han tenido estas Ventas: {sales_client}"



    def total_amount_by_client(self):
        # Suma de importes de un cliente
        sales_amount_client = {} 
        for i in self.a_line_file:
            client_id = i[1]
            amomunt_id = round(float(i[4]),2)
            if client_id not in sales_amount_client:
                sales_amount_client[client_id] = amomunt_id
            else:
                sales_amount_client[client_id] += amomunt_id
        return sales_amount_client

        

    def total_amount_by_category(self):
        sales_amount_category = {} 
        for i in self.a_line_file:
            category = i[3]
            amomunt = round(float(i[4]),2)
            if category not in sales_amount_category:
                sales_amount_category[category] = amomunt
            else:
                sales_amount_category[category] += amomunt
        sales_amount_category = {value: round(key, 2) for value, key in sales_amount_category.items()}
        return sales_amount_category

    def average_sale_by_client(self, client_id):
        # Media de gasto por venta para un cliente
        pass




























