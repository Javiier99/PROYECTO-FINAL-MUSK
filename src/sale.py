



class Sale:
    def __init__(self, sale_id, client_id, product, category, amount, date):
        self.sale_id = int(sale_id) #id de la venta
        self.client_id = int(client_id) # id del cliente asociado (clave externa)
        self.product = str(product) # nombre del producto vendido
        self.category = str(category) # categoría
        self.amount = float(amount) # importe de la venta
        self.date = str(date) # fecha de la venta

    def to_dict(self):
        # Hacer que el objeto se transforme en un diccionario  para poder exportarlo como JSON
        pass























