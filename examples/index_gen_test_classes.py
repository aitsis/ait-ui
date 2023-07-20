from ait_ui.elements import Element
from ait_ui.index_gen import add_header_item, add_script_source, add_script, add_custom_style

# Dropzone
class TestElement(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.id = id
        self.value_name = None
        add_header_item('dropzone', '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.2/min/dropzone.min.css" />')
        add_script_source('dropzone', '<script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.2/min/dropzone.min.js"></script>')
        add_script('dropzone', """
        event_handlers["init-dropzone"] = function(id, value, event_name){
            elements[id] = new Dropzone("#"+id, { url: "/file/post" });
            console.log("init-dropzone");
        }
        event_handlers["dropzone"] = function(id, value, event_name){
        console.log("dropzone",id,value);
            elements[id][value.action](value.value);}
        """)
        add_custom_style('dropzone', """
        .dropzone {
            border: 2px dashed #0087F7;
            border-radius: 5px;
            background: white;
        }
        .dropzone .dz-message {
            font-size: 25px;
            color: #0087F7;
        }
        """)

# OpenSeadragon
class TestElement2(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.id = id
        self.value_name = None
        add_script_source('openseadragon', '<script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>')
        add_script('openseadragon', """
        event_handlers["init-openseadragon"] = function(id, value, event_name){
            elements[id] = OpenSeadragon({
                id: id,
                prefixUrl: "https://openseadragon.github.io/openseadragon/images/",
                tileSources: value
            });
            console.log("init-openseadragon");
        }
        event_handlers["openseadragon"] = function(id, value, event_name){
            console.log("openseadragon",id,value);
            elements[id][value.action](value.value);
        }
        """)
        add_custom_style('openseadragon-style', """
        #openseadragon {
            width: 800px;
            height: 600px;
            border: 1px solid black;
            background-color: black;
        }
        """)

# AlpineJS
class TestElement3(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.id = id
        self.value_name = None
        add_script_source('alpinejs', '<script src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.4.2/cdn.min.js"></script>')
        add_script('alpinejs', """
        event_handlers["init-alpinejs"] = function(id, value, event_name){
            elements[id] = value;
            console.log("init-alpinejs");
        }
        event_handlers["alpinejs"] = function(id, value, event_name){
            console.log("alpinejs",id,value);
            elements[id][value.action](value.value);
        }
        """)
        add_custom_style('alpinejs-style', """
        .bg-blue-500 {
            background-color: #3b82f6;
        }
        """)

# Bootstrap
class TestElement4(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.id = id
        self.value_name = None
        add_header_item('bootstrap', '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css" />')
        add_script_source('bootstrap', '<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.min.js"></script>')
        add_script('bootstrap', """
        event_handlers["init-bootstrap"] = function(id, value, event_name){
            elements[id] = value;
            console.log("init-bootstrap");
        }
        event_handlers["bootstrap"] = function(id, value, event_name){
            console.log("bootstrap",id,value);
            elements[id][value.action](value.value);
        }
        """)

# TailwindCSS
class TestElement5(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.id = id
        self.value_name = None
        add_header_item('tailwindcss', '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" />')