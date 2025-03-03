from . import NeatipyFormatter


class Neatipy:
    formatter = NeatipyFormatter()

    @staticmethod
    def nprint(*args: any, **kwargs: any) -> None:
        print(
            *(Neatipy.formatter.format(a) for a in args), **kwargs
        )  # Unpacks the formatted args and prints them, using generator expression to avoid creating a list
