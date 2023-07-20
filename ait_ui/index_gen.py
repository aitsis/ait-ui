#index_gen.py
# create index.html from index.html.template
#

default_header_items = {
    'meta-charset': '<meta charset="UTF-8">',
    'meta-viewport': '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    'title': '<title>Document</title>',
    'socket.io': '<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.0/socket.io.js"></script>',
    # 'openseadragon': '<script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>',
    'style': '<link rel="stylesheet" href="style.css">'
}

header_items = {}

default_script_sources = {"main": "<script src='js/main.js'></script>"}

script_sources = {}

scripts = {}

custom_styles = {}

def add_header_item(key, value):
    header_items[key] = value

def add_script_source(key, value):
    script_sources[key] = value

def add_script(id, value):
    scripts[id] = value

def add_custom_style(key, value):
    custom_styles[key] = value

def get_index():
    # HTML BEGIN ------------------------------------------------------------
    index_str = '<!DOCTYPE html><html lang="en"><head>'
    # HEADER ITEMS ----------------------------------------------------------
    for key in default_header_items:
        index_str += default_header_items[key]
    for key in header_items:
        index_str += header_items[key]
    index_str += '</head>'
    # BODY ------------------------------------------------------------------
    index_str += '<body>'
    index_str += "<div id='myapp'></div>"
    # SCRIPTS ----------------------------------------------------------------
    for key in default_script_sources:
        index_str += default_script_sources[key]
    for key in script_sources:
        index_str += script_sources[key]
    if len(scripts) > 0:
        index_str += '<script>'
        for id in scripts:
            index_str += scripts[id]
        index_str += '</script>'
    # CUSTOM STYLES ----------------------------------------------------------
    if len(custom_styles) > 0:
        index_str += '<style>'
        for key in custom_styles:
            index_str += custom_styles[key]
        index_str += '</style>'
    index_str += '</body>'
    index_str += '</html>'
    return index_str
