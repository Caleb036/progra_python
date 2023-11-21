import pickle

# Objeto de ejemplo a serializar
datos_a_serializar = {
    'nombre': 'Alice',
    'edad': 30,
    'profesion': 'Ingeniera'
}
# Serializar el objeto y guardarlo en un archivo
with open('datos.pickle', 'wb') as archivo:
    pickle.dump(datos_a_serializar, archivo)
# Recuperar el objeto desde el archivo
with open('datos.pickle', 'rb') as archivo:
    datos_recuperados = pickle.load(archivo)

# Mostrar el objeto recuperado
print("Objeto recuperado:", datos_recuperados)
