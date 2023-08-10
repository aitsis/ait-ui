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

    def render(self):
        str_ = f"<{self.tag}"
        if self.id is not None:
            str_ += f" id='{self.id}'"
        class_str = " ".join(self.classes)
        if(len(class_str) > 0):
            str_ += f" class='{class_str}'"
        if(len(self.styles) > 0):
            style_str = " style='"
            for style_name, style_value in self.styles.items():
                style_str += f" {style_name}:{style_value};"
            str_ += style_str + "'"
        for attr_name, attr_value in self.attrs.items():
            str_ += f" {attr_name}='{attr_value}'"
        for event_name, action in self.events.items():
            str_ += self.get_client_handler_str(event_name)
        str_ += ">"
        for child in self.children:
            str_ += child.render()
        str_ += f"</{self.tag}>"
        return str_