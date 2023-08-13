#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Radio, Label
from ait_ui.core import Component, Element

class Comp_Radio(Component):
    
    save_path = os.getcwd() + "/assets"
    
    def __init__(self, id=None, value_list=None, autoBind=True, callback=None, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        self.callback = callback
        self.value_list=value_list
        self.add_header_item("radio-css", """
                                  <style>.btn input[type="radio"] {
                                    display: block;
                                    position: absolute;
                                    top: 0;
                                    left: 0;
                                    right: 0;
                                    bottom: 0;
                                    opacity: 0.011;
                                    z-index: 100;
                                    height: 100%;
                                }
                                
                                .btn input[type="radio"]:checked + .container{
                                    background-color: rgba(255,255,255,0.3);
                                }

                                .lbl{
                                    font-size: 0.9em !important;
                                }</style>""")
        
        self.cls("container").style("flex-direction","row").style("height","50px").style("justify-content","space-around")
        with self:
            for value in self.value_list:
                with Element().cls("btn").style("position","relative").style("margin-right","5px").style("padding","0").style("display","grid").style("grid-template-columns","repeat(auto-fit, minmax(40px, 1fr))").style("border","5px solid black").style("max-height","100%"):
                    Radio(name="check-substitution-2").checked(value = value).style("width","100%").on("change", self.on_change)
                    with Element().cls("container").style("height","100%").style("justify-content","center").style("align-items","center"):
                        Label(value=value).cls("lbl")
    
    def on_change(self, id, value):
        if self.callback:
            self.callback(id, value)