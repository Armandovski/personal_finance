import os
import unittest
import uuid
from finance_app.core.models.category import Category
from finance_app.core.repositories.category_repository import CategoryRepository

# ---------- Category Repository Unit Test ----------
class TestCategoryRepository(unittest.TestCase):
    """
    Testes unitários para a classe CategoryRepository.
    Verifica operações CRUD
    """

    def setUp(self):
        # Criar um arquivo temporário para testes
        os.makedirs("tests/tmp", exist_ok=True)
        self.repo = CategoryRepository(filepath="tests/tmp/categories_test.json")


    def tearDown(self):
        # Deletar o arquivo temporário
        os.remove("tests/tmp/categories_test.json")


    def test_add(self):
        """
        Deve adicionar 1 category na base de teste
        """
        c1 = Category(
            id=uuid.uuid4(),
            nome="Vivendo o agora",
            nivel=1
        )

        # Adicionar ao repositório
        self.repo.add(c1)

        # Verificar que o repositório tem 1 linha de dado
        self.assertEqual(len(self.repo.list_all()), 1)


    def test_get_by_id(self):
        """
        Deve buscar categorias por seu id
        """
        c2 = Category(
            id=uuid.uuid4(),
            nome="Vivendo o agora",
            nivel=1
        )
        c3 = Category(
            id=uuid.uuid4(),
            nome="Restaurante",
            nivel=2,
            categoria_pai=c2.id
        )

        # Adicionar as categorias ao repositório
        self.repo.add(c2)
        self.repo.add(c3)

        # Busca por id
        c2_retrieved = self.repo.get_by_id(c2.id)
        c3_retrieved = self.repo.get_by_id(c3.id)

        # Verifica se todos os campos das transações inseridas correspondem aos definidos
        self.assertEqual(c2, c2_retrieved)
        self.assertEqual(c3, c3_retrieved)


    def test_update(self):
        """
        Deve atualizar uma linha de dados
        """
        c4 = Category(
            id=uuid.uuid4(),
            nome="Vivendo o agora",
            nivel=1
        )

        # Acrescenta a categoria c4
        self.repo.add(c4)

        # Modifica o campo "nome"
        c4.nome = "Estilo de vida"
        self.repo.update(c4)

        # Verifica o nome da categoria gravada nos dados
        c4_retrieved = self.repo.get_by_id(c4.id)
        self.assertEqual(c4_retrieved.nome, "Estilo de vida")


    def test_update_no_id(self):
        """
        Deve atualizar uma linha de dados cujo id não existe na base e retornar um erro
        """
        cx = Category(
            id=uuid.uuid4(),
            nome="Vivendo o agora",
            nivel=1
        )
        c1 = Category(
            id=uuid.uuid4(),
            nome="Vivendo o agora",
            nivel=1
        )

        # Adicionar ao repositório
        self.repo.add(c1)

        # Verifica que retorna erro
        with self.assertRaises(ValueError):
            self.repo.update(cx)

    
    def test_delete(self):
        """
        Deve deletar uma linha de dados
        """
        c5 = Category(
            id=uuid.uuid4(),
            nome="Vivendo o agora",
            nivel=1
        )

        # Acrescenta a categoria c5 ao repo
        self.repo.add(c5)

        # Deleta a categoria c5 do repo
        self.repo.delete(c5)

        # Verifica que não há dados no repo
        self.assertEqual(len(self.repo.list_all()), 0)

    
    def test_list_by_parent(self):
        """
        Deve listar todas as transações por parente
        """
        c6 = Category(
            id=uuid.uuid4(),
            nome="Vivendo o agora",
            nivel=1
        )
        c7 = Category(
            id=uuid.uuid4(),
            nome="Restaurante",
            nivel=2,
            categoria_pai=c6.id
        )
        c8 = Category(
            id=uuid.uuid4(),
            nome="Estilo de vida",
            nivel=1
        )
        c9 = Category(
            id=uuid.uuid4(),
            nome="Carro",
            nivel=2,
            categoria_pai=c8.id
        )
        c10 = Category(
            id=uuid.uuid4(),
            nome="Gasolina",
            nivel=3,
            categoria_pai=c9.id
        )

        # Adiciona as categorias ao repo
        self.repo.add(c6)
        self.repo.add(c7)
        self.repo.add(c8)
        self.repo.add(c9)
        self.repo.add(c10)

        # Verificar que dado o id do parent, ele lista as categorias
        self.assertEqual(self.repo.list_by_parent(c6.id), [c7])
        self.assertEqual(self.repo.list_by_parent(c7.id), [])
        self.assertEqual(self.repo.list_by_parent(c8.id), [c9])
        self.assertEqual(self.repo.list_by_parent(c9.id), [c10])