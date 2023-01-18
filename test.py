import unittest

class TestBank(unittest.TestCase):
    #Estas son las pruebas que se tienen planeadas para revisar el funcionamiento de la herramienta


    def test_deposito(self):
        """Prueba que los depositos se hacen correctamente"""
        # Obten el saldo de una cuenta 
        # Manda a llamar la funcion de deposito
        # Llamar la funcion de revision de saldo
        # Comparar las cantidad

    def test_retiro(self):
        """Prueba que los retiros se hacen correctamente"""
        # Obten el saldo de una cuenta 
        # Manda a llamar la funcion de retiro
        # Llamar la funcion de revision de saldo
        # Comparar la cantidad

    
    def test_transferencia(self):
        """Prueba que las transferencias se hacen correctamente"""
        # Obten el saldo de 2 cuentas  
        # Manda a llamar la funcion de transferencia
        # Llamar la funcion de revision de saldo en las cuentas
        # Comparar la cantidad 

    def test_revision_de_saldo(self):
        """Prueba que las transferencias se hacen correctamente"""
        # Obten el saldo de una cuenta  
        # Manda a llamar funciones para actualizar el saldo
        # Llamar la funcion de revision de saldo
        # Comrpobar que el saldo es el correcto
    




if __name__ == '__main__':
    unittest.main()