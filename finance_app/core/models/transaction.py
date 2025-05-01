from dataclasses import dataclass
from datetime import date
import uuid

@dataclass
class Transaction:
    """
    Representa uma transação financeira com valor, data, categorias e status de pagamento.
    """

    id: uuid.UUID  # Identificador único da transação
    descricao: str  # Descrição da transação
    valor: float  # Valor monetário (positivo para receita, negativo para despesa)
    data_transacao: date  # Data em que a transação foi criada
    data_efetivacao: date  # Data em que a transação foi efetivada
    conta: str  # Conta associada à transação
    cartao: str  # Cartão utilizado, se aplicável
    categoria_n1: str  # Categoria principal (ex: Alimentação)
    categoria_n2: str  # Subcategoria (ex: Restaurante)
    categoria_n3: str  # Sub-subcategoria (ex: Delivery)
    pago: bool = False  # Flag indicando se a transação foi paga

    def __post_init__(self):
        """
        Validação executada após a criação do objeto.
        Garante que a data de efetivação não seja anterior à data da transação.
        """
        if self.data_efetivacao < self.data_transacao:
            raise ValueError("Data da efetivação não pode ser anterior à data da transação")

    @property
    def tipo(self) -> str:
        """
        Retorna o tipo da transação com base no valor.
        - receita: valor positivo
        - despesa: valor negativo
        - neutro: valor zero
        """
        if self.valor > 0:
            return "receita"
        elif self.valor < 0:
            return "despesa"
        return "neutro"

    def marcar_como_pago(self):
        """
        Marca a transação como paga.
        """
        self.pago = True

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da transação.
        Ex: [Supermercado] - R$ -150.00 em 05/04/2025 (pago: True)
        """
        return f"[{self.descricao}] - R$ {self.valor:.2f} em {self.data_transacao.strftime('%d/%m/%Y')} (pago: {self.pago})"

    def __repr__(self) -> str:
        """
        Retorna uma representação técnica da transação, útil para debugging.
        """
        return (f"Transaction(id={self.id}, valor={self.valor}, "
                f"descricao='{self.descricao}', pago={self.pago})")
    
    def to_dict(self) -> dict:
        """
        Converte a transação para um dicionário serializável (por exemplo, para JSON).
        """
        return {
            "id": str(self.id),
            "descricao": self.descricao,
            "data_transacao": self.data_transacao.isoformat(),
            "data_efetivacao": self.data_efetivacao.isoformat(),
            "valor": self.valor,
            "conta": self.conta,
            "cartao": self.cartao,
            "categoria_n1": self.categoria_n1,
            "categoria_n2": self.categoria_n2,
            "categoria_n3": self.categoria_n3,
            "pago": self.pago
        }
    
    @staticmethod # Wrapper que basicamente passa o 'self' automaticamente, já que não colocamos o 'self' na função
    def from_dict(data: dict) -> "Transaction":
        """
        Cria uma instância de Transaction a partir de um dicionário.
        
        Args:
            data (dict): Dicionário com os campos esperados.

        Returns:
            Transaction: nova instância populada.
        """
        return Transaction(
            id=uuid.UUID(data["id"]),
            descricao=data["descricao"],
            data_transacao=date.fromisoformat(data["data_transacao"]),
            data_efetivacao=date.fromisoformat(data["data_efetivacao"]),
            valor=data["valor"],
            conta=data["conta"],
            cartao=data["cartao"],
            categoria_n1=data["categoria_n1"],
            categoria_n2=data["categoria_n2"],
            categoria_n3=data["categoria_n3"],
            pago=data["pago"]
        )

