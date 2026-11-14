frutas =["Manzana","Banana","Naranja"]
print (frutas[0])
print (frutas[-1])
frutas.append ("uva")
frutas.insert (1,"pera")
print (frutas)
frutas.remove ("Banana")
ultimo = frutas.pop()
print ("Elemento eliminado", ultimo)
del frutas [0]
print (frutas)