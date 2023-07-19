class UI:
    def __init__(self, main):
        self.header_items = {}
        self.scripts = {}
        self.styles = {}
        self.main = main

    def add_header_item(self, item):
        self.header_items[item.id] = item
    
    def add_script(self, script):
        self.scripts[script.id] = script

    def add_style(self, style):
        self.styles[style.id] = style

    def render(self):
        return self.main.render()