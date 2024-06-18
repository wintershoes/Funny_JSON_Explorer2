from component import Composite, Leaf
from abc import ABC, abstractmethod

class DisplayStrategy(ABC):
    def __init__(self, icon_creator):
        self.icon_creator = icon_creator

    @abstractmethod
    def display(self, node):
        pass


class TreeStrategy(DisplayStrategy):
    def display(self, node, node_level, last_child, extra_params, terminal=False):
        if terminal: return
        extra_params.pop(0) 
        if isinstance(node, Composite):
            icon_type = self.icon_creator.get_middle_icon()
        else:
            icon_type = self.icon_creator.get_leaf_icon()
        if node_level > 0:
            structure = ''.join('│  ' if idx in extra_params else '   ' for idx in range(1, node_level))
            structure += '└─ ' if last_child else '├─ '
            content = f"{structure}{icon_type} {node.name}"
            if isinstance(node, Leaf) and node.value is not None:
                content += f": {node.value}"
         
            print(content)
            if last_child:
                if node_level in extra_params:
                    extra_params.remove(node_level)
            else:
                if node_level not in extra_params:
                    extra_params.append(node_level)


class RectangleStrategy(DisplayStrategy):
    def display(self, node, node_level, last_child, level_starters,terminal = False):
        if terminal: 
            print('└' + '─' * 58 + '┘')
            return
        if isinstance(node, Composite):
            icon_type = self.icon_creator.get_middle_icon()
        else:
            icon_type = self.icon_creator.get_leaf_icon()

        structure = "│  " * (node_level - 1)
        if node_level > 0:
            if node_level == 1 and level_starters[0]:
                structure += '┌'
                end_mark = '┐'
            else:
                structure += '├─ '
                end_mark = '┤'
            content = structure + icon_type + ' ' + node.name
            if isinstance(node, Leaf) and node.value is not None:
                content += ':' + str(node.value)
            remaining_width = 59 - len(content)
            print(content + '─' * remaining_width + end_mark)

       
