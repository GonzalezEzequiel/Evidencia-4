class PatinElectrico:
    def __init__(self):
        self.modelo = 'Segway'
        self.encendida = False
        self.velocidad = 0
        self.autonomia = 6.5  # horas
        self.aceleracion = 10  # km/h
        self.velocidad_maxima = 40
    
    def encender(self):
        if not self.encendida:
            self.encendida = True
            print(f"Tu {self.modelo} está encendido.")
        else:
            print(f"Tu {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print(f"Tu {self.modelo} está apagado.")
        else:
            print(f"Tu {self.modelo} ya está apagado.")
        
    def _acelerar(self):
        if not self.encendida:
            raise Exception(f"El {self.modelo} debe estar encendido para acelerar.")
        
        if self.velocidad < self.velocidad_maxima:
            self.velocidad += self.aceleracion
            if self.velocidad > self.velocidad_maxima:
                self.velocidad = self.velocidad_maxima
            print(f"Acelerando... ahora vas a {self.velocidad} km/h.")
        else:
            print(f"Ya has alcanzado la velocidad máxima de {self.velocidad_maxima} km/h.")
        
        self.autonomia -= 0.1  # Reduce autonomía al acelerar
        self.verificar_autonomia()

    def _frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"Frenando... ahora vas a {self.velocidad} km/h.")
            self.autonomia -= 0.05  # Reduce autonomía también al frenar, pero solo si se ha movido
            self.verificar_autonomia()
        else:
            print("Ya estás detenido.")
    
    def verificar_autonomia(self):
        if self.autonomia <= 0:
            print(f"Tu {self.modelo} se ha quedado sin batería.")
            self.apagar()
            raise Exception(f"Debes recargar la batería de tu {self.modelo}.")
        else:
            print(f"Tu {self.modelo} tiene una autonomía de {self.autonomia:.1f} horas restantes.")
    
    def iniciar(self):
        if not self.encendida:
            raise Exception(f"Tu {self.modelo} debe estar encendido para utilizarlo.")
        if self.velocidad == 0:
            raise Exception("Debes acelerar para poder empezar a andar.")
        if self.autonomia <= 0:
            raise Exception(f"Debes recargar la batería para poder usar tu {self.modelo}.")
        
        print(f"Tu {self.modelo} está en marcha a {self.velocidad} km/h.")
        
        # Llamamos a frenar hasta que la velocidad llegue a 0, reduciendo la autonomía adecuadamente
        while self.velocidad > 0:
            self._frenar()

        print(f"Tu {self.modelo} se ha detenido.")
        self.apagar()

    def __str__(self):
        return f"{self.modelo}: {self.velocidad} km/h, encendido: {'sí' if self.encendida else 'no'}"


# Pruebas unitarias
import unittest

class TestPatinElectrico(unittest.TestCase):
    def setUp(self):
        self.patineta = PatinElectrico()

    def test_encender_apagar(self):
        # Encender la patineta solo si no está encendida
        self.patineta.encender()
        self.assertTrue(self.patineta.encendida)
        
        # Apagar la patineta solo si está encendida
        self.patineta.apagar()
        self.assertFalse(self.patineta.encendida)
        self.assertEqual(self.patineta.velocidad, 0)

    def test_acelerar(self):
        self.patineta.encender()
        
        # Acelera y verifica la velocidad
        self.patineta._acelerar()
        self.assertEqual(self.patineta.velocidad, 10)
        self.patineta._acelerar()
        self.assertEqual(self.patineta.velocidad, 20)
        self.patineta._acelerar()
        self.assertEqual(self.patineta.velocidad, 30)
        self.patineta._acelerar()
        self.assertEqual(self.patineta.velocidad, 40)  # Alcanza la velocidad máxima

        # Intenta acelerar más allá de la velocidad máxima
        self.patineta._acelerar()
        self.assertEqual(self.patineta.velocidad, 40)  # Se mantiene en la velocidad máxima

    def test_frenar(self):
        self.patineta.encender()
        
        self.patineta._acelerar()  # Aumenta a 10 km/h
        self.patineta._frenar()    # Reduce a 0 km/h
        self.assertEqual(self.patineta.velocidad, 0)

    def test_iniciar(self):
        self.patineta.encender()
        
        # Acelera hasta la velocidad máxima y luego frena completamente
        for _ in range(4):
            self.patineta._acelerar()  # Llega a 40 km/h
        
        self.patineta.iniciar()   # Inicia y reduce la velocidad a 0, apagándose
        self.assertFalse(self.patineta.encendida)  # Se apaga al detenerse

    def test_error_si_no_enciende(self):
        with self.assertRaises(Exception):
            self.patineta._acelerar()

    def test_error_si_no_autonomia(self):
        self.patineta.encender()
        self.patineta.autonomia = 0
        with self.assertRaises(Exception):
            self.patineta.iniciar()

if __name__ == '__main__':
    unittest.main()
