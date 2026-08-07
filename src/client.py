# from client_collection import client_collection

class Client:
    def __init__(self, client_id, name, country, signup_date):
        self.client_id = int(client_id) # Identificaión único
        self.name =  str(name) # Nombre del cliente
        self.country = str(country) # Pais del cliente
        self.signup_date = str(signup_date) # Fecha en la que se registro

    # ? Tengo que exportarlo, en base a un filtro que quiero hacer, en base a ventas en base a que?
    def to_dict(self, export):
        if(export == 1):
            pass
        elif(export == 2):
            pass
        with open("data/clientes_creado.json", "w", encoding="utf-8"):
            pass
        pass
































