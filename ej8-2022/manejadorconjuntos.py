from claseconjunto import conjunto
import csv
class manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def testing(self):
        archivo=open("conjuntos.csv")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            conj1=conjunto()
            conj1.crearlista(fila)
            self.__lista.append(conj1)
    def mostrar(self):
        print(self.__lista[0].mostrar())
    def manejadorunion(self,i1,i2):
        return self.__lista[i1]+self.__lista[i2]
    def manejadordif(self,i1,i2):
        return self.__lista[i1]-self.__lista[i2]
    def manejadoreq(self,i1,i2):
        return self.__lista[i1]==self.__lista[i2]
    def mostrar2(self):
        print("se trabajara con los siguientes conjuntos:")
        for i in range(len(self.__lista)):
            print(i+1,self.__lista[i].mostrar2())
    


    
            
    