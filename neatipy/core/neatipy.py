from . import NeatipyFormatter

class Neatipy():
    formatter=NeatipyFormatter()
    @staticmethod
    def neatipy_print(obj:any)->None:
        print(Neatipy.formatter.format(obj))
