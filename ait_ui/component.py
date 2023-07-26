class Component:
    def __init__(self):
        self.events = {}

    def on(self, event, callback):
        self.events[event] = callback
        return self