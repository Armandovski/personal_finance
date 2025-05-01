import unittest
import uuid
from finance_app.core.models.category import Category

class TestCategory(unittest.TestCase):

    def test_cat_1_valida(self):
        """
        Testa a criação de uma categoria nivel 1 válida.
        """
        cat1 = Category(
            id=uuid.uuid4(),
            nome="Teste: Cat 1 Teste",
            nivel=1,
            categoria_pai=None
        )
        self.assertEqual(cat1.nome, "Teste: Cat 1 Teste")
        self.assertEqual(cat1.nivel, 1)
        self.assertIsNone(cat1.categoria_pai)


    def test_cat_1_sem_pai(self):
        """
        Testa que uma categoria nivel 1 não pode ter pai
        """
        with self.assertRaises(ValueError):
            Category(
                id=uuid.uuid4(),
                nome="Teste: Cat 1 com pai deve dar Erro",
                nivel=1,
                categoria_pai=uuid.uuid4() # ← cat nivel 1 com pai deve disparar exceção
            )


    def test_cat_2_valida(self):
        """
        Testa a criação de uma categoria nivel 2 válida.
        """
        cat1 = Category(
            id=uuid.uuid4(),
            nome="Teste: Cat 1 Teste",
            nivel=1,
            categoria_pai=None
        )
        cat2 = Category(
            id=uuid.uuid4(),
            nome="Teste: Cat 2 Teste",
            nivel=2,
            categoria_pai=cat1.id
        )
        self.assertEqual(cat2.nome, "Teste: Cat 2 Teste")
        self.assertEqual(cat2.nivel, 2)
        self.assertEqual(cat2.categoria_pai, cat1.id)

    
    def test_cat_2_sem_pai(self):
        """
        Testa que uma categoria nivel 2 deve ter pai
        """
        with self.assertRaises(ValueError):
            Category(
                id=uuid.uuid4(),
                nome="Teste: Cat 2 sem pai deve dar Erro",
                nivel=2,
                categoria_pai=None # ← cat nivel 2 sem pai deve disparar exceção
            )

    
    def test_cat_3_valida(self):
        """
        Testa a criação de uma categoria nivel 3 válida.
        """
        cat1 = Category(
            id=uuid.uuid4(),
            nome="Teste: Cat 1 Teste",
            nivel=1,
            categoria_pai=None
        )
        cat2 = Category(
            id=uuid.uuid4(),
            nome="Teste: Cat 2 Teste",
            nivel=2,
            categoria_pai=cat1.id
        )
        cat3 = Category(
            id=uuid.uuid4(),
            nome="Teste: Cat 3 Teste",
            nivel=3,
            categoria_pai=cat2.id
        )
        self.assertEqual(cat3.nome, "Teste: Cat 3 Teste")
        self.assertEqual(cat3.nivel, 3)
        self.assertEqual(cat3.categoria_pai, cat2.id)

    
    def test_cat_3_sem_pai(self):
        """
        Testa que uma categoria nivel 3 deve ter pai
        """
        with self.assertRaises(ValueError):
            Category(
                id=uuid.uuid4(),
                nome="Teste: Cat 3 sem pai deve dar Erro",
                nivel=3,
                categoria_pai=None # ← cat nivel 3 sem pai deve disparar exceção
            )

    
    def test_cat_nivel_invalido(self):
        """
        Testa que uma categoria que não tenha nivel 1, 2 ou 3 seja inválido
        """
        with self.assertRaises(ValueError):
            Category(
                id=uuid.uuid4(),
                nome="Teste: Cat nivel inválido deve dar erro",
                nivel=0,
                categoria_pai=None
            )
        with self.assertRaises(ValueError):
            Category(
                id=uuid.uuid4(),
                nome="Teste: Cat nivel inválido deve dar erro",
                nivel=-1,
                categoria_pai=None
            )
        with self.assertRaises(ValueError):
            Category(
                id=uuid.uuid4(),
                nome="Teste: Cat nivel inválido deve dar erro",
                nivel=4,
                categoria_pai=None
            )


    def test_categoria_to_dict_e_from_dict(self):
        """
        Testa que uma categoria possa ser transformada de um objeto para dict, e de volta para objeto
        """
        cat1 = Category(
            id=uuid.uuid4(),
            nome="Teste: Cat 1 Teste",
            nivel=1,
            categoria_pai=None
        )
        cat1_dict = cat1.to_dict()
        cat1_back = Category.from_dict(cat1_dict)

        self.assertEqual(cat1_back, cat1)


if __name__ == "__main__":
    unittest.main()