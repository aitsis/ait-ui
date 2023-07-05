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



body = """
    <div id="myapp"></div>"""

from .components import scripts as extras

def generate_index():
    index_str = '<!DOCTYPE html><html lang="en">'
    index_str += '<head>'
    # add header items
    for item in header_items:
        index_str += item
    for item in extras.header_items:
        index_str += item
    index_str += '</head>'
    index_str += '<body>'
    index_str += body
    # add scripts on body
    if len(extras.scripts) > 0:
        index_str += '<script>'
        for id in extras.scripts:
            index_str += extras.scripts[id]
        index_str += '</script>'
    index_str += '</body>'
    index_str += '</html>'
    return index_str
