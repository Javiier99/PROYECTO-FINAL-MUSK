from src.client import Client
# ! Logica para manejar los clientes


class ClientCollection:

    def __init__(self, clients=None):
        self.clients = clients if clients is not None else []

    def n_total_client(self):
        return len(self.clients)

    def get_client_by_id(self, client_id):
        """Devuelve el OBJETO Client que coincide con el ID."""
        for client in self.clients:
            cid = (
                client.client_id
                if hasattr(client, "client_id")
                else client.get("client_id")
            )
            if cid == client_id:
                return client
        return None

    def search_clients_by_country(self, country):
        for client in self.clients:
            c_country = (
                client.country
                if hasattr(client, "country")
                else client.get("country")
            )
            if str(c_country).lower() == str(country).lower():
                return client
        return None