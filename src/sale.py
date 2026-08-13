class Sale:

    def __init__(self, sale_id, client_id, product, category, amount, date):
        self.sale_id = int(sale_id)  # Identificador único de la venta
        self.client_id = int(client_id)  # ID del cliente (Clave foránea)
        self.product = str(product)  # Producto adquirido
        self.category = str(category)  # Categoria del producto
        self.amount = float(amount)  # Importe de la transacción
        self.date = str(date)  # Fecha de la venta

    def to_dict(self):
        """Convierte la transacción en un diccionario de datos."""
        return {
            "sale_id": self.sale_id,
            "client_id": self.client_id,
            "product": self.product,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
        }