from abc import ABCMeta
from enum import Enum

class ButtonType(str, Enum):
    PRESS = "PRESS"
    TOGGLE = "TOGGLE"
    DROPDOWN = "DROPDOWN"

class Component(metaclass=ABCMeta):
    def __init__(self):
        print(self.get_component_name() + "생성")
        
    def get_component_name(self):
        raise NotImplementedError()
    
class Button(Component):
    def get_component_name(self):
        return "버튼"
    
class Switch(Component):
    def get_component_name(self):
        return "스위치"
    
class DropDown(Component):
    def get_component_name(self):
        return "드랍다운"
    
def get_component_obj(button_type):
    if button_type == ButtonType.PRESS:
        return Button()
    elif button_type == ButtonType.TOGGLE:
        return Switch()
    elif button_type == ButtonType.DROPDOWN:
        return DropDown()

button_type = ButtonType.TOGGLE
comp1 = get_component_obj(button_type)
