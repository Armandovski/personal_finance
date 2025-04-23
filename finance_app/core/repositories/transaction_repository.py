import json
from uuid import UUID
from finance_app.core.models.transaction import Transaction
from datetime import datetime

class TransactionRepository:
    """
    Repositório simples baseado em arquivo JSON para persistência de transações.
    Responsável por adicionar, remover, buscar e listar objetos Transaction.
    """

    def __init__(self, filepath="finance_app/data/transaction.json"):
        """
        Inicializa o repositório com o caminho do arquivo de dados.

        Args:
            filepath (str): Caminho do arquivo JSON que armazena as transações.
        """
        self._filepath = filepath

    def _load(self) -> list:
        """
        Carrega e retorna a lista de transações do arquivo JSON.

        Returns:
            list: Lista de transações no formato de dicionários.
        """
        try:
            with open(self._filepath, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # Arquivo ainda não existe: retorna lista vazia
            return []
        except json.JSONDecodeError:
            # Arquivo corrompido ou vazio: trata como lista vazia
            return []

    def _save(self, data: list):
        """
        Salva a lista de transações no arquivo JSON.

        Args:
            data (list): Lista de transações no formato de dicionários.
        """
        with open(self._filepath, "w") as f:
            json.dump(data, f, indent=4)

    def add(self, transaction: Transaction):
        """
        Adiciona uma nova transação ao repositório.

        Args:
            transaction (Transaction): A transação a ser adicionada.
        """
        data = self._load()
        data.append(transaction.to_dict())
        self._save(data)

    def delete(self, transaction: Transaction):
        """
        Remove uma transação existente com base no seu ID.

        Args:
            transaction (Transaction): A transação a ser removida.
        """
        data = self._load()
        # Remove todas as transações com ID igual ao da fornecida
        new_data = [item for item in data if item["id"] != str(transaction.id)]
        self._save(new_data)

    def get_by_id(self, id: UUID) -> Transaction | None:
        """
        Recupera uma transação pelo seu ID.

        Args:
            id (UUID): ID da transação.

        Returns:
            Transaction | None: A transação correspondente, ou None se não encontrada.
        """
        data = self._load()
        for item in data:
            if item["id"] == str(id):
                return Transaction.from_dict(item)
        return None

    def list_all(self) -> list:
        """
        Lista todas as transações armazenadas no repositório.

        Returns:
            list: Lista de transações (formato de dicionários).
        """
        return self._load()

    def list_by_month(self, year: int, month: int) -> list:
        """
        Lista transações filtradas por ano e mês.

        Args:
            year (int): Ano desejado.
            month (int): Mês desejado.

        Returns:
            list: Lista de transações no período especificado.
        """
        data = self._load()
        # Aqui assumimos que os campos 'year' e 'month' existem no dict salvo
        return [item for item in data if datetime.strptime(item["data_transacao"], "%Y-%m-%d").year  == year and datetime.strptime(item["data_transacao"], "%Y-%m-%d").month == month]

    def update(self, transaction: Transaction):
        """
        Atualiza uma transação existente com base no ID.

        Args:
            transaction (Transaction): Transação com os dados atualizados.

        Raises:
            ValueError: Caso a transação não seja encontrada.
        """
        data = self._load()
        updated = False

        for idx, item in enumerate(data):
            if item["id"] == str(transaction.id):
                data[idx] = transaction.to_dict()
                updated = True
                break

        if updated:
            self._save(data)
        else:
            raise ValueError(f'Transaction with ID {transaction.id} not found.')

