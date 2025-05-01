import uuid
from dataclasses import dataclass
from typing import Optional

@dataclass
class Category():
    """
    Representa a categoria de uma transação financeira. Existem 3 níveis hierárquicos de transação financeira
    """
    id: uuid.UUID  # Identificador único da categoria
    nome: str  # Nome da categoria
    nivel: int  # Nivel hierárquico da categoria (só pode 1, 2 ou 3)
    categoria_pai: Optional[uuid.UUID] = None  # Categoria pai (se for categoria nível 2 ou 3)

    def __post_init__(self):
        """
        Validação executada após a criação do objeto.
        Garante que a categoria é nível 1, 2 ou 3
        """
        if self.nivel not in [1, 2, 3]:
            raise ValueError("Nivel hierárquico de categoria inválido. Use 1, 2 ou 3.")
        elif self.nivel == 1 and self.categoria_pai != None:
            raise ValueError("Categoria Nível 1 não pode ter Categoria Pai.")
        elif self.nivel != 1 and self.categoria_pai == None:
            raise ValueError("Categorias de nível 2 ou 3 devem ter Categoria Pai.")
        

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da categoria
        """
        return f"[id: {self.id} - Nome: {self.nome} - Nível: {self.nivel} - Categoria Pai: {self.categoria_pai}]"
    

    def __repr__(self) -> str:
        """
        Retorna uma representação técnica da categoria
        """
        return f"Category(id={self.id!r}, nome={self.nome!r}, nivel={self.nivel}, categoria_pai={self.categoria_pai!r})"
    
    @staticmethod
    def from_dict(data: dict) -> "Category":
        """
        Cria uma instância de Category a partir de um dicionário

        Args:
            data (dict): Dicionário com os campos esperados

        Returns:
            Category: nova instância populada.
        """
        return Category(
            id=uuid.UUID(data["id"]),
            nome=data["nome"],
            nivel=data["nivel"],
            categoria_pai=uuid.UUID(data["categoria_pai"]) if data["categoria_pai"] else None
        )
    

    def to_dict(self) -> dict:
        """
        Cria um dicionário serializável a partir de um objeto Category

        Args:
            Category: instância populada

        Returns:
            dict: Dicionário com os campos esperados
        """
        return {
            "id": str(self.id),
            "nome": self.nome,
            "nivel": self.nivel,
            "categoria_pai": str(self.categoria_pai) if self.categoria_pai else None
            }
