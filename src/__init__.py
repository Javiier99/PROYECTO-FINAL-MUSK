import os
import site
import sys

# Calculamos la ruta absoluta del directorio raíz (un nivel por encima de src)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Agregamos la raíz mediante site-packages/path resolution de Python
if root_dir not in sys.path:
    site.addsitedir(root_dir)
    sys.path.insert(0, root_dir)