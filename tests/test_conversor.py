import unittest
from src.conversor import criar_conversor, aplicar_funcao_extra, arredondar, converter_valor, gerar_tabela

class TestConversorMoedas(unittest.TestCase):

    def test_closure_conversao_basica(self):
        conv = criar_conversor(1.0, 5.0)  # BRL -> USD
        self.assertEqual(conv(10), 50.0)

    def test_funcao_alta_ordem_arredondamento(self):
        conv = criar_conversor(6.0, 7.0)  # EUR -> GBP
        conv_round = aplicar_funcao_extra(conv, arredondar)
        self.assertEqual(conv_round(10), round(10 * (7/6), 2))

    def test_converter_valor(self):
        self.assertEqual(converter_valor("BRL", "USD", 10), 50.00)
        self.assertEqual(converter_valor("EUR", "EUR", 12.34), 12.34)

    def test_converter_valor_erros(self):
        with self.assertRaises(ValueError):
            converter_valor("XYZ", "USD", 10)
        with self.assertRaises(ValueError):
            converter_valor("USD", "XYZ", 10)
        with self.assertRaises(ValueError):
            converter_valor("USD", "BRL", -1)

    def test_gerar_tabela_tem_todas_as_moedas(self):
        tabela = gerar_tabela("BRL", 10)
        for m in ("BRL","USD","EUR","GBP"):
            self.assertIn(m, tabela)
        self.assertEqual(tabela["BRL"], 10.00)

if __name__ == "__main__":
    unittest.main()
