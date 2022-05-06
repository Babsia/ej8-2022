from manejadorconjuntos import manejador

class menuu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.salir,
            }
        self.__M=manejador()
        self.__M.testing()
        

    def getSwitcher(self):
        return self.__switcher

    def opcion(self,op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        i1=int(input("ingrese el numero de conjunto a unir: "))
        i2=int(input("ingrese el segundo numero de conjunto a unir: "))
        i1-=1
        i2-=1
        f=self.__M.manejadorunion(i1,i2)
        f.mostrar()
    
    def opcion2(self):
        i1=int(input("ingrese el numero de conjunto: "))
        i2=int(input("ingrese el segundo numero de conjunto para hacer la diferencia: "))
        i1-=1
        i2-=1
        h=self.__M.manejadordif(i1,i2)
        h.mostrar()
    
    def opcion3(self):
        i1=int(input("ingrese el numero de conjunto: "))
        i2=int(input("ingrese el segundo numero de conjunto para comprobar igualdad: "))
        i1-=1
        i2-=1
        t=self.__M.manejadoreq(i1,i2)
        if (t==True):
            print("los conjuntos son iguales")
        else:
            print("los conjuntos son distintos")
    def mostrar(self):
        self.__M.mostrar2()
