from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GLabel
from campy.gui.events.mouse import onmouseclicked
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 64       # Height of a brick (in pixels). 40
BRICK_HEIGHT = 24      # Height of a brick (in pixels). 15
BRICK_ROWS = 8        # Number of rows of bricks.
BRICK_COLS = 16        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).

NUM_LIVES = 3		   # Number of attempts


class MoleGraphics:

    def __init__(self, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Whack a Mole'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # background
        self.background = GImage('pic/mole_background.png')
        self.window.add(self.background)

        # mole
        self.mole_1 = GImage('pic/mole.png')
        self.window.add(self.mole_1, x=96, y=122)

        self.mole_2 = GImage('pic/mole.png')
        self.window.add(self.mole_2, x=self.window.width+1, y=self.window.height+1)

        self.mole_3 = GImage('pic/mole.png')
        self.window.add(self.mole_3, x=96, y=462)

        self.mole_4 = GImage('pic/mole.png')
        self.window.add(self.mole_4, x=self.window.width+1, y=self.window.height+1)

        self.mole_5 = GImage('pic/mole.png')
        self.window.add(self.mole_5, x=self.window.width+1, y=self.window.height+1)

        self.mole_6 = GImage('pic/mole.png')
        self.window.add(self.mole_6, x=914, y=122)

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

        onmouseclicked(self.click_background_or_mole)

    def mole_show(self):
        mole = self.random_mole()
        if mole.x > self.window.width:
            mole.x = self.random_x()
            mole.y = self.random_y()

    def mole_hide(self):
        mole = self.random_mole()
        if random.random() > 0.3 and mole.x < self.window.width:
            mole.x = self.window.width + 1
            mole.y = self.window.height + 1

    def random_mole(self):
        n = random.randint(1, 6)
        if n == 1:
            return self.mole_1
        elif n == 2:
            return self.mole_2
        elif n == 3:
            return self.mole_3
        elif n == 4:
            return self.mole_4
        elif n == 5:
            return self.mole_5
        elif n == 6:
            return self.mole_6

    @staticmethod
    def random_x():
        n = random.randint(1, 4)
        if n == 1:
            return 96
        elif n == 2:
            return 373
        elif n == 3:
            return 640
        elif n == 4:
            return 914

    @staticmethod
    def random_y():
        n = random.randint(1, 3)
        if n == 1:
            return 122
        elif n == 2:
            return 292
        elif n == 3:
            return 462

    def click_background_or_mole(self, mouse):
        maybe_mole = self.window.get_object_at(mouse.x, mouse.y)
        if maybe_mole == self.background:
            self.lives -= 1
            self.remove_heart()
        elif maybe_mole is self.mole_1 or maybe_mole is self.mole_2 or maybe_mole is self.mole_3 or \
                maybe_mole is self.mole_4 or maybe_mole is self.mole_5 or maybe_mole is self.mole_6:
            maybe_mole.x = self.window.width + 1
            maybe_mole.y = self.window.height + 1
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)

    def lose(self):
        self.remove_all_obj()
        lose = GLabel('Game Over')
        lose.font = 'Courier-80-bold'
        self.window.add(lose, x=(self.window.width - lose.width) / 2, y=self.window.height / 2)
        self.window.add(self.score_label, x=(self.window.width-self.score_label.width)/2, y=lose.y + 100)

    def win_line(self):
        self.remove_all_obj()
        win = GLabel('You Win!!')
        win.font = 'Courier-80-bold'
        self.window.add(win, x=(self.window.width - win.width) / 2, y=self.window.height / 2)
        self.window.add(self.score_label, x=(self.window.width - self.score_label.width) / 2, y=win.y + 100)

    def remove_heart(self):
        heart = self.window.get_object_at(self.window.width - self.heart_width * self.lives + self.heart_width / 2, 8)
        if heart is not self.background:
            self.window.remove(heart)

    def remove_all_obj(self):
        for i in range(0, self.window.width, 10):
            for j in range(0, self.window.height, 10):
                maybe_is_obj = self.window.get_object_at(i, j)
                if maybe_is_obj is not None:
                    self.window.remove(maybe_is_obj)
