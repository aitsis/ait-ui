#index_gen.py
# create index.html from index.html.template
#

header_items = ['<meta charset="UTF-8">',
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                '<title>Document</title>',
                '<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.0/socket.io.js"></script>',
                '<script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>',
                '<link rel="stylesheet" href="style.css">'
            ]


default_header_items = {
    'meta-charset': '<meta charset="UTF-8">',
    'meta-viewport': '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    'title': '<title>Document</title>',
    'socket.io': '<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.0/socket.io.js"></script>',
    'openseadragon': '<script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>',
    'style': '<link rel="stylesheet" href="style.css">'
}

scripts = {
    
}


from .elements import scripts as extras
from .elements import styles as extras_css

def generate_index():
    # HTML BEGIN ------------------------------------------------------------
    index_str = '<!DOCTYPE html><html lang="en"><head>'
    # HEADER ITEMS ----------------------------------------------------------
    for key in default_header_items:
        index_str += default_header_items[key]
    index_str += '</head>'
    # BODY ------------------------------------------------------------------
    index_str += '<body>'
    index_str += "<div id='myapp'></div>"
    # SCRIPTS ----------------------------------------------------------------
    if len(extras.scripts) > 0:
        index_str += '<script>'
        for id in extras.scripts:
            index_str += extras.scripts[id]
        index_str += '</script>'
    # add css on body
    if len(extras_css.styles) > 0:
        index_str += '<style>'
        for id in extras_css.styles:
            index_str += extras_css.styles[id]
        index_str += '</style>'

    index_str += '</body>'
    index_str += '</html>'
    return index_str
