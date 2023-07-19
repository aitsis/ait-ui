from .element import Element

# Dropzone
class ScriptStyleTest(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.append_script_source('dropzone','<script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/dropzone.min.js"></script>')
        self.append_header_item('dropzone-css','<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/dropzone.min.css" />')
        self.append_script('dropzone', """
        event_handlers["init-dropzone"] = function(id, value, event_name){
            elements[id] = new Dropzone("#"+id, { url: "/file/post" });
            console.log("init-dropzone");
        }
        event_handlers["dropzone"] = function(id, value, event_name){
        console.log("dropzone",id,value);
            elements[id][value.action](value.value);}
        """)
        self.append_custom_style('dropzone-style', """
        .dropzone {
            border: 2px dashed #0087F7;
            border-radius: 5px;
            background: white;
        }
        .dropzone.dz-started .dz-message {
            display: none;
        }
        .dropzone.dz-drag-hover {
            border-color: #2AD705;
        }
        """)
    
# OpenSeadragon
class ScriptStyleTest2(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.append_script_source('openseadragon','<script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>')
        self.append_script('openseadragon', """
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
        self.append_custom_style('openseadragon-style', """
        #openseadragon {
            width: 800px;
            height: 600px;
            border: 1px solid black;
            background-color: black;
        }
        """)

# AlpineJS
class ScriptStyleTest3(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.append_script_source('alpine','<script src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/2.8.2/alpine.js"></script>')
        self.append_script('alpinejs', """
        event_handlers["init-alpinejs"] = function(id, value, event_name){
            elements[id] = value;
            console.log("init-alpinejs");
        }
        event_handlers["alpinejs"] = function(id, value, event_name){
            console.log("alpinejs",id,value);
            elements[id][value.action](value.value);
        }
        """)
        self.append_custom_style('alpinejs-style', """
        .bg-blue-500 {
            background-color: #3b82f6;
        }
        """)

# Bootstrap
class ScriptStyleTest4(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.append_header_item('bootstrap-css','<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.1.3/css/bootstrap.min.css" />')
        self.append_script_source('bootstrap','<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>')
        self.append_script('bootstrap', """
        event_handlers["init-bootstrap"] = function(id, value, event_name){
            elements[id] = value;
            console.log("init-bootstrap");
        }
        event_handlers["bootstrap"] = function(id, value, event_name){
            console.log("bootstrap",id,value);
            elements[id][value.action](value.value);
        }
        """)
        self.append_custom_style('bootstrap-style', """
        .bg-blue-500 {
            background-color: #3b82f6;
        }
        """)