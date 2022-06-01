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
                            indica si el grafo es dirigido
        """
        self.m_num_de_nodos = num_de_nodos
        self.m_nodo = range(self.m_num_de_nodos)
		
       
        self.m_dirijido = dirijido
		
       
        self.m_lista_de_adj = {node: set() for node in self.m_nodo}      
	
  


if __name__ == "__main__":
    #### Ejemplo #####

    ##Se instancia un grafo de 5 nodos
    g = Grafo(5)
    # Se imprime la cantidad de nodos del atributo m_num_de_nodos
    print(g.m_num_de_nodos);


   
   
   