#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Element , Button , Elm
from ait_ui.component import Component

class Comp_Accordion(Component):
    def __init__(self, id=None, elements=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        
        self.isAccordionOpen = True
        self.add_header_item("accordion-css", """<style>
                                    .accordion-element-wrapper{
                                        width: 100%;
                                        height: 100px;
                                        box-sizing: border-box;
                                        padding: 5px;
                                        border: 1px solid gray;
                                        border-radius: 3px;
                                        display: flex;
                                        flex-direction: row;
                                        justify-content: space-between;
                                    }

                                    .item-wrapper{
                                        width: 100%;
                                        height: 100%;
                                        box-sizing: border-box;
                                        padding: 5px;
                                        display: flex;
                                        flex-direction: column;
                                        justify-content: center;
                                    }


                                    .accordion{
                                        width: 100%;
                                        height: 100%;
                                    }

                                    .accordion button{
                                        width: 100%;
                                        height: 9%;
                                        color: white;
                                        border: 1px solid gray;
                                        border-radius: 3px;
                                        box-sizing: border-box;
                                        padding: 10px;
                                        display: flex;
                                        align-items: center;
                                        cursor: pointer;
                                        transition: all 300ms ease-out;
                                    }

                                    .accordion-button:active{
                                        scale: 0.9;
                                    }

                                    .accordion-wrapper{
                                        width: 100%;
                                        height: 0px;
                                        color: white;
                                        box-sizing: border-box;
                                        display: flex;
                                        flex-direction: column;
                                        overflow-y: auto;
                                        gap: 10px;
                                        transition: all 300ms ease-out;
                                    }

                                    .accordion{
                                        width: 100%;
                                        height: 9%;
                                        border-radius: 3px;
                                        box-sizing: border-box;
                                        padding: 10px;
                                        display: flex;
                                        flex-direction: column;
                                        justify-content: center;
                                        align-items: center;
                                        transition: all 300ms ease-out;
                                    }</style>""")
        
        self.cls("accordion").style("height","5%").style("background-color","#434952").style("border","1px solid gray").style("border-radius","3px").style("padding","10px").style("box-sizing","border-box")
        
        with self:
            with Button(value="Advanced Options > ").style("border", "none").style("height", "0").style("justify-content", "flex-start").on("click", self.change_accordion):
                pass
            with Element().cls("accordion-wrapper") as accordion_wrapper:
                self.accordion_wrapper = accordion_wrapper
                for element in elements:
                    with Element().cls("accordion-element-wrapper"):
                        with Element().cls("item-wrapper"):
                            element.bind()

    def change_accordion(self, id, value):
        if self.isAccordionOpen:
            self.accordion_wrapper.set_style("height", "100%")
            self.set_style("height", "100%")
            self.set_style("gap", "10px")
        else:
            self.accordion_wrapper.set_style("height", "0px")
            self.set_style("gap", "0px")
            self.set_style("height", "5%")
        self.isAccordionOpen = not self.isAccordionOpen