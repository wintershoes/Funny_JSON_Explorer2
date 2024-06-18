from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def __init__(self, root):
        pass
    @abstractmethod
    def __iter__(self):
        pass
    @abstractmethod
    def __next__(self):
        pass

