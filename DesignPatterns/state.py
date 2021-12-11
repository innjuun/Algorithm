from abc import ABCMeta, abstractmethod
from enum import Enum

class ModeType(str, Enum):
    DARK = "DARK"
    LIGHT = "LIGHT"

class ModeSwitch:
    def __init__(self, mode_type):
        self.mode_state = self._set_mode_state(mode_type)

    def _set_mode_state(self, mode_type):
        # 일종의 팩터리 메서드 .. !
        if mode_type == ModeType.LIGHT:
            self.mode_state = ModeStateLight()
        elif mode_type == ModeType.DARK:
            self.mode_state = ModeStateDark()
        
    def set_state(self, mode_state_cls: "ModeState"):
        self.mode_state = mode_state_cls()
    
    def on_switch(self):
        self.mode_state.toggle(self)
    
class ModeState(metaclass=ABCMeta):
    @abstractmethod
    def toggle(self, mode_switch: ModeSwitch):
        raise NotImplementedError()
    
class ModeStateDark(ModeState):
    def toggle(self, mode_switch: ModeSwitch):
        print("FROM DARK TO LIGHT")
        # state 전환
        mode_switch.set_state(ModeStateLight)

class ModeStateLight(ModeState):
    def toggle(self, mode_switch: ModeSwitch):
        print("FROM LIGHT TO DARK")
        mode_switch.set_state(ModeStateDark)

mode_switch = ModeSwitch(ModeType.DARK)

mode_switch.on_switch()
mode_switch.on_switch()
mode_switch.on_switch()
mode_switch.on_switch()