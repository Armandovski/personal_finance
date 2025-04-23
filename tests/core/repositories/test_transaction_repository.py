import os
import unittest
import uuid
from datetime import date
from finance_app.core.models.transaction import Transaction
from finance_app.core.repositories.transaction_repository import TransactionRepository

class TestTransactionRepository(unittest.TestCase):
    """
    Testes unitários para a classe TransactionRepository.
    Verifica operações CRUD
    """
    def setUp(self):
        # Criar um arquivo temporário para testes
        os.makedirs("tests/tmp", exist_ok=True)
        self.repo = TransactionRepository(filepath="tests/tmp/transactions_test.json")


    def tearDown(self):
        # Deletar o arquivo temporário
        os.remove("tests/tmp/transactions_test.json")


    def test_add(self):
        """
        Deve adicionar 1 transações na base de teste
        """
        t1 = Transaction(
            id=uuid.uuid4(),
            descricao="Salário",
            valor=10000,
            data_transacao=date(2025, 4, 1),
            data_efetivacao=date(2025, 4, 1),
            conta="Itaú",
            cartao="",
            categoria_n1="Renda",
            categoria_n2="Fixa",
            categoria_n3="Salário",
            pago=False
        )

        # Adicionar ao repositório
        self.repo.add(t1)

        # Verificar que o repositório tem 1 linha de dado
        self.assertEqual(len(self.repo.list_all()), 1)


    def test_get_by_id(self):
        """
        Deve buscar transações por seu id
        """
        t2 = Transaction(
            id=uuid.uuid4(),
            descricao="Combustível",
            valor=-150.00,
            data_transacao=date(2025, 4, 1),
            data_efetivacao=date(2025, 4, 1),
            conta="Bradesco",
            cartao="",
            categoria_n1="Estilo de Vida",
            categoria_n2="Transporte",
            categoria_n3="Carro",
            pago=False
        )
        t3 = Transaction(
            id=uuid.uuid4(),
            descricao="Presente teste",
            valor=100.00,
            data_transacao=date(2025, 4, 1),
            data_efetivacao=date(2025, 5, 5),
            conta="Itaú",
            cartao="Mastercard Black",
            categoria_n1="Viver o agora",
            categoria_n2="Presentes do Mês",
            categoria_n3="",
            pago=False
        )

        # Acrescenta mais duas transações t2 e t3 na base de teste
        self.repo.add(t2)
        self.repo.add(t3)

        # Busca por id
        t2_retrieved = self.repo.get_by_id(t2.id)
        t3_retrieved = self.repo.get_by_id(t3.id)

        # Verifica se todas os campos das transações inseridas correspondem aos campos das transações buscadas por id
        self.assertEqual(t2, t2_retrieved)
        self.assertEqual(t3, t3_retrieved)

    
    def test_update(self):
        """
        Deve atualizar uma linha de dados
        """
        t4 = Transaction(
            id=uuid.uuid4(),
            descricao="Presente teste",
            valor=200.00,
            data_transacao=date(2025, 4, 1),
            data_efetivacao=date(2025, 5, 5),
            conta="Bradesco",
            cartao="Bradesco Visa Platinum",
            categoria_n1="Viver o agora",
            categoria_n2="Presentes do Mês",
            categoria_n3="",
            pago=False
        )

        # Acrescenta a transação t4
        self.repo.add(t4)

        # Modifica o campo "valor"
        t4.valor = 250.00
        self.repo.update(t4)

        # Verifica o valor da transação gravada nos dados
        t4_retrieved = self.repo.get_by_id(t4.id)
        self.assertEqual(t4_retrieved.valor, 250.00)


    def test_delete(self):
        """
        Deve deletar uma linha de dados
        """
        t5 = Transaction(
            id=uuid.uuid4(),
            descricao="Presente teste",
            valor=200.00,
            data_transacao=date(2025, 4, 1),
            data_efetivacao=date(2025, 5, 5),
            conta="Bradesco",
            cartao="Bradesco Visa Platinum",
            categoria_n1="Viver o agora",
            categoria_n2="Presentes do Mês",
            categoria_n3="",
            pago=False
        )

        # Acrescenta a transação t5 ao repo
        self.repo.add(t5)

        # Deleta a transação t5 do repo
        self.repo.delete(t5)

        # Verificar que não há transações no repo
        assert len(self.repo.list_all()) == 0


    def test_list_by_month(self):
        """
        Deve acrescentar duas transações em meses diferentes e listar as transações por mês
        """
        t6 = Transaction(
            id=uuid.uuid4(),
            descricao="Presente teste",
            valor=200.00,
            data_transacao=date(2025, 4, 1),
            data_efetivacao=date(2025, 5, 5),
            conta="Bradesco",
            cartao="Bradesco Visa Platinum",
            categoria_n1="Viver o agora",
            categoria_n2="Presentes do Mês",
            categoria_n3="",
            pago=False
        )
        t7 = Transaction(
            id=uuid.uuid4(),
            descricao="Presente teste",
            valor=200.00,
            data_transacao=date(2025, 5, 1),
            data_efetivacao=date(2025, 6, 5),
            conta="Bradesco",
            cartao="Bradesco Visa Platinum",
            categoria_n1="Viver o agora",
            categoria_n2="Presentes do Mês",
            categoria_n3="",
            pago=False
        )

        # Acrescentar as transações ao repo
        self.repo.add(t6)
        self.repo.add(t7)

        # Listar por mês
        len(self.repo.list_by_month(year=2025, month=3)) == 0
        len(self.repo.list_by_month(year=2025, month=4)) == 1
        len(self.repo.list_by_month(year=2025, month=5)) == 1
        len(self.repo.list_by_month(year=2025, month=6)) == 0


    def test_update_no_id(self):
        """
        Testa que o repositório retorne um erro caso tente atualizar uma transação sem id correspondente
        """
        t8 = Transaction(
            id=uuid.uuid4(),
            descricao="Presente teste",
            valor=200.00,
            data_transacao=date(2025, 5, 1),
            data_efetivacao=date(2025, 6, 5),
            conta="Bradesco",
            cartao="Bradesco Visa Platinum",
            categoria_n1="Viver o agora",
            categoria_n2="Presentes do Mês",
            categoria_n3="",
            pago=False
        )
        t9 = Transaction(
            id=uuid.uuid4(),
            descricao="Presente teste",
            valor=200.00,
            data_transacao=date(2025, 5, 1),
            data_efetivacao=date(2025, 6, 5),
            conta="Bradesco",
            cartao="Bradesco Visa Platinum",
            categoria_n1="Viver o agora",
            categoria_n2="Presentes do Mês",
            categoria_n3="",
            pago=False
        )

        self.repo.add(t8)

        # Verifica que retorna erro
        with self.assertRaises(ValueError):
            self.repo.update(t9)
        