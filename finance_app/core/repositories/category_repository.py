import json
from uuid import UUID
from finance_app.core.models.category import Category

# ---------- Category Repository ----------
class CategoryRepository:
    """
    Repositório baseado em arquivo JSON para persistência de categorias.
    Responsável por adicionar, remover, buscar e listar objetos Category.
    """

    def __init__(self, filepath="finance_app/data/category.json"):
        """
        Inicializa o repositório com o caminho do arquivo de dados

        Args:
            filepath (str): Caminho do arquivo JSON que armazena as categorias
        """
        self._filepath = filepath


    def _load(self) -> list:
        """
        Carrega e retorna a lista de categorias do arquivo JSON.

        Returns:
            list: Lista de categorias no formato de dicionários.
        """
        try:
            with open(self._filepath, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # Arquivo ainda não existe: retorna lista vazia.
            return []
        except json.JSONDecodeError:
            # Arquivo corrompido ou vazio: trata como lista vazia
            return []
        

    def _save(self, data: list):
        """
        Salva a lista de categorias no arquivo JSON.

        Args:
            data (list): Lista de transações no formato de dicionários.
        """
        with open(self._filepath, "w") as f:
            json.dump(data, f, indent=4)

    
    def add(self, category: Category):
        """
        Adiciona uma nova categoria ao repositório.

        Args:
            category (Category): A categoria a ser adicionada.
        """
        data = self._load()
        data.append(category.to_dict())
        self._save(data)


    def delete(self, category:Category):
        """
        Deleta uma categoria do repositório com base no seu ID.

        Args:
            category (Category): A categoria a ser deletada.
        """
        data = self._load()

        # Verifica se o item existe antes de deletar
        if not [item for item in data if item["id"] == str(category.id)]:
            raise ValueError("Category not found!")
        # Remove todas as categorias com ID igual ao da fornecida.
        new_data = [item for item in data if item["id"] != str(category.id)]
        self._save(new_data)


    def get_by_id(self, id: UUID) -> Category | None:
        """
        Retorna uma categoria com base no ID.

        Args:
            id (UUID): ID da categoria

        Returns:
            Category | None: A categoria correspondente, ou None se não encontrada.
        """
        data = self._load()
        for item in data:
            if item["id"] == str(id):
                return Category.from_dict(item)
        return None
    

    def list_all(self) -> list[Category]:
        """
        Lista todas as categorias armazenadas no repositório;

        Returns:
            list: Lista de categorias (formato de dicionários).
        """
        return [Category.from_dict(item) for item in self._load()]
    

    def list_by_parent(self, id: UUID) -> list:
        """
        Lista todas as categorias cuja a categoria pai é a categoria com ID fornecido.

        Args:
            id (UUID): ID da categoria pai.

        Returns:
            list: lista de categorias com aquela categoria pai.
        """
        data = self._load()
        return [Category.from_dict(item) for item in data if item["categoria_pai"] == str(id)]
        

    def update(self, category: Category):
        """
        Atualiza uma categoria existente com base no ID.

        Args:
            category (Category): A categoria a ser atualizada

        Raises:
            ValueError: Caso a transação não seja encontrada
        """
        data = self._load()
        updated = False

        for idx, item in enumerate(data):
            if item["id"] == str(category.id):
                data[idx] = category.to_dict()
                updated = True
                break

        if updated:
            self._save(data)
        else:
            raise ValueError(f'Category with ID {category.id} not found.')