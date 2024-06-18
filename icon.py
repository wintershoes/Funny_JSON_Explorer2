from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_icon_factory(self):
        pass

class FactoryProducer(AbstractFactory):
    def create_icon_factory(self,style):
        if style == 'poker':
            return PokerFaceIconFactory()
        elif style == 'default':
            return DefaultIconFactory()

class PokerFaceIconFactory():
    def get_middle_icon(self):
        return "♢"

    def get_leaf_icon(self):
        return "♤"


class DefaultIconFactory():
    def get_middle_icon(self):
        return '○'

    def get_leaf_icon(self):
        return '●'