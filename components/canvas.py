from components.element import Element
import connection

import components.scripts as scripts


scripts.add_script("canvas", """
    event_handlers["init-canvas"] = function(id, value, event_name){
            console.log("init-canvas");
            canvas = document.getElementById(id);
            
            elements[id] = {canvas: canvas, ctx: canvas.getContext('2d')};            
        }
    event_handlers["canvas"] = function(id, value, event_name){
        console.log("canvas", id, value, event_name);
        if (value.action == "fillRect"){
            console.log("fillRect", value.params,elements[id].ctx);
            elements[id].ctx.fillRect(value.params.x, value.params.y, value.params.width, value.params.height);
        }
    }
    """)
class Canvas(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "canvas"
        self.id = id
        self.value_name = None
        if id is not None:            
            connection.queue_for_send(self.id, self.value, "init-canvas")
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value                        

    def width(self, value):
        self.attrs["width"] = value
        return self
    def height(self, value):
        self.attrs["height"] = value
        return self

    def get_client_handler_str(self, event_name):
        if event_name in ["mousedown", "mouseup", "mousemove"]:
            return f" on{event_name}='clientEmit(this.id,{{x: event.clientX, y: event.clientY}},\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

    def fill_rect(self, x, y, width, height):
        connection.send(self.id, {"action": "fillRect", "params": {"x": x, "y": y, "width": width, "height": height}}, "canvas")