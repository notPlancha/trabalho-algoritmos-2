class Vertex:
    def __init__(self, e):
        self.__element = e

    @property
    def id(self):
        return hash(self)

    @property
    def element(self):
        return self.__element

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return f"Vertex({str(self.__element)})"

    def __repr__(self):
        return str(self)