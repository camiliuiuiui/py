persona1={"Nombre":"Camila","Edad":18,"Apellido":"Jaimes","Correo":"cjaimes65412@universidadean.edu.co","Hobbies":["Dormir","Comer","Salir"]}
for clave,valor in persona1.items():
    print (clave,"->",valor)
persona1["Edad"]=40
print (persona1['Edad'])
print (persona1['Hobbies'][0])
print (persona1['Hobbies'])
for k in persona1["Hobbies"]:
    print(k)
for h in persona1["Hobbies"][0:2]:
    print(h)