#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app, UI
from ait_ui.elements import Element, Elm, Row, Col
from ait_ui.elements import Text
from ait_ui.elements import Button
from ait_ui.elements import ScriptStyleTest, ScriptStyleTest2, ScriptStyleTest3, ScriptStyleTest4

class myApp():
    def __init__(self):
        self.click_count = 0
        self.main = Element()
        with self.main as main:
            main.cls("container")
            Text("t1", value="Hello World")
            with ScriptStyleTest("dropzone"):
                ScriptStyleTest2("openseadragon")
            
            with ScriptStyleTest3("alpinejs"):
                ScriptStyleTest4("bootstrap")

        self.header_items = self.main.get_all_header_items()
        self.scripts_sources = self.main.get_all_script_sources()
        self.scripts = self.main.get_all_scripts()
        self.styles = self.main.get_all_styles()

if __name__ == '__main__':
    app.run2(ui = myApp, debug=True)