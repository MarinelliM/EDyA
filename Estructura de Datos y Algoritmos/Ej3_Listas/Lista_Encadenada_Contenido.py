class Nodo:
    __nodo: None
    __siguiente: None

    def __init__(self, nodo) -> None:
        self.__nodo = nodo
        self.__siguiente = None

    def getnodo(self):
        return self.__nodo
    
    def setnodo(self, elemento):
        self.__nodo = elemento
    
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
            while aux != None and elemento > aux.getnodo():
                anterior = aux
                aux = aux.getsiguiente()
            if anterior == None:
                nuevo.setsiguiente(aux)
                self.__cabeza = nuevo
                self.__cantidad += 1
            else:
                nuevo.setsiguiente(aux)
                anterior.setsiguiente(nuevo)
                self.__cantidad += 1

    '''def insertar(self, elemento):
        nuevo = Nodo(elemento)
        if self.vacio():
            self.__cabeza = nuevo
            self.__cantidad += 1
        else:
            aux = self.__cabeza
            anterior = None
            while aux != None and elemento > aux.getnodo():
                anterior = aux
                aux = aux.getsiguiente()
            nuevo.setsiguiente(aux)
            anterior.setsiguiente(nuevo)
            self.__cantidad += 1'''

    def suprimir(self, elemento):
        if self.vacio():
            print('La lista esta vacia. No se puede suprimir')
        aux = self.__cabeza
        anterior = None
        while aux != None and aux.getnodo() != elemento:
            anterior = aux
            aux = aux.getsiguiente()
        if aux == None:
            print('El elemento no se encuentra en la lista')
        elif anterior == None:
            self.__cabeza = self.__cabeza.getsiguiente()
            self.__cantidad -= 1
        else:
            anterior.setsiguiente(aux.getsiguiente())
            self.__cantidad -= 1

    def mostrar(self):
        aux = self.__cabeza
        i = 0
        while aux != None:
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
        elif anterior == None:
            print('El dato ingresado corresponde al primer elemento. No tiene anterior')
        else:
            print(f'El elemento anterior se encuentra en la posicion: {i-1} y el dato que contiene es: {str(anterior.getnodo())}')

    def siguiente(self, elemento):
        aux = self.__cabeza
        i = 0
        while aux != None and aux.getnodo() != elemento:
            aux = aux.getsiguiente()
            i += 1
        if aux == None:
            print('El elemento no se encontro en la lista')
        else:
            try:
                siguiente = aux.getsiguiente()
                print(f'El elemento siguiente se encuentra en la posicion: {i+1} y el dato es: {siguiente.getnodo()}')
            except AttributeError:
                print(f'El dato ingresado es el ultimo elemento de la lista. Este se encuentra en la posicion: {i}')

    '''-----------Otra forma es:-------------------'''
            #siguiente = aux.getsiguiente()
            #if siguiente is None:
            #    print(f'El dato ingresado se encuentra en el último elemento, que se encuentra en la posición: {i}')
            #else:
            #    print(f'El elemento siguiente se encuentra en la posición: {i+1} y el dato es: {siguiente.getnodo()}')

    def ordenar(self):
        if self.vacio():
            return  # La lista está vacía, no hay nada que ordenar
        actual = self.__cabeza
        while actual is not None:
            siguiente = actual.getsiguiente()
            while siguiente is not None:
                if actual.getnodo() > siguiente.getnodo():
                    # Intercambiar los valores de los nodos
                    temp = actual.getnodo()
                    actual.setnodo(siguiente.getnodo())
                    siguiente.setnodo(temp)
                siguiente = siguiente.getsiguiente()
            actual = actual.getsiguiente()

    
