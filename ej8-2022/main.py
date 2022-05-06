from Menu import menuu
if __name__ == '__main__':
    m=menuu()
    bandera = False
    while not bandera:
        print("")
        m.mostrar()
        print("d Salir")
        print("a Union ")
        print("b Diferencia ")
        print("c Igualdad ")
        opcion=(input("Ingrese una opción: "))
        m.opcion(opcion)
        bandera =(opcion)=='d'