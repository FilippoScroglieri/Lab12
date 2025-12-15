import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        # TODO
        self._rifugi= None
        self._sentieri= None
        self.G= nx.Graph()

    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        # TODO
        self._rifugi= DAO.read_rifugi()
        self._sentieri= DAO.read_sentieri()
        self.G.clear()
        for sentiero in self._sentieri:
            if sentiero.anno<=year:
                r1= self._rifugi[sentiero.id_rifugio1]
                r2= self._rifugi[sentiero.id_rifugio2]
                self.G.add_node(r1)
                self.G.add_node(r2)
                if sentiero.difficolta== 'facile':
                    peso= float(sentiero.distanza)
                elif sentiero.difficolta== 'media':
                    peso= float(sentiero.distanza) * 1.5
                else:
                    peso= float(sentiero.distanza) * 2
                self.G.add_edge(r1, r2, weight=peso)






    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        # TODO
        peso_min= 10000
        for u,v,data in self.G.edges(data=True):
            if data['weight'] < peso_min:
                peso_min = data['weight']

        peso_max= 0.0
        for u,v,data in self.G.edges(data=True):
            if data['weight'] > peso_max:
                peso_max = data['weight']
        return peso_min, peso_max

    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        # TODO
        minori= 0
        for u,v,data in self.G.edges(data=True):
            if data['weight'] < soglia:
                minori+=1
        maggiori= 0
        for u,v,data in self.G.edges(data=True):
            if data['weight'] > soglia:
                maggiori+=1
        return minori, maggiori


    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
