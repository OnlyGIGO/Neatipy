from abc import ABC, abstractmethod
class BaseFormatter(ABC):
    @staticmethod
    @abstractmethod
    def format(obj):
        """Formats the given object neatly"""
        ...
        