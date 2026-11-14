persona = {"Nombre": "Camila", "Edad":18, "Ciudad":"Bogota"}
print (persona['Nombre'])
print (persona.get("Sexo"))
persona ["Correo"]="cjaimes65412@universidadean.edu.co"
persona ["Edad"] = 21
persona.update({"Pais":"Colombia"})
print(persona['Correo'])
print(persona['Edad'])
print(persona['Pais'])
for clave in persona.keys():
    print("Clave:",clave)
for valor in persona.values():
    print ("Valor:",valor)
for clave,valor in persona.items():
    print(clave,"->",valor)