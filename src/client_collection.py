from src.client import Client


class ClientCollection:

    def __init__(self, clients=None):
        # Inicializa la lista de clientes o asigna una vacía por defecto
        self.clients = clients if clients is not None else []

    def n_total_client(self):
        """Ejercicio 1: Cuenta el número total de clientes registrados."""
        total_client = 0
        for _ in self.clients:
            total_client += 1
        return total_client

    def get_client_by_id(self, client_id):
        """Busca y devuelve los detalles de un cliente por su ID único."""
        for i in self.clients:
            # Compatibilidad para acceder tanto a objeto Client como a diccionario
            cid = i.client_id if hasattr(i, "client_id") else i.get("client_id")
            name = i.name if hasattr(i, "name") else i.get("name")
            country = i.country if hasattr(i, "country") else i.get("country")
            sdate = (
                i.signup_date
                if hasattr(i, "signup_date")
                else i.get("signup_date")
            )

            if cid == client_id:
                return f"El cliente que buscas con id {client_id} se llama {name} es de {country} y se registró el {sdate}"

        return f"No se ha encontrado el id {client_id}"

    def search_clients_by_country(self, country):
        """Busca el primer cliente coincidente por país."""
        for i in self.clients:
            c_country = (
                i.country if hasattr(i, "country") else i.get("country")
            )
            cid = i.client_id if hasattr(i, "client_id") else i.get("client_id")
            name = i.name if hasattr(i, "name") else i.get("name")
            sdate = (
                i.signup_date
                if hasattr(i, "signup_date")
                else i.get("signup_date")
            )

            if str(c_country).lower() == str(country).lower():
                return f"El cliente que buscas con su pais {country} se llama {name} su id es {cid} y se registró el {sdate}"

        return f"No se ha encontrado el pais del cliente: {country}"