from ait_ui.elements import Element

class Component(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value