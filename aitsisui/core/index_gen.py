#index_gen.py
# create index.html from index.html.template
#
import re

default_header_items = {
    'meta-charset': '<meta charset="UTF-8">',
    'meta-viewport': '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    #'title': '<title>Document</title>',
    'socket.io': '<script src="js/socket.io.min.js"></script>',
    # 'font-awesome-css': '<link rel="stylesheet" href="font-awesome_6.4.2.all.min.css" referrerpolicy="no-referrer">',
    # 'font-awesome-js': '<script src="/js/font-awesome_6.4.2.all.min.js" referrerpolicy="no-referrer"></script>',
    'style': '<link rel="stylesheet" href="style.css">',
    'favicon': '<link rel="icon" href="https://ai.ait.com.tr/wp-content/uploads/cropped-favicon_aiait-32x32.png" sizes="32x32" />'
}

global header_items
global scripts
global script_sources
global styles

header_items = {}

default_script_sources = {"main": "<script src='js/main.js'></script>"}

script_sources = {}

scripts = {}

styles = {}

def add_header_item(id, item):
    if id in header_items:
        return
    header_items[id] = item

def add_script_source(id, script):
    if id in scripts:
        return
    script_sources[id] = script

def add_script(id, script):
    if id in scripts:
        return
    scripts[id] = script

def add_css(id, style):
    if id in styles:
        return
    styles[id] = style

def minify_js(js_code):
    return re.sub(r'\s+', ' ', re.sub(r'//.*?\n|/\*.*?\*/', '', js_code)).strip()

def minify_css(css_code):
    return re.sub(r'\s+', ' ', re.sub(r'/\*.*?\*/', '', css_code)).strip()

def minify_html(html_code):
    return re.sub(r'>\s+<', '><', re.sub(r'<!--.*?-->', '', html_code)).strip()

def get_index():
    global header_items
    global scripts
    global script_sources
    global styles
    # HTML BEGIN ------------------------------------------------------------
    index_str = '<!DOCTYPE html><html lang="en"><head>'
    # HEADER ITEMS ----------------------------------------------------------
    for key in default_header_items:
        index_str += default_header_items[key]
    for key in header_items:
        index_str += header_items[key]
    # STYLES ----------------------------------------------------------------
    for key in styles:
        index_str += '<style>'
        index_str += minify_css(styles[key])
        index_str += '</style>'
    index_str += '</head>'
    # BODY ------------------------------------------------------------------
    index_str += '<body>'
    index_str += "<div id='myapp'></div>"
    # SCRIPTS ---------------------------------------------------------------
    for key in default_script_sources:
        index_str += default_script_sources[key]
    for key in script_sources:
        index_str += script_sources[key]
    if len(scripts) > 0:
        for id in scripts:
            index_str += '<script>'
            index_str += minify_js(scripts[id])
            index_str += '</script>'
    index_str += '</body>'
    index_str += '</html>'
    index_str = minify_html(index_str)
    return index_str

def get_minified_index():
    return minify_html(get_index())