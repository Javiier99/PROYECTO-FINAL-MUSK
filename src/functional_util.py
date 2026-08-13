import csv
import json
import pandas as pd


def read_file_client():
    """Lee el archivo JSON de clientes."""
    try:
        with open("data/clients.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Ha ocurrido un error al leer clientes: {e}")
        return []


def read_file_sales():
    """Lee el archivo CSV de ventas mediante el módulo csv."""
    try:
        with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
            read_files = csv.reader(file)
            header = next(read_files)
            return list(read_files)
    except Exception as e:
        print(f"Ha ocurrido un error al leer ventas: {e}")
        return []


def read_file_client_pd():
    """Carga el JSON de clientes directamente en un DataFrame de Pandas."""
    try:
        with open("data/clients.json", "r", newline="", encoding="utf-8") as file:
            file_date = pd.read_json(file)
            return pd.DataFrame(file_date)
    except Exception as e:
        print(f"Ha ocurrido un error al leer clientes con Pandas: {e}")
        return pd.DataFrame()


def read_file_sales_pd():
    """Carga el CSV de ventas directamente en un DataFrame de Pandas."""
    try:
        with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
            file_date = pd.read_csv(file)
            return pd.DataFrame(file_date)
    except Exception as e:
        print(f"Ha ocurrido un error al leer ventas con Pandas: {e}")
        return pd.DataFrame()