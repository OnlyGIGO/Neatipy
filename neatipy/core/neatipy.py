from . import NeatipyFormatter


class Neatipy:
    formatter = NeatipyFormatter()

    @staticmethod
    def nprint(obj: any) -> None:
        print(Neatipy.formatter.format(obj))
