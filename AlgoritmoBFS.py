from queue import Queue

class Grafo:
    """
    Una clase que representa un grafo

    ...

    Atributos
    ----------
    m_num_de_nodos : entero
                número de nodos del grafo
    m_nodo : rango
                conjunto de nodos que contiene el grafo
    m_dirijido : booleano
                indica si el grafo es dirigido o no

    m_lista_de_adj: diccionario
                contiene la lista de adyacencia del grafo

    """

    def __init__(self, num_de_nodos, dirijido=True):
        """
        Constructor utilizado para instanciar el objeto grafo

        Parámetros
        -----------
            num_de_nodos: entero
                            número de nodos del grafo
            dirijido:   
                            indica si el grafo es dirigido,
                            valor por defecto es verdadero
        """
        self.m_num_de_nodos = num_de_nodos
        self.m_nodo = range(self.m_num_de_nodos)
		
       
        self.m_dirijido = dirijido
		
       
        self.m_lista_de_adj = {node: set() for node in self.m_nodo}      
    
    def aumentar_enlace(self, nodo1, nodo2, peso=1):
        """
        Añade enlace al grafo

        Parámetros
        ----------
        nodo1 : entero
                nodo que formará el nuevo enlace
        nodo2 : entero
                nodo que será parte del nuevo enlace

        peso : entero, omitible
                valor numérico asignado al enlace

        Devuelve
        --------
        No devuelve
        """
        self.m_lista_de_adj[nodo1].add((nodo2, peso))

        if not self.m_dirijido:
            self.m_lista_de_adj[nodo2].add((nodo1, peso))
	
    def mostrar_lista_de_adj(self):
        """
        Muestra la representación del grafo.

        Parámetros 
        ----------
        No hay parámetros

        Devuelve
        --------
        No devuelve ningún valor
        """

        for clave in self.m_lista_de_adj.keys():
            print("node", clave, ": ", self.m_lista_de_adj[clave])

    def recorrer_BEA(self, nodo_inicial):
       
        """
        muestra el recorrido del árbol usando la búsqueda de anchura

        Parámetros
        ----------
        nodo inicial : entero
                        nodo con el que comienza a recorrer


        """
        visitado = set()
        cola_de_espera = Queue()

       
        cola_de_espera.put(nodo_inicial)
        visitado.add(nodo_inicial)

        while not cola_de_espera.empty():
            
            nodo_actual = cola_de_espera.get()
            print(nodo_actual, end = " ")

           
            for (nodo_siguiente, peso) in self.m_lista_de_adj[nodo_actual]:
                if nodo_siguiente not in visitado:
                    cola_de_espera.put(nodo_siguiente)
                    visitado.add(nodo_siguiente)


if __name__ == "__main__":
    #### Ejemplo #####

    ##Se instancia un grafo de 5 nodos
    g = Grafo(6)
    # Se imprime la cantidad de nodos del atributo m_num_de_nodos
    print(g.m_num_de_nodos);
    #Se imprime los nodos que contiene el grafo
    print(g.m_nodo);
    #Se imprime los datos de los nodos
    print(g.m_lista_de_adj);

    #Se aumentan los enlaces
    g.aumentar_enlace(0, 1)
    g.aumentar_enlace(0, 2)
    g.aumentar_enlace(1, 2)
    g.aumentar_enlace(1, 4)
    g.aumentar_enlace(2, 3)
    g.aumentar_enlace(2,5)

    #Se muestra la lista de adyacencia
    g.mostrar_lista_de_adj()

    #muestra el recorrido del grafo usando búsqueda en anchura desde 1
    g.recorrer_BEA(1)



   
   
   