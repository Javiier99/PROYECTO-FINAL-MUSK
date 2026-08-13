



class Sale:

    def __init__(self, sale_id, client_id, product, category, amount, date):
        self.sale_id = int(sale_id)  # ID de la venta
        self.client_id = int(client_id)  # ID del cliente asociado
        self.product = str(product)  # Nombre del producto
        self.category = str(category)  # Categoría
        self.amount = float(amount)  # Importe de la venta
        self.date = str(date)  # Fecha de la venta

    def to_dict(self):
        return {
            "sale_id": self.sale_id,
            "client_id": self.client_id,
            "product": self.product,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
        }








    