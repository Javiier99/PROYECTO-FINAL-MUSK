import os
import sys

# Calculamos la ruta raíz (un nivel por encima de la carpeta src)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Inyectamos la ruta en el sistema de búsqueda de Python
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)