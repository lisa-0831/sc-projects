from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval
from campy.gui.events.mouse import onmousemoved, onmousedragged, onmouseclicked

WINDOW_WIDTH = 1099
WINDOW_HEIGHT = 731

# This constant controls the size of the GOval
SIZE = 30


class PainterGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT, size=SIZE):

        self.window = GWindow(width=window_width, height=window_height, title='Painter')
        self.size = size

        self.oval = GOval(self.size, self.size)
        self.oval.color = 'tomato'
        self.oval.filled = True
        self.oval.fill_color = 'tomato'
        self.window.add(self.oval, x=self.window.width+self.size+1, y=self.window.height+self.size+1)

        onmousemoved(self.move_oval)
        onmouseclicked(self.draw)
        onmousedragged(self.draw)

    def move_oval(self, mouse):
        self.oval.x = mouse.x-self.size/2
        self.oval.y = mouse.y-self.size/2

    def draw(self, mouse):
        stroke = GOval(self.size, self.size)
        stroke.color = 'tomato'
        stroke.filled = True
        stroke.fill_color = 'tomato'
        self.window.add(stroke, x=mouse.x - SIZE / 2, y=mouse.y - self.size / 2)
