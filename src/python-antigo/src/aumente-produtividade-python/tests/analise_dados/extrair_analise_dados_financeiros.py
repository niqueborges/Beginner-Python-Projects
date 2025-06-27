import unittest
import pandas as pd
import os
from yfinance import download

class TestStockDataAnalysis(unittest.TestCase):

    def setUp(self):
        """Configuração inicial para os testes."""
        self.ticker = "AAPL"
        self.data = download(self.ticker, period="1y")
        self.data.index = pd.to_datetime(self.data.index)

    def test_data_download(self):
        """Teste para verificar se os dados foram baixados corretamente."""
        self.assertFalse(self.data.empty, "Os dados não foram baixados corretamente.")
        self.assertIn("Adj Close", self.data.columns, "A coluna 'Adj Close' não foi encontrada nos dados.")

    def test_calculate_daily_return(self):
        """Teste para verificar o cálculo de retorno diário."""
        self.data["Daily Return"] = self.data["Adj Close"].pct_change()
        self.assertIn("Daily Return", self.data.columns, "A coluna 'Daily Return' não foi adicionada aos dados.")
        self.assertFalse(self.data["Daily Return"].isnull().all(), "Os retornos diários não foram calculados corretamente.")

    def test_calculate_statistics(self):
        """Teste para verificar o cálculo de estatísticas."""
        self.data["Daily Return"] = self.data["Adj Close"].pct_change()
        average_daily_return = self.data["Daily Return"].mean()
        maximum_daily_return = self.data["Daily Return"].max()
        minimum_daily_return = self.data["Daily Return"].min()

        self.assertIsInstance(average_daily_return, float, "O retorno médio diário não é um número decimal.")
        self.assertIsInstance(maximum_daily_return, float, "O retorno diário máximo não é um número decimal.")
        self.assertIsInstance(minimum_daily_return, float, "O retorno diário mínimo não é um número decimal.")

    def test_csv_export(self):
        """Teste para verificar se os dados são exportados para CSV."""
        filename = "daily_stock_prices.csv"
        self.data.to_csv(filename, index=True)
        self.assertTrue(os.path.exists(filename), "O arquivo CSV não foi criado.")
        
        # Verificar se o arquivo contém dados
        exported_data = pd.read_csv(filename)
        self.assertFalse(exported_data.empty, "O arquivo CSV está vazio.")

        # Limpar o arquivo gerado para manter o ambiente de teste limpo
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
