class Nodo:
    __nodo: None
    __siguiente: None

    def __init__(self, nodo) -> None:
        self.__nodo = nodo
        self.__siguiente = None

    def getnodo(self):
        return self.__nodo
    
    def getsiguiente(self):
        return self.__siguiente
    
    def setsiguiente(self, siguiente):
        self.__siguiente = siguiente

class Lista_Encadenada:
    __cabeza: Nodo
    __cantidad: int

    def __init__(self) -> None:
        self.__cabeza = None
        self.__cantidad = 0

    def vacio(self):
        return self.__cabeza == None
    
    def insertar(self, elemento):
        nuevo = Nodo(elemento)
        if self.vacio():
            self.__cabeza = nuevo
            self.__cantidad += 1
        else:
            aux = self.__cabeza
            anterior = None
            while aux.getnodo() != None and elemento > aux.getnodo():
                anterior = aux
                aux = aux.getsiguiente()
            nuevo.setsiguiente(aux)
            anterior.setsiguiente(nuevo)
            self.__cantidad += 1

    def suprimir(self, elemento):
        if self.vacio():
            print('La lista esta vacia. No se puede suprimir')
        aux = self.__cabeza
        anterior = None
        while aux.getnodo() != None and aux.getnodo() != elemento: #aux != None:
            anterior = aux
            aux = aux.getsiguiente()
        if aux.getnodo() == None: #aux == None:
            print('El elemento no se encuentra en la lista')
        else:
            anterior.setsiguiente(aux.getsiguiente())
            self.__cantidad -= 1

    def mostrar(self):
        aux = self.__cabeza
        i = 0
        while aux.getnodo() != None:#aux != None:
            print(f'El elemento {i} es: {str(aux.getnodo())}')
            aux = aux.getsiguiente()
            i += 1
        
    def anterior(self, elemento):
        aux = self.__cabeza
        anterior = None
        i = 0
        while aux != None and aux.getnodo() != elemento:
            anterior = aux
            aux = aux.getsiguiente()
            i += 1
        if aux == None:
            print('No se encontro el elemento en la lista')
        else:
            print(f'El elemento se encuentra en la posicion: {i} y el dato es: {str(anterior.getnodo())}')

    def siguiente(self, elemento):
        aux = self.__cabeza
        i = 0
        while aux != None and aux.getnodo() != elemento:
            aux = aux.getsiguiente()
            i += 1
        if aux == None:
            print('El elemento no se encontro en la lista')
        else:
            siguiente = aux.getsiguiente()
            print(f'El elemento siguiente se encuentra en la posicion: {i} y el dato es: {siguiente.getnodo()}')
            


if __name__ == '__main__':
    a = Lista_Encadenada()
    a.insertar(1)
