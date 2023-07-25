#index_gen.py
# create index.html from index.html.template
#

default_header_items = {
    'meta-charset': '<meta charset="UTF-8">',
    'meta-viewport': '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    'title': '<title>Document</title>',
    'socket.io': '<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.0/socket.io.js"></script>',
    'style': '<link rel="stylesheet" href="style.css">'
}

header_items = {}

default_script_sources = {"main": "<script src='js/main.js'></script>"}

script_sources = {}

scripts = {}

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
    index_str += '</body>'
    index_str += '</html>'
    return index_str