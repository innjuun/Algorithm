from abc import ABCMeta, abstractmethod
from enum import Enum

class ButtonType(str, Enum):
    PRESS = "PRESS"
    TOGGLE = "TOGGLE"
    DROPDOWN = "DROPDOWN"

class Component(metaclass=ABCMeta):
    def __init__(self):
        print(self.get_component_name() + "생성")
    
    @abstractmethod
    def get_component_name(self):
        raise NotImplementedError()
    
class DarkButton(Component):
    def get_component_name(self):
        return "까만 버튼"
        
class LightButton(Component):
    def get_component_name(self):
        return "하얀 버튼"

class DarkSwitch(Component):
    def get_component_name(self):
        return "까만 스위치"

class LightSwitch(Component):
    def get_component_name(self):
        return "하얀 스위치"
    
class DarkDropDown(Component):
    def get_component_name(self):
        return "까만 드랍다운"
    
class LightDropDown(Component):
    def get_component_name(self):
        return "하얀 드랍다운"


class ComponentFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def create_component_obj(self):
        raise NotImplementedError()

class LightComponentFactory(ComponentFactory):
    def create_component_obj(self, button_type):
        if button_type == ButtonType.PRESS:
            return LightButton()
        elif button_type == ButtonType.TOGGLE:
            return LightSwitch()
        elif button_type == ButtonType.DROPDOWN:
            return LightDropDown()
        
class DarkComponentFactory(ComponentFactory):
    def create_component_obj(self, button_type):
        if button_type == ButtonType.PRESS:
            return DarkButton()
        elif button_type == ButtonType.TOGGLE:
            return DarkSwitch()
        elif button_type == ButtonType.DROPDOWN:
            return DarkDropDown()

button_type = ButtonType.TOGGLE
comp1 = DarkComponentFactory().create_component_obj(button_type)
