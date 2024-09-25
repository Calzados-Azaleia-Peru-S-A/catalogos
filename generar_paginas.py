import yaml
import os

# Ruta al archivo YAML
yaml_file_path = r'D:\HTML\FINAL\catalogo-productos\_data\productos.yml'

# Ruta donde se generarán los archivos .md
output_dir = r'D:\HTML\FINAL\catalogo-productos\_productos'

# Crear la carpeta _productos si no existe
os.makedirs(output_dir, exist_ok=True)

# Leer el archivo YAML y generar archivos .md para cada producto
with open(yaml_file_path, 'r', encoding='utf-8') as file:
    productos = yaml.safe_load(file)

if productos is None:
    print("Error: No se cargaron los productos. Verifica el formato del archivo YAML.")
else:
    # Crear un archivo .md para cada producto
    for nombre_color, datos in productos.items():
        # Reemplazar caracteres no permitidos en nombres de archivo
        nombre_color_limpio = nombre_color.replace("/", "-").replace("\\", "-").replace(" ", "").replace(":", "")
        file_name = f"{nombre_color_limpio}.md"
        file_path = os.path.join(output_dir, file_name)
        
        # Contenido de cada archivo .md
        content = f"""---
layout: product
title: "{datos['name']}"
name: "{datos['name']}"
price: {datos['price']}
---
"""
        # Escribir el contenido en el archivo .md
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    # Mensaje de confirmación al final (sin indentación extra)
    print(f"Páginas de productos generadas en la carpeta {output_dir}")
