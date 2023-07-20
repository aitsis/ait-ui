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
from index_gen_test_classes import TestElement, TestElement2, TestElement3, TestElement4, TestElement5

class myApp():
    def __init__(self):
        self.click_count = 0
        self.main = Element(id="main")
        with self.main:
            with Row() as row:
                with Col(id="col1") as col1:
                    TestElement(id='dropzone')
                    TestElement2(id='openseadragon')
                with Col(id="col2") as col2:
                    TestElement3(id='alpinejs')
                    TestElement4(id='bootstrap')
                with Col(id="col3") as col3:
                    Text(value="Hello World")
                    with Element():
                        Button(id="BTN1", value="button1")
                    with Element():
                        Button(id="BTN2", value="button2")
                    Button(id="BTN3", value="button3")

    def render(self):
        return self.main.render()

if __name__ == '__main__':
    app.run2(ui = myApp, debug=True)