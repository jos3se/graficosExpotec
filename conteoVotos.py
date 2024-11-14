import requests
import matplotlib.pyplot as plt
import operator
url = "https://sistema-votos-python-five.vercel.app/planillaVotos"
#Obtención de data
data = requests.get(url).json()

#Definimos función de conteo de votos
"""
Funciona seleccionando la id y pasandole la información en el formato lista (asi lo devuelve la api).
Luego, iteramos en la data. Si la id buscada coincide con una de las ids devuelta por la API suma un voto al conteo. Al final de iterar toda la data devuelve la suma de todos los votos de esa id en partícular
"""
cantidadVotos = {}
podio = {}
for item in data:
    cantidadVotos[item["Nombre"]] = 0 
for puesto in cantidadVotos:
    for item in data:
        if item["Nombre"] == puesto:
            cantidadVotos[puesto]+=1
res = 0
for voto in cantidadVotos.values():
    res+=voto

valoresOrdenar = dict(sorted(cantidadVotos.items(),key=operator.itemgetter(1),reverse=True))

for i, (clave,valor) in enumerate(valoresOrdenar.items()):
    if i == 5:
        break
    podio[clave] = valor

    
print(podio)

"""
Gráficamos los contenedores. Fácil, verdad? xd
"""
def graficar(titulos:list, valores:list):
    
    fig, ax = plt.subplots()
    colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
    
    ax.pie(valores, labels=titulos, colors=colores)
    ax.set_title("Los 5 stands mas votados de la expo24")
    plt.show()

graficar(podio.keys(),podio.values())  
    

 