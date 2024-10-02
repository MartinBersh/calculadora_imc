import unittest
from unittest.mock import patch, MagicMock
from calculo_imc import calcular_imc, clasificar_imc

class TestCalculoIMC(unittest.TestCase):

    @patch('calculo_imc.messagebox')
    def test_imc_valores_validos_67kg_1_85m(self, mock_messagebox):
        """
        Prueba con valores válidos: peso de 67 kg y altura de 1.85 m.
        Se espera que el IMC calculado sea aproximadamente 19.6 y la clasificación sea "Peso normal".
        """
        imc = calcular_imc(67, 1.85)
        self.assertAlmostEqual(imc, 19.6, places=1)
        self.assertEqual(clasificar_imc(imc), "Peso normal")
        mock_messagebox.showerror.assert_not_called()

    @patch('calculo_imc.messagebox')
    def test_imc_valores_validos_87kg_1_69m(self, mock_messagebox):
        """
        Prueba con valores válidos: peso de 87 kg y altura de 1.69 m.
        Se espera que el IMC calculado sea aproximadamente 30.5 y la clasificación sea "Obesidad".
        """
        imc = calcular_imc(87, 1.69)
        self.assertAlmostEqual(imc, 30.5, places=1)
        self.assertEqual(clasificar_imc(imc), "Obesidad")
        mock_messagebox.showerror.assert_not_called()

    @patch('calculo_imc.messagebox')
    def test_imc_solo_altura(self, mock_messagebox):
        """
        Prueba cuando solo se proporciona la altura y no el peso.
        Se espera que se lance un error indicando que el peso y la altura son requeridos.
        """
        self.assertIsNone(calcular_imc(76, None))
        mock_messagebox.showerror.assert_called_once_with("Error", "El peso y la altura son requeridos.")

    @patch('calculo_imc.messagebox')  # Simulación de messagebox para la siguiente prueba.
    def test_imc_solo_peso(self, mock_messagebox):
        """
        Prueba cuando solo se proporciona el peso y no la altura.
        Se espera que se lance un error indicando que el peso y la altura son requeridos.
        """
        self.assertIsNone(calcular_imc(None, 1.77))
        mock_messagebox.showerror.assert_called_once_with("Error", "El peso y la altura son requeridos.")

    @patch('calculo_imc.messagebox')
    def test_imc_valores_zero(self, mock_messagebox):
        """
        Prueba cuando el peso y la altura son 0.
        Se espera que se lance un error indicando que ambos valores deben ser positivos.
        """
        self.assertIsNone(calcular_imc(0, 0))
        mock_messagebox.showerror.assert_called_once_with("Error", "El peso y la altura deben ser valores positivos.")

    @patch('calculo_imc.messagebox')
    def test_imc_valores_negativos(self, mock_messagebox):
        """
        Prueba cuando se proporcionan valores negativos para el peso.
        Se espera que se lance un error indicando que los valores deben ser positivos.
        """
        self.assertIsNone(calcular_imc(-45, 1.56))
        mock_messagebox.showerror.assert_called_once_with("Error", "El peso y la altura deben ser valores positivos.")

if __name__ == '__main__':
    unittest.main()
