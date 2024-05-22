"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Adrián Torres Gómez
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Estudiante:
    """
    Esta clase crea a un estudiante con sus parámetros correspondientes
    """
    nif = "11111111Z"
    curso = "Primaria"
    nombre = "Nombre"
    apellidos = "Apellidos"

    def __init__(self):
        pass;

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Se trata del __init__ de la clase
        :param nif: NIF del estudiante
        :param curso: Curso del estudiante
        :param nombre: Nombre del estudiante
        :param apellidos: Apellidos del estudiante
        """
        self.nif = nif
        self.curso = curso
        self.nombre = nombre
        self.apellidos = apellidos

    @property
    def nif(self):
        """
        NIF
        :return: Devuelve el NIF del estudiante
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        NIF
        :param value: El NIF del estudiante
        :return: Establece el NIF del estudiante
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Curso
        :return: Devuelve el curso en el que se encuentra el estudiante
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Curos
        :param value: Curso al que pertenece el estudiante
        :return: Establece el curso al que pertenece el estudiante
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Nombre
        :return: Devuelve el nombre del estudiante
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Nombre
        :param value: Nombre del estudiante
        :return: Establece el nombre del estudiante
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Apellidos
        :return: Devuelve los apellidos del estudiante
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Apellidos
        :param value: Apellidos del estudiante
        :return: Establece los apellidos del estudiante
        """
        self.__apellidos = value


class Persona(Estudiante):
    """
    Superclase Persona
    """
    def __init__(self, nif, nombre, apellidos):
        super().__init__()
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
