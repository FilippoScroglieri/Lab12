import datetime
from dataclasses import dataclass



@dataclass
class Sentiero:
    id:int
    id_rifugio1:int
    id_rifugio2:int
    distanza: float
    difficolta: str
    durata: datetime.time
    anno: int

    def __str__(self):
        return (f'Sentiero: {self.id_rifugio1} - {self.id_rifugio2},'
                f'distanza: {self.distanza},'
                f'difficolta: {self.difficolta},'
                f'durata: {self.durata}')
    def __repr__(self):
        return (f'Sentiero: {self.id_rifugio1} - {self.id_rifugio2},'
                f'distanza: {self.distanza},'
                f'difficolta: {self.difficolta},'
                f'durata: {self.durata}')
    def __hash__(self):
        return hash(self.id)