import os
import shutil

def organize_files(source_folder):
    # Verificar si la carpeta de origen existe
    if not os.path.exists(source_folder):
        print(f"La carpeta {source_folder} no existe.")
        return

    # Obtener la lista de archivos en la carpeta de origen
    files = os.listdir(source_folder)

    # Crear un diccionario para almacenar los tipos de archivo
    file_types = {}

    # Iterar sobre cada archivo
    for file in files:
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(file)
        extension = extension.lower()

        # Si la extensión no está en el diccionario, crear una nueva lista
        if extension not in file_types:
            file_types[extension] = []

        # Agregar el archivo a la lista correspondiente
        file_types[extension].append(file)

    # Crear carpetas para cada tipo de archivo y mover los archivos
    for extension, files in file_types.items():
        # Crear el nombre de la carpeta (sin el punto de la extensión)
        folder_name = extension[1:] if extension else "sin_extension"
        folder_path = os.path.join(source_folder, folder_name)

        # Crear la carpeta si no existe
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Mover cada archivo a la carpeta correspondiente
        for file in files:
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(folder_path, file)
            shutil.move(source_path, destination_path)

    print("Organización de archivos completada.")

# Solicitar al usuario la ruta de la carpeta
source_folder = input("Ingrese la ruta de la carpeta que desea organizar: ")

# Llamar a la función para organizar los archivos
organize_files(source_folder)