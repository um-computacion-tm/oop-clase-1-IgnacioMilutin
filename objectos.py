import unittest

class Materia:
    def __init__(self, nombre, profesores):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumno__=[]
    def obtener_profesores(self):
        return self.__profesores__
    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre
    def agregar_alumnos(self,alumno):
        self.__alumno__.append(alumno)
    def obtener_alumnos_nombres(self):
        alumnos=[]
        for alumno in self.__alumno__:
            alumnos.append(alumno.__nombre__)
        return alumnos
    
class Profesor:
    def __init__(self,nombre,cargo,legajo):
        self.__nombre__=nombre
        self.__cargo__=cargo
        self.__legajo__=legajo
    def obtener_nombre(self):
        return self.__nombre__
    def obtener_cargo(self):
        return self.__cargo__
    def obtener_legajo(self):
        return self.__legajo__
        
daniel=Profesor(nombre='Daniel',cargo='Titular',legajo=123)
elio=Profesor(nombre='Elio',cargo='JTP',legajo=456)

class Alumno:
    def __init__(self,nombre,legajo,edad,email,):
        self.__nombre__=nombre
        self.__legajo__=legajo
        self.__edad__=edad
        self.__email__=email

comp=Materia('Computacion',['daniel','walter'])
alumno1=Alumno(nombre='Camila',legajo=123,edad=21,email=None)
alumno2=Alumno(nombre='Ian',legajo=456,edad=20,email='ian@gmail.com')


class TestClases(unittest.TestCase):
    def test_materia_constructor(self):
        nombre='Computacion'
        profesores=['daniel','walter']
        comp=Materia(nombre,profesores)
        self.assertEqual(comp.__nombre__,'Computacion')
        self.assertEqual(comp.__profesores__,['daniel','walter'])
    def test_materia_obtener_profesores(self):
        nombre='Computacion'
        profesores=['daniel','walter']
        comp=Materia(nombre,profesores)
        self.assertEqual(comp.obtener_profesores(),['daniel','walter'])
    def test_materia_cambiar_nombre(self):
        nombre='Computacion'
        profesores=['daniel','walter']
        comp=Materia(nombre,profesores)
        comp.cambiar_nombre('Computacion2')
        self.assertEqual(comp.__nombre__,'Computacion2')
    def test_profesor_contructor(self):
        nombre='Daniel'
        cargo='Titular'
        legajo=123
        daniel=Profesor(nombre,cargo,legajo)
        self.assertEqual(daniel.__nombre__,'Daniel')
        self.assertEqual(daniel.__cargo__,'Titular')
        self.assertEqual(daniel.__legajo__,123)
    def test_profesor_obtener_nombre(self):
        nombre='Daniel'
        cargo='Titular'
        legajo=123
        daniel=Profesor(nombre,cargo,legajo)
        self.assertEqual(daniel.obtener_nombre(),'Daniel')
    def test_profesor_obtener_cargo(self):
        nombre='Daniel'
        cargo='Titular'
        legajo=123
        daniel=Profesor(nombre,cargo,legajo)
        self.assertEqual(daniel.obtener_cargo(),'Titular')
    def test_profesor_obtener_legajo(self):
        nombre='Daniel'
        cargo='Titular'
        legajo=123
        daniel=Profesor(nombre,cargo,legajo)
        self.assertEqual(daniel.obtener_legajo(),123)
    def test_alumno_constructor(self):
        alumno1=Alumno('Ignacio',456,20,'i.milutin@gmail.com')
        self.assertEqual(alumno1.__nombre__,'Ignacio')
        self.assertEqual(alumno1.__legajo__,456)
        self.assertEqual(alumno1.__edad__,20)
        self.assertEqual(alumno1.__email__,'i.milutin@gmail.com')
    def test_materia_obtener_alumnos_nombres(self):
        alumno1=Alumno('Ignacio',456,20,'i.milutin@gmail.com')
        alumno2=Alumno('Santiago',789,20,'s.escudero@gmail.com')
        comp=Materia('Computacion',['daniel','walter'])
        comp.agregar_alumnos(alumno1)
        comp.agregar_alumnos(alumno2)
        self.assertEqual(comp.obtener_alumnos_nombres(),['Ignacio','Santiago'])

if __name__ == '__main__':
    unittest.main()