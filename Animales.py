Animales=[
    {
        "ID":"1",
        "nombre":"antonio",
        "especie":"pantera",
        "edad":"4",
        "citas":"Ninguna",
        "alimento":"Res",
        "cantidad":"10 kilos",
        "vacunas":"Rabia"
    },
    {
        "ID":"2",
        "nombre":"pantera1",
        "especie":"pantera",
        "edad":"4",
        "citas":"Ninguna",
        "alimento":"Res",
        "cantidad":"10 kilos",
        "vacunas":"Rabia"
    }
]
def GetAnimales():
    for animal in Animales:
        print(f"| {animal['ID'],animal['nombre'],animal['especie'],animal['edad'],animal['citas'],animal['alimento'],animal['cantidad'],animal['vacunas']}|")

def postAnimales():
    nombre=input("nombre: ")
    especie=input("especie: ")
    edad=input("edad: ")
    citas=input("citas: ")
    alimento=input("alimento: ")
    cantidad= input("cantidad: ")
    vacunas=input("vacunas: ")
    id=len(Animales)+1
    Animales.append({"ID":id,"nombre":nombre,"especie":especie,"edad":edad,"citas":citas,"alimento":alimento,"cantidad":cantidad,"vacunas":vacunas})            

def ModificarAnimales():
    id=input("ID de el animal que desea editar: ")
    columna=input("columna que desea editar: ")
    NuevoDato=input("Ingrese el nuevo dato: ")
    Animales[int(id)][columna]=NuevoDato
def Alimento():
    for animal in Animales:
        print(f"| {animal['nombre'],animal['especie'],animal['alimento'],animal['cantidad']}|")

def ModificarAlimentos():
    for animal in Animales:
        print(f"| {animal['ID'],animal['alimento'],animal['cantidad']}|")
    id=input("ID de el animal que desea editar: ")
    columna=input("columna que desea editar: ")
    NuevoDato=input("Ingrese el nuevo dato: ")
    Animales[int(id)][columna]=NuevoDato

def GetCitas():
    for animal in Animales:
        print(f"| {animal['ID'],animal['nombre'],animal['especie'],animal['edad'],animal['citas']}|")

def ModificarCitas():
    for animal in Animales:
        print(f"| {animal['ID'],animal['nombre'],animal['especie'],animal['edad'],animal['citas']}|")
    id=input("ID de el animal que desea editar: ")
    columna=input("columna que desea editar: ")
    NuevoDato=input("Ingrese el nuevo dato: ")
    Animales[int(id)][columna]=NuevoDato

def GetVacunas():
    for animal in Animales:
        print(f"| {animal['ID'],animal['nombre'],animal['especie'],animal['vacunas']}|")
