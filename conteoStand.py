import requests
import matplotlib.pyplot as plt
url = "https://jsjose-fejm.vercel.app/"
data = requests.get(url)
data = data.json()
res1 = 0
res2 = 0
res3 = 0
res4 = 0
res5 = 0

ids = ['EST01', 'EST02', 'EST03', 'EST04', 'EST05', 'EST06', 'EST07', 'EST08', 'EST09', 'EST10', 'EST11', 'EST12', 'EST13', 'EST14', 'EST15', 'EST16', 'EST17', 'EST18', 'EST19', 'EST20', 'EST21', 'EST22', 'EST23', 'EST24', 'EST25', 'EST26', 'EST27', 'EST28', 'EST29', 'EST30', 'EST31', 'EST32', 'EST33', 'EST34', 'EST35', 'EST36', 'EST37', 'EST38', 'EST39', 'EST40', 'EST41', 'EST42', 'EST43', 'EST44', 'EST45', 'EST46', 'EST47', 'EST48', 'EST49', 'EST50', 'EST51', 'EST52', 'EST53', 'EST54', 'EST55', 'EST56', 'EST57', 'EST58', 'EST59', 'EST60', 'EST61', 'EST62', 'EST63', 'EST64', 'EST65', 'EST66', 'EST67', 'EST68', 'EST69', 'EST70', 'EST71', 'EST72']
for e in range(0,72):
        if "Ciclo Basico" in data[ids[e]].values():
            res1 = res1 +1
for e in range(0,72):
        if "Quimica" in data[ids[e]].values():
            res2 = res2 +1
for e in range(0,72):
        if "Ciclo Basico, Quimica" in data[ids[e]].values():
            res2 = res2 +1
for e in range(0,72):
        if "Electromecanica" in data[ids[e]].values():
            res3 = res3 +1
for e in range(0,72):
        if "Soldadura" in data[ids[e]].values():
            res4 = res4 +1
for e in range(0,72):
        if "Programacion" in data[ids[e]].values():
            res5 = res5 +1
resultado = res1+res2+res3+res4+res5
listaStands = [res1,res2,res3,res4,res5]
orientaciones = ["Ciclo basico","Quimica","Electromecanica","Soldadura","Programacion"]
colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
ig, ax = plt.subplots()
ax.pie(listaStands,labels=orientaciones,autopct="%0.1f %%", colors=colores)
ax.set_title("Cantidad de stands por orientacion")
plt.show()