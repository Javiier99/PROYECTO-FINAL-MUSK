
from client import Client



# ! Logica para manejar los clientes

class ClientCollection:
    def __init__(self, clients = None): # Creamos el objeto self cliente, en caso de que no pase nada, será none
        self.clients = clients if clients is not None else []
        

    def get_client_by_id(self, client_id): # buscaremos el cliente por el ID
        for i in self.clients: # un bucle dado que tenemos un yield, debemos de recorrer por todos los sitios hasta encontrar lo que nos interesa
            if(i['client_id'] == client_id): # hay una coincidencia, pasa el if
                save_dates = f"El cliente que buscas con id {client_id} se llama {i['name']} es de {i['country']} y se registró el {i['signup_date']}" # ponemos los datos de mejor forma
                return save_dates #retornamos los datos, dado que el id es único, pues no hace falta buscar más
        
        return f"No se ha encontrado el id {client_id}" # en caso de que no encuentre nada con el id, retornamos "no se ha encontrado"



    def clients_by_country(self, country): # buscaremos el pais del cliente
        for i in self.clients:
            if(str(i['country']).lower() == country):
                save_date = f"El cliente que buscas con su pais {country} se llama {i['name']} su id es {i['client_id']} y se registró el {i['signup_date']}"
                return save_date
        return f"No se ha encontrado el pais del cliente: {country}"














