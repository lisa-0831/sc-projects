from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GRect, GLabel
from campy.gui.events.mouse import onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 64       # Height of a brick (in pixels). 40
BRICK_HEIGHT = 24      # Height of a brick (in pixels). 15
BRICK_ROWS = 8        # Number of rows of bricks.
BRICK_COLS = 16        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).

NUM_LIVES = 3		   # Number of attempts


class UfoGraphics:

    def __init__(self, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='UFO Game'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # background
        self.background = GImage('pic/ufo_background.png')
        self.window.add(self.background)

        # ufo
        self.ufo = GImage('pic/ufo.png')
        self.window.add(self.ufo, x=300, y=100)

        # pillars (hole is 200，window_height is 750)
        self.pillar_1_top = GRect(80, 200, x=-100, y=0)
        self.pillar_1_top.color = 'darkgrey'
        self.pillar_1_top.filled = True
        self.pillar_1_top.fill_color = 'darkgrey'
        self.window.add(self.pillar_1_top)

        self.pillar_1_bottom = GRect(80, 350, x=-100, y=400)
        self.pillar_1_bottom.color = 'darkgrey'
        self.pillar_1_bottom.filled = True
        self.pillar_1_bottom.fill_color = 'darkgrey'
        self.window.add(self.pillar_1_bottom)

        self.pillar_2_top = GRect(80, 250, x=-100, y=0)
        self.pillar_2_top.color = 'darkgrey'
        self.pillar_2_top.filled = True
        self.pillar_2_top.fill_color = 'darkgrey'
        self.window.add(self.pillar_2_top)

        self.pillar_2_bottom = GRect(80, 300, x=-100, y=450)
        self.pillar_2_bottom.color = 'darkgrey'
        self.pillar_2_bottom.filled = True
        self.pillar_2_bottom.fill_color = 'darkgrey'
        self.window.add(self.pillar_2_bottom)

        self.pillar_3_top = GRect(80, 300, x=-100, y=0)
        self.pillar_3_top.color = 'darkgrey'
        self.pillar_3_top.filled = True
        self.pillar_3_top.fill_color = 'darkgrey'
        self.window.add(self.pillar_3_top)

        self.pillar_3_bottom = GRect(80, 250, x=-100, y=500)
        self.pillar_3_bottom.color = 'darkgrey'
        self.pillar_3_bottom.filled = True
        self.pillar_3_bottom.fill_color = 'darkgrey'
        self.window.add(self.pillar_3_bottom)

        self.pillar_4_top = GRect(80, 350, x=-100, y=0)
        self.pillar_4_top.color = 'darkgrey'
        self.pillar_4_top.filled = True
        self.pillar_4_top.fill_color = 'darkgrey'
        self.window.add(self.pillar_4_top)

        self.pillar_4_bottom = GRect(80, 200, x=-100, y=550)
        self.pillar_4_bottom.color = 'darkgrey'
        self.pillar_4_bottom.filled = True
        self.pillar_4_bottom.fill_color = 'darkgrey'
        self.window.add(self.pillar_4_bottom)

        # score board
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = 'Times New Roman-40-italic'
        self.window.add(self.score_label, x=5, y=self.score_label.height+5)

        # lives
        self.lives = NUM_LIVES
        for i in range(1, self.lives):
            heart = GImage('pic/lives.png')
            self.heart_width = heart.width
            self.heart_height = heart.height
            self.window.add(heart, x=self.window.width - heart.width * i, y=5)

        self.was_pillar = False
        self.speed = -5
        self.last_num = -1  # know when to increase the speed

        onmousemoved(self.move_ufo)

    def move_ufo(self, mouse):
        self.ufo.y = mouse.y - self.ufo.height / 2

    def hit_pillar(self):
        ufo_top = self.window.get_object_at(self.ufo.x+self.ufo.width+1, self.ufo.y)
        if ufo_top is not None and ufo_top is not self.background:
            ufo_top.x = -100  # remove the pillar
            self.was_pillar = True

        ufo_bottom = self.window.get_object_at(self.ufo.x+self.ufo.width+1, self.ufo.y+self.ufo.height)
        if ufo_bottom is not None and ufo_bottom is not self.background:
            ufo_bottom.x = -100  # remove the pillar
            self.was_pillar = True

    def move_pillar(self):
        if int(self.score) % 50 == 0 and int(self.score) != self.last_num:
            self.last_num = int(self.score)
            if self.speed > -30:
                self.speed -= 5

        if self.pillar_1_top.x > -100:
            self.pillar_1_top.move(self.speed, 0)
        if self.pillar_1_bottom.x > -100:
            self.pillar_1_bottom.move(self.speed, 0)
        if self.pillar_2_top.x > -100:
            self.pillar_2_top.move(self.speed, 0)
        if self.pillar_2_bottom.x > -100:
            self.pillar_2_bottom.move(self.speed, 0)
        if self.pillar_3_top.x > -100:
            self.pillar_3_top.move(self.speed, 0)
        if self.pillar_3_bottom.x > -100:
            self.pillar_3_bottom.move(self.speed, 0)
        if self.pillar_4_top.x > -100:
            self.pillar_4_top.move(self.speed, 0)
        if self.pillar_4_bottom.x > -100:
            self.pillar_4_bottom.move(self.speed, 0)

    def show_pillar(self):
        top_pillar = self.random_pillar()
        if top_pillar.x < 0:
            top_pillar.x = self.window.width + 1

            bottom_pillar = self.another_pillar(top_pillar)
            bottom_pillar.x = self.window.width + 1

    def random_pillar(self):
        n = random.randint(1, 4)
        if n == 1:
            return self.pillar_1_top
        elif n == 2:
            return self.pillar_2_top
        elif n == 3:
            return self.pillar_3_top
        elif n == 4:
            return self.pillar_4_top

    def another_pillar(self, top_pillar):
        if top_pillar is self.pillar_1_top:
            return self.pillar_1_bottom
        elif top_pillar is self.pillar_2_top:
            return self.pillar_2_bottom
        elif top_pillar is self.pillar_3_top:
            return self.pillar_3_bottom
        elif top_pillar is self.pillar_4_top:
            return self.pillar_4_bottom

    def lose(self):
        self.remove_all_obj()
        lose = GLabel('Game Over')
        lose.font = 'Courier-80-bold'
        self.window.add(lose, x=(self.window.width - lose.width) / 2, y=self.window.height / 2)
        self.window.add(self.score_label, x=(self.window.width - self.score_label.width) / 2, y=lose.y + 100)

    def win_line(self):
        self.remove_all_obj()
        win = GLabel('You Win!!')
        win.font = 'Courier-80-bold'
        self.window.add(win, x=(self.window.width - win.width) / 2, y=self.window.height / 2)
        self.window.add(self.score_label, x=(self.window.width - self.score_label.width) / 2, y=win.y + 100)

    def remove_heart(self):
        self.lives -= 1
        heart = self.window.get_object_at(self.window.width - self.heart_width * self.lives + self.heart_width / 2,
                                          8)
        if heart is not self.background:
            self.window.remove(heart)

    def remove_all_obj(self):
        for i in range(0, self.window.width, 10):
            for j in range(0, self.window.height, 10):
                maybe_is_obj = self.window.get_object_at(i, j)
                if maybe_is_obj is not None:
                    self.window.remove(maybe_is_obj)
