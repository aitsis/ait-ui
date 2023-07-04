import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#-------------------------------------------------------------

from ait_ui import  app

from ait_ui.components.element import Element, Elm
from ait_ui.components.input import Input
from ait_ui.components.button import Button
from ait_ui.components.row import Row
from ait_ui.components.text import Text
from ait_ui.components.image import Image

thisdict = {
  "Imagine": "static/assets/images/AIT-logo.png",
  "Repeater": "static/assets/images/AIT-logo.png"
}

with Element(id="main") as main:
    with Row(id="navbar") as navbar:
        with Row(id="search_area") as search_area:
            Input(id="search_input", placeholder="Search for tools and assets").on("change", lambda id, value: print("search", value))
       
    with Element(id="content") as content:
        Text(value="AI Tools").style("font-size", "40px").style("color", "white")
        with Row(id="tools_container") as tools:
            for key in thisdict:
                with Element(id="tool_image") as tool:
                    Image(value=thisdict[key]).cls("image")
                    with Element(id="middle") as tool:
                        Text(value=key).style("font-size", "20px").style("color", "white").cls("text")
        

if __name__ == '__main__':
    app.run(ui = main, debug=True)