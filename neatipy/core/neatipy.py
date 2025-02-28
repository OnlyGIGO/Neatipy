from . import NeatipyFormatter

class Neatipy():
    formatter=NeatipyFormatter()
    @staticmethod
    def neatipy_print(obj:any):
        print(Neatipy.formatter.format(obj))
