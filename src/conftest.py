import os
import sys

# Inyecta la raíz del repositorio en sys.path al arrancar pytest
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_path not in sys.path:
    sys.path.insert(0, root_path)