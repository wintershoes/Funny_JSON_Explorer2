import json
from strategy import TreeStrategy, RectangleStrategy
from icon import FactoryProducer
from component import Composite, Leaf

class StrategyBuilder:
    def __init__(self, json_file, style='rectangle', icon='default'):
        self.json_file = json_file
        self.style = style
        self.icon = icon
        self.strategy = None
        self.json_data = None

    def choose_icon_factory(self):
        factory = FactoryProducer()
        return factory.create_icon_factory(self.icon)

    def choose_strategy(self, icon_factory):
        if self.style == 'tree':
            return TreeStrategy(icon_factory)
        elif self.style == 'rectangle':
            return RectangleStrategy(icon_factory)

    def load_data(self):
        with open(self.json_file, 'r') as file:
            self.json_data = json.load(file)

    def build_composite(self, name, data):
        if isinstance(data, dict) or isinstance(data, list):
            composite = Composite(name)
            if isinstance(data, dict):
                items = list(data.items())
                for i, (key, value) in enumerate(items):
                    composite.add(self.build_composite(key, value))
            return composite
        else:
            return Leaf(name, data)

    def execute_strategy(self):
        icon_factory = self.choose_icon_factory()
        self.strategy = self.choose_strategy(icon_factory)
        self.load_data()
        root = self.build_composite('root', self.json_data)
        arg_list = []
        for node, (level, endofparent, startofparent) in root:
            arg_list.insert(0, startofparent)
            self.strategy.display(node, level, endofparent, arg_list)
        self.strategy.display(node, level, endofparent, arg_list,terminal=True)