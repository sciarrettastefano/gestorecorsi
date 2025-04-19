from dataclasses import dataclass


@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int
    # studenti: list[Studente] = None # lazy initialization  #---> pattern ORM
    # matricole: list[str] = None   #---> pattern ORM

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"
