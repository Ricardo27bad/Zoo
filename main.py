from Animales import *
import os
while True:
    print("╔════════════════════╗")
    print("║--------MENU--------║")
    print("║1...........Animales║\n║2...........Alimento║\n║3............Vacunas║\n║4....tiempo en patio║\n║5..............Salir║")
    print("╚════════════════════╝")
    op =input(":_")

    if(int(op)==1):
        print("╔════════════════════╗")
        print("║------Animales------║")
        print("║1............Agregar║\n║2...........Eliminar║\n║3..........Modificar║\n║4...............Leer║\n║5..............Salir║")
        print("╚════════════════════╝")
        opc =input(":_")
        if(int(opc)==1):
            postAnimales()
            GetAnimales()
        if(int(opc)==2):
            print(GetAnimales())
            op=input("Elija cual remover segun el ID: ")
            del Animales[int(op)+1]
            print(GetAnimales())           
        if(int(opc)==3):
            print(GetAnimales())
            print(ModificarAnimales())
            print(GetAnimales())
        if(int(opc)==4):
            print(GetAnimales())
    if(int(op)==2):
        print("╔════════════════════╗")
        print("║-----Alimentos------║")
        print("║1................ver║\n║2.............Editar║\n║3..............Salir║")
        print("╚════════════════════╝")
        opc =input(":_")
        if(int(opc)==1):
            print(Alimento())
        if(int(opc)==2):
            print(ModificarAlimentos())
            print(Alimento())
    if(int(op)==3):
        print("╔════════════════════╗")
        print("║-------Citas--------║")
        print("║1...............Leer║\n║2.............Editar║\n║3............Vacunas║\n║4..Modificar Vacunas║\n║5..............Salir║")
        print("╚════════════════════╝")
        opc =input(":_")
        if(int(opc)==1):
            print(GetCitas())
        if(int(opc)==2):
            print(ModificarCitas())
            print(GetCitas())
        if(int(opc)==3):
            print(GetVacunas())
        if(int(opc)==4):
            print(ModificarVacunas())
            print(GetVacunas())
    if(int(op)==4):
        print("╔════════════════════╗")
        print("║-------Tiempo-------║")
        print("║1...............Leer║\n║2.............Editar║\n║3..............Salir║")
        print("╚════════════════════╝")
        opc =input(":_")
        if(int(opc)==1):
            print(GetTiempoPatio())
        if(int(opc)==2):
            print(ModificarTiempoPatio())
            print(GetTiempoPatio())
    if(int(op)==5):
        print("Usted esta saliendo del sistema... Bonito día :D ")
        break