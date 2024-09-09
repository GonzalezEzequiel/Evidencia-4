class PatinElectrico:
    def __init__(self):
        self.__modelo = 'Segway'
        self.__encendida = False
        self.__velocidad = 0
        self.__autonomia = 6.5  # horas
        self.__aceleracion = 10  # km/h
        self.__velocidad_maxima = 40

    # Getters
    def get_modelo(self):
        return self.__modelo

    def get_encendida(self):
        return self.__encendida

    def get_velocidad(self):
        return self.__velocidad

    def get_autonomia(self):
        return self.__autonomia

    def get_aceleracion(self):
        return self.__aceleracion

    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

    # Setters
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_encendida(self, estado):
        self.__encendida = estado

    def set_velocidad(self, velocidad):
        if velocidad <= self.__velocidad_maxima:
            self.__velocidad = velocidad
        else:
            print(f"No se puede exceder la velocidad máxima de {self.__velocidad_maxima} km/h.")

    def set_autonomia(self, autonomia):
        self.__autonomia = autonomia

    def set_aceleracion(self, aceleracion):
        self.__aceleracion = aceleracion

    def set_velocidad_maxima(self, velocidad_maxima):
        self.__velocidad_maxima = velocidad_maxima

    # Métodos de control
    def encender(self):
        if not self.__encendida:
            self.__encendida = True
            print(f"Tu {self.__modelo} está encendido.")
        else:
            print(f"Tu {self.__modelo} ya está encendido.")

    def apagar(self):
        if self.__encendida:
            self.__encendida = False
            print(f"Tu {self.__modelo} está apagado.")
        else:
            print(f"Tu {self.__modelo} ya está apagado.")
        
    def _acelerar(self):
        if not self.__encendida:
            raise Exception(f"El {self.__modelo} debe estar encendido para acelerar.")
        
        if self.__velocidad < self.__velocidad_maxima:
            self.__velocidad += self.__aceleracion
            if self.__velocidad > self.__velocidad_maxima:
                self.__velocidad = self.__velocidad_maxima
            print(f"Acelerando... ahora vas a {self.__velocidad} km/h.")
        else:
            print(f"Ya has alcanzado la velocidad máxima de {self.__velocidad_maxima} km/h.")
        
        self.__autonomia -= 0.1  # Reduce autonomía al acelerar
        self.verificar_autonomia()

    def _frenar(self):
        if self.__velocidad > 0:
            self.__velocidad -= 10
            if self.__velocidad < 0:
                self.__velocidad = 0
            print(f"Frenando... ahora vas a {self.__velocidad} km/h.")
            self.__autonomia -= 0.05  # Reduce autonomía también al frenar, pero solo si se ha movido
            self.verificar_autonomia()
        else:
            print("Ya estás detenido.")
    
    def verificar_autonomia(self):
        if self.__autonomia <= 0:
            print(f"Tu {self.__modelo} se ha quedado sin batería.")
            self.apagar()
            raise Exception(f"Debes recargar la batería de tu {self.__modelo}.")
        else:
            print(f"Tu {self.__modelo} tiene una autonomía de {self.__autonomia:.1f} horas restantes.")
    
    def iniciar(self):
        if not self.__encendida:
            raise Exception(f"Tu {self.__modelo} debe estar encendido para utilizarlo.")
        if self.__velocidad == 0:
            raise Exception("Debes acelerar para poder empezar a andar.")
        if self.__autonomia <= 0:
            raise Exception(f"Debes recargar la batería para poder usar tu {self.__modelo}.")
        
        print(f"Tu {self.__modelo} está en marcha a {self.__velocidad} km/h.")
        
        # Llamamos a frenar hasta que la velocidad llegue a 0, reduciendo la autonomía adecuadamente
        while self.__velocidad > 0:
            self._frenar()

        print(f"Tu {self.__modelo} se ha detenido.")
        self.apagar()

    def __str__(self):
        return f"{self.__modelo}: {self.__velocidad} km/h, encendido: {'sí' if self.__encendida else 'no'}"

# Pruebas unitarias
import unittest

class TestPatinElectrico(unittest.TestCase):
    def setUp(self):
        self.patineta = PatinElectrico()

    def test_encender_apagar(self):
        self.patineta.encender()
        self.assertTrue(self.patineta.get_encendida())
        
        self.patineta.apagar()
        self.assertFalse(self.patineta.get_encendida())
        self.assertEqual(self.patineta.get_velocidad(), 0)

    def test_acelerar(self):
        self.patineta.encender()
        
        self.patineta._acelerar()
        self.assertEqual(self.patineta.get_velocidad(), 10)
        self.patineta._acelerar()
        self.assertEqual(self.patineta.get_velocidad(), 20)
        self.patineta._acelerar()
        self.assertEqual(self.patineta.get_velocidad(), 30)
        self.patineta._acelerar()
        self.assertEqual(self.patineta.get_velocidad(), 40)  # Alcanza la velocidad máxima

        self.patineta._acelerar()
        self.assertEqual(self.patineta.get_velocidad(), 40)  # Se mantiene en la velocidad máxima

    def test_frenar(self):
        self.patineta.encender()
        
        self.patineta._acelerar()  # Aumenta a 10 km/h
        self.patineta._frenar()    # Reduce a 0 km/h
        self.assertEqual(self.patineta.get_velocidad(), 0)

    def test_iniciar(self):
        self.patineta.encender()
        
        for _ in range(4):
            self.patineta._acelerar()  # Llega a 40 km/h
        
        self.patineta.iniciar()   # Inicia y reduce la velocidad a 0, apagándose
        self.assertFalse(self.patineta.get_encendida())  # Se apaga al detenerse

    def test_error_si_no_enciende(self):
        with self.assertRaises(Exception):
            self.patineta._acelerar()

    def test_error_si_no_autonomia(self):
        self.patineta.encender()
        self.patineta.set_autonomia(0)
        with self.assertRaises(Exception):
            self.patineta.iniciar()

if __name__ == '__main__':
    unittest.main()
