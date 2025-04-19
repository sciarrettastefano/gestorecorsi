from dataclasses import dataclass


@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str
    # corsi: list[Corso] = None  #---> pattern ORM
    # codins: list[str] = None   #---> pattern ORM

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)

    def __str__(self):
        return f"{self.cognome} {self.nome} ({self.matricola}) - {self.CDS}"
