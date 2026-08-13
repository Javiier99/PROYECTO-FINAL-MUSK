class Client:

    def __init__(self, client_id, name, country, signup_date):
        self.client_id = int(client_id)  # Identificador único del cliente
        self.name = str(name)  # Nombre del cliente
        self.country = str(country)  # País de residencia
        self.signup_date = str(signup_date)  # Fecha de registro

    def to_dict(self):
        """Convierte la instancia en un diccionario plano."""
        return {
            "client_id": self.client_id,
            "name": self.name,
            "country": self.country,
            "signup_date": self.signup_date,
        }