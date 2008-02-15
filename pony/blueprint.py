from cStringIO import StringIO

from pony.templating import template, cycle
from pony.web import http

@http('/blueprint/$column_count/$column_width/$gutter_width/grid.css', type='text/css')
def grid(column_count=24, column_width=30, gutter_width=10):
    column_count=int(column_count)
    column_width=int(column_width)
    gutter_width=int(gutter_width)
    page_width = column_count*(column_width+gutter_width) - gutter_width
    return template()

@http('/blueprint/$column_count/$column_width/$gutter_width/grid.png', type='image/png')
def grid_background(column_count=24, column_width=30, gutter_width=10):
    column_count=int(column_count)
    column_width=int(column_width)
    gutter_width=int(gutter_width)
    try: import Image, ImageDraw
    except ImportError: raise http.NotFound
    im = Image.new('RGB', (column_width+gutter_width, 18), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.rectangle((0, 0, column_width, 17), fill=(232, 239, 251))
    draw.line((0, 17, column_width+gutter_width, 17), fill=(233, 233, 233))
    io = StringIO()
    im.save(io, 'PNG')
    return io.getvalue()