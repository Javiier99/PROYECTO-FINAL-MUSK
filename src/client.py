# from client_collection import client_collection

class Client:
    def __init__(self, client_id, name, country, signup_date):
        self.client_id = int(client_id) # Identificaión único
        self.name =  str(name) # Nombre del cliente
        self.country = str(country) # Pais del cliente
        self.signup_date = str(signup_date) # Fecha en la que se registro

    def to_dict(self):
        # Hacer que el objeto se transforme en un diccionario para poder exportarlo como JSON
        pass
        































