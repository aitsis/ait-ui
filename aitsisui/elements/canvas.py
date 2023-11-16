from ..core import Element, index_gen

index_gen.add_script_source('canvas-js-lib', '<script src="js/canvas.js"></script>')

class Canvas(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "canvas"
        self.value_name = None

    def render(self):
        if id is not None:
            self.queue_for_send(self.id, self.value, "init-canvas")
        return super().render()

    def width(self, value):
        self.attrs["width"] = value
        return self

    def height(self, value):
        self.attrs["height"] = value
        return self

    def get_client_handler_str(self, event_name):
        if event_name in ["mousedown", "mouseup", "mousemove"]:
            return f" on{event_name}='clientEmit(this.id,{{x: event.offsetX, y: event.offsetY}},\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

    def fill_rect(self, x, y, width, height,color):
        self.send(self.id, {"action": "fillRect", "params": {"x": x, "y": y, "width": width, "height": height, "color": color}}, "canvas")
        return self

    def fill_circle(self, x, y, radius,color):
        self.send(self.id, {"action": "fillCircle", "params": {"x": x, "y": y, "radius": radius, "color":color}}, "canvas")
        return self