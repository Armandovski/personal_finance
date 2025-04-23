import unittest
import uuid
from datetime import date
from finance_app.core.models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    """
    Testes unitários para a classe Transaction.
    Verifica instanciamento, marcação de pagamento e validação de datas.
    """

    def test_instanciacao_valida(self):
        """
        Deve instanciar corretamente uma transação válida
        e calcular o tipo com base no valor.
        """
        t = Transaction(
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
        self.assertEqual(t.descricao, "Salário")
        self.assertEqual(t.tipo, "receita")  # valor > 0 => receita
        self.assertFalse(t.pago)

    def test_marca_como_pago(self):
        """
        Deve alterar o status da transação para paga ao chamar `marcar_como_pago`.
        """
        t = Transaction(
            id=uuid.uuid4(),
            descricao="Gasolina",
            valor=-150.00,
            data_transacao=date(2025, 4, 2),
            data_efetivacao=date(2025, 4, 2),
            conta="Nubank",
            cartao="",
            categoria_n1="Transporte",
            categoria_n2="Carro",
            categoria_n3="Combustível",
            pago=False
        )
        t.marcar_como_pago()
        self.assertTrue(t.pago)  # status pago deve estar True
        self.assertEqual(t.tipo, "despesa")  # valor < 0 => despesa

    def test_data_efetivacao_invalida(self):
        """
        Deve lançar ValueError quando a data de efetivação for anterior à data da transação.
        """
        with self.assertRaises(ValueError):
            Transaction(
                id=uuid.uuid4(),
                descricao="Erro",
                valor=50.0,
                data_transacao=date(2025, 4, 5),
                data_efetivacao=date(2025, 4, 1),  # ← anterior: deve disparar exceção
                conta="Banco",
                cartao="",
                categoria_n1="Teste",
                categoria_n2="Erro",
                categoria_n3="Data",
                pago=False
            )

if __name__ == "__main__":
    unittest.main()
