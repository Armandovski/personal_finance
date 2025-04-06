import unittest
import uuid
from datetime import date
from finance_app.core.models.transaction import Transaction
import sys
print("\n### sys.path ###")
for p in sys.path:
    print(p)
print("################\n")



class TestTransaction(unittest.TestCase):

    def test_instanciacao_valida(self):
        t = Transaction(
            id = uuid.uuid4(),
            descricao = "Salário",
            valor = 10000,
            data_transacao = date(2025, 4, 1),
            data_efetivacao = date(2025, 4, 1),
            conta = "Itaú",
            cartao = "",
            categoria_n1 = "Renda",
            categoria_n2 = "Fixa",
            categoria_n3 = "Salário",
            pago = False
        )
        self.assertEqual(t.descricao, "Salário")
        self.assertEqual(t.tipo, "receita")
        self.assertFalse(t.pago)

    def test_marca_como_pago(self):
        t = Transaction(
            id = uuid.uuid4(),
            descricao = "Gasolina",
            valor = -150.00,
            data_transacao = date(2025, 4, 2),
            data_efetivacao = date(2025, 4, 2),
            conta = "Nubank",
            cartao = "",
            categoria_n1 = "Transporte",
            categoria_n2 = "Carro",
            categoria_n3 = "Combustível",
            pago = False
        )
        t.marcar_como_pago()
        self.assertTrue(t.pago)
        self.assertEqual(t.tipo, "despesa")

    def test_data_efetivacao_invalida(self):
        with self.assertRaises(ValueError):
            Transaction(
                id = uuid.uuid4(),
                descricao = "Erro",
                valor = 50.0,
                data_transacao = date(2025, 4, 5),
                data_efetivacao= date(2025, 4, 1), # anterior!
                conta = "Banco",
                cartao = "",
                categoria_n1 = "Teste",
                categoria_n2 = "Erro",
                categoria_n3 = "Data",
                pago = False
            )

        
if __name__ == "__main__":
    unittest.main()