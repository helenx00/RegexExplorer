import re

texto = 'María tiene 3 gatos. Cada gato pesa alrededor de 4.5 kilos. Ella siempre dice que cuidar a sus mascotas es importante, y es True, porque los gatos son amigables y felices. Su nombre favorito para llamar a sus gatos es "Pelusa". Además, María tiene una lista de tareas para sus gatos: [alimentar, jugar, limpiar, acariciar].'


patron = r"\d+"
enteros= re.findall(patron,texto)
print("Enteros encontrados:", enteros)

patron1 = r"\d+\.+\d"
flotante = re.findall(patron1,texto)
print("flotantes encontrados:", flotante)

patron2 = r"\b(True|False)\b"
booleano = re.findall(patron2,texto)
print("Booleanos encontrados:", booleano)

patron3 = r'"(.*?)"'
string = re.findall(patron3, texto)
print("Strings encontrados:",string)

patron4 = r"\[.*?\]"
lista = re.findall(patron4, texto)
print("listas encontrada:",lista)



