from dataclasses import dataclass
from datetime import date
import uuid

@dataclass
class Transaction:
    id: uuid.UUID
    descricao: str
    valor: float
    data_transacao: date
    data_efetivacao: date
    conta: str
    cartao: str
    categoria_n1: str
    categoria_n2: str
    categoria_n3: str
    pago: bool = False

    def __post_init__(self):
        if self.data_efetivacao < self.data_transacao:
            raise ValueError("Data da efetivação não pode ser anterior à data da transação")

    @property
    def tipo(self) -> str:
        if self.valor > 0:
            return "receita"
        elif self.valor < 0:
            return "despesa"
        return "neutro"

    def marcar_como_pago(self):
        self.pago = True

    def __str__(self):
        return f"[{self.descricao}] - R$ {self.valor:.2f} em {self.data_transacao.strftime('%d/%m/%Y')} (pago: {self.pago})"

    def __repr__(self):
        return (f"Transaction(id={self.id}, valor={self.valor}, "
            f"descricao='{self.descricao}', pago={self.pago})")

