

class Client:

    def __init__(self, client_id, name, country, signup_date):
        self.client_id = int(client_id)  # Identificador único
        self.name = str(name)  # Nombre del cliente
        self.country = str(country)  # País del cliente
        self.signup_date = str(signup_date)  # Fecha en la que se registró

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "country": self.country,
            "signup_date": self.signup_date,
        }






