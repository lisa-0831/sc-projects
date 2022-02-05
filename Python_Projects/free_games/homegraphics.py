from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GLabel, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from molegraphics import MoleGraphics
from zonegraphics import ZoneGraphics
from ufographics import UfoGraphics
from paintergraphics import PainterGraphics
from bogglegraphics import BoggleGraphics

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 64       # Height of a brick (in pixels). 40
BRICK_HEIGHT = 24      # Height of a brick (in pixels). 15
BRICK_ROWS = 8         # Number of rows of bricks.
BRICK_COLS = 16        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
TIME_WIN_SCORE = 300   # Scores that players need to gain to win the game
MOLE_WIN_SCORE = 100   # Scores that players need to gain to win the game

NUM_LIVES = 3		     # Number of attempts
FRAME_RATE = 1000 / 120  # 120 frames per second / for breakout
DELAY = 550              # for mole


class HomeGraphics:

    def __init__(self, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='SC101 Free Games',
                 time_win_score=TIME_WIN_SCORE, mole_win_score=MOLE_WIN_SCORE):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        self.bar = GRect(self.window_width, 30)
        self.bar.color = 'seashell'
        self.bar.filled = True
        self.bar.fill_color = 'seashell'
        self.window.add(self.bar)

        self.home_label = GLabel('Home|')
        self.home_label.font = 'Courier-30'
        self.window.add(self.home_label, x=5, y=self.home_label.height + 5)

        self.record_label = GLabel('Records|')
        self.record_label.font = 'Courier-30'
        self.window.add(self.record_label, x=5 + self.home_label.width, y=self.home_label.height + 5)

        self.name_label = GLabel('Designed by Lisa ')
        self.name_label.font = 'Courier-20'
        self.name_label.color = 'darkgreen'
        self.window.add(self.name_label, x=self.window.width - self.name_label.width,
                        y=self.home_label.height + 5)

        self.mole_record = 0
        self.breakout_record = 0
        self.zone_record = 0
        self.ufo_record = 0

        self.time_win_score = time_win_score
        self.mole_win_score = mole_win_score

        onmouseclicked(self.handle_clicked)
        onmousemoved(self.handle_moved)

        # Objects for Homepage
        self.background = GImage('pic/home_background.png')
        self.window.add(self.background, x=0, y=self.home_label.y)

        self.title = GLabel('SC101 Free Games')
        self.title.font = 'Courier-80-bold'
        self.title.color = 'white'
        self.window.add(self.title, x=(self.window.width - self.title.width) / 2,
                        y=self.home_label.y + self.title.height + 50)

        self.breakout_sign = GImage('pic/breakout_sign.png')
        self.window.add(self.breakout_sign, x=(self.window_width - self.breakout_sign.width) / 2,
                        y=self.title.y+20)

        self.whack_a_mole_sign = GImage('pic/mole_sign.png')
        self.window.add(self.whack_a_mole_sign, x=self.breakout_sign.x - 350,
                        y=self.title.y+20)

        self.zone_sign = GImage('pic/zone_sign.png')
        self.window.add(self.zone_sign, x=self.breakout_sign.x + 350,
                        y=self.title.y+20)

        self.painter_sign = GImage('pic/painter_sign.png')
        self.window.add(self.painter_sign, x=self.breakout_sign.x - 350,
                        y=self.breakout_sign.height + self.breakout_sign.y + 20)

        self.ufo_sign = GImage('pic/ufo_sign.png')
        self.window.add(self.ufo_sign, x=(self.window_width - self.breakout_sign.width) / 2,
                        y=self.breakout_sign.height + self.breakout_sign.y + 20)

        self.boggle_sign = GImage('pic/boggle_sign.png')
        self.window.add(self.boggle_sign, x=self.breakout_sign.x + 350,
                        y=self.breakout_sign.height + self.breakout_sign.y + 20)

        self.mole_explain = GImage('pic/mole_explain.png')
        self.window.add(self.mole_explain, x=self.window.width + 1, y=self.window.height + 1)

        self.breakout_explain = GImage('pic/breakout_explain.png')
        self.window.add(self.breakout_explain, x=self.window.width + 1, y=self.window.height + 1)

        self.zone_explain = GImage('pic/zone_explain.png')
        self.window.add(self.zone_explain, x=self.window.width + 1, y=self.window.height + 1)

        self.painter_explain = GImage('pic/painter_explain.png')
        self.window.add(self.painter_explain, x=self.window.width + 1, y=self.window.height + 1)

        self.ufo_explain = GImage('pic/ufo_explain.png')
        self.window.add(self.ufo_explain, x=self.window.width + 1, y=self.window.height + 1)

        self.boggle_explain = GImage('pic/boggle_explain.png')
        self.window.add(self.boggle_explain, x=self.window.width + 1, y=self.window.height + 1)

        # Objects for Records
        self.record_title = GLabel('The Highest Score')
        self.record_title.font = 'Courier-80-bold'

        self.mole_r_label = GLabel('Whack a Mole: ' + str(self.mole_record))
        self.mole_r_label.font = 'Courier-60'

        self.breakout_r_label = GLabel('Breakout: ' + str(self.breakout_record))
        self.breakout_r_label.font = 'Courier-60'

        self.zone_r_label = GLabel('Zone: ' + str(self.zone_record))
        self.zone_r_label.font = 'Courier-60'

        self.ufo_r_label = GLabel('UFO: ' + str(self.ufo_record))
        self.ufo_r_label.font = 'Courier-60'

    # Functions for all pages
    def handle_clicked(self, event):
        obj_clicked = self.window.get_object_at(event.x, event.y)

        # Show other pages
        if obj_clicked is self.breakout_sign:
            self.play_breakout()
        elif obj_clicked is self.whack_a_mole_sign:
            self.play_whack_a_mole()
        elif obj_clicked is self.zone_sign:
            self.play_zone()
        elif obj_clicked is self.ufo_sign:
            self.play_ufo()
        elif obj_clicked is self.painter_sign:
            self.play_painter()
        elif obj_clicked is self.boggle_sign:
            self.play_boggle()
        elif obj_clicked is self.home_label:
            self.show_homepage()
        elif obj_clicked is self.record_label:
            self.show_records()

    def handle_moved(self, event):
        obj_moved = self.window.get_object_at(event.x, event.y)

        # Show the explanation of the game
        if obj_moved is self.whack_a_mole_sign:
            self.mole_explain.x = event.x + 8
            self.mole_explain.y = event.y - self.mole_explain.height / 4
        else:
            self.mole_explain.x = self.window.width + 1
            self.mole_explain.y = self.window.height + 1

        if obj_moved is self.breakout_sign:
            self.breakout_explain.x = event.x + 8
            self.breakout_explain.y = event.y - self.breakout_explain.height / 4
        else:
            self.breakout_explain.x = self.window.width + 1
            self.breakout_explain.y = self.window.height + 1

        if obj_moved is self.zone_sign:
            self.zone_explain.x = event.x - 8 - self.zone_explain.width
            self.zone_explain.y = event.y - self.zone_explain.height / 4
        else:
            self.zone_explain.x = self.window.width + 1
            self.zone_explain.y = self.window.height + 1

        if obj_moved is self.painter_sign:
            self.painter_explain.x = event.x + 5
            self.painter_explain.y = event.y + 5
        else:
            self.painter_explain.x = self.window.width + 1
            self.painter_explain.y = self.window.height + 1

        if obj_moved is self.ufo_sign:
            self.ufo_explain.x = event.x + 5
            self.ufo_explain.y = event.y - 5 - self.ufo_explain.height
        else:
            self.ufo_explain.x = self.window.width + 1
            self.ufo_explain.y = self.window.height + 1

        if obj_moved is self.boggle_sign:
            self.boggle_explain.x = event.x - 8 - self.boggle_explain.width
            self.boggle_explain.y = event.y - 5 - self.boggle_explain.height
        else:
            self.boggle_explain.x = self.window.width + 1
            self.boggle_explain.y = self.window.height + 1

    # Functions for homepage and record
    def show_homepage(self):
        # Remove
        self.window.remove(self.record_title)
        self.window.remove(self.mole_r_label)
        self.window.remove(self.breakout_r_label)
        self.window.remove(self.zone_r_label)
        self.window.remove(self.ufo_r_label)

        # Add
        self.window.add(self.background, x=0, y=self.home_label.y)
        self.window.add(self.title, x=(self.window.width - self.title.width) / 2,
                        y=self.home_label.y + self.title.height + 50)
        self.window.add(self.breakout_sign, x=(self.window_width - self.breakout_sign.width) / 2,
                        y=self.title.y + 20)
        self.window.add(self.whack_a_mole_sign, x=self.breakout_sign.x - 350,
                        y=self.title.y + 20)
        self.window.add(self.zone_sign, x=self.breakout_sign.x + 350,
                        y=self.title.y + 20)
        self.window.add(self.painter_sign, x=self.breakout_sign.x - 350,
                        y=self.breakout_sign.height + self.breakout_sign.y + 20)
        self.window.add(self.ufo_sign, x=(self.window_width - self.breakout_sign.width) / 2,
                        y=self.breakout_sign.height + self.breakout_sign.y + 20)
        self.window.add(self.boggle_sign, x=self.breakout_sign.x + 350,
                        y=self.breakout_sign.height + self.breakout_sign.y + 20)

        self.window.add(self.mole_explain, x=self.window.width + 1, y=self.window.height + 1)
        self.window.add(self.breakout_explain, x=self.window.width + 1, y=self.window.height + 1)
        self.window.add(self.zone_explain, x=self.window.width + 1, y=self.window.height + 1)
        self.window.add(self.painter_explain, x=self.window.width + 1, y=self.window.height + 1)
        self.window.add(self.ufo_explain, x=self.window.width + 1, y=self.window.height + 1)
        self.window.add(self.boggle_explain, x=self.window.width + 1, y=self.window.height + 1)

    def show_records(self):
        # Remove
        self.window.remove(self.background)
        self.window.remove(self.title)
        self.window.remove(self.breakout_sign)
        self.window.remove(self.whack_a_mole_sign)
        self.window.remove(self.zone_sign)
        self.window.remove(self.painter_sign)
        self.window.remove(self.ufo_sign)
        self.window.remove(self.boggle_sign)

        self.window.remove(self.mole_explain)
        self.window.remove(self.breakout_explain)
        self.window.remove(self.zone_explain)
        self.window.remove(self.painter_explain)
        self.window.remove(self.ufo_explain)
        self.window.remove(self.boggle_explain)

        # Add
        self.window.add(self.record_title, x=(self.window.width - self.record_title.width) / 2,
                        y=self.home_label.y + self.record_title.height + 50)

        self.mole_r_label.text = 'Whack a Mole: ' + str(self.mole_record) + ' / ' + str(self.mole_win_score)
        self.window.add(self.mole_r_label, x=(self.window.width - self.record_title.width) / 2,
                        y=self.record_title.y + self.mole_r_label.height + 80)

        self.breakout_r_label.text = 'Breakout: ' + str(self.breakout_record) + ' / 128'
        self.window.add(self.breakout_r_label, x=(self.window.width - self.record_title.width) / 2,
                        y=self.mole_r_label.y + self.breakout_r_label.height + 80)

        self.zone_r_label.text = 'Zone: ' + str(self.zone_record) + ' / ' + str(self.time_win_score)
        self.window.add(self.zone_r_label, x=(self.window.width - self.record_title.width) / 2,
                        y=self.breakout_r_label.y + self.zone_r_label.height + 80)

        self.ufo_r_label.text = 'UFO: ' + str(self.ufo_record) + ' / ' + str(self.time_win_score)
        self.window.add(self.ufo_r_label, x=(self.window.width - self.record_title.width) / 2,
                        y=self.zone_r_label.y + self.ufo_r_label.height + 80)

    # The starter of breakout
    def play_breakout(self):
        graphics = BreakoutGraphics()
        lives = graphics.lives

        # Add animation loop here!
        while True:
            pause(FRAME_RATE)
            graphics.ball_out_of_window()
            if graphics.no_ball():
                lives -= 1
                graphics.remove_heart()
                if lives > 0:
                    graphics.set_ball_position()
                else:
                    graphics.lose()  # show 'Game Over' and remove the ball
                    if graphics.score > self.breakout_record:
                        self.breakout_record = graphics.score
                    break

            graphics.move_ball()
            if graphics.ball.x <= 0 and graphics.get_dx() < 0:
                graphics.set_dx(-graphics.get_dx())  # rebound
            if (graphics.ball.x + graphics.ball.width >= graphics.window.width) and graphics.get_dx() > 0:
                graphics.set_dx(-graphics.get_dx())  # rebound
            if graphics.ball.y <= 0 and graphics.get_dy() < 0:  # out of the window
                graphics.set_dy(-graphics.get_dy())  # rebound

            if graphics.extra_ball.x <= 0 and graphics.get_extra_dx() < 0:
                graphics.set_extra_dx(-graphics.get_extra_dx())  # rebound
            if (graphics.extra_ball.x+graphics.extra_ball.width >= graphics.window.width) and \
                    graphics.get_extra_dx() > 0:
                graphics.set_extra_dx(-graphics.get_extra_dx())  # rebound
            if graphics.extra_ball.y <= 0 and graphics.get_extra_dy() < 0:  # out of the window
                graphics.set_extra_dy(-graphics.get_extra_dy())  # rebound

            graphics.confirm_collision_and_rebound()  # check if the ball should rebound or the bricks should be removed

            if graphics.no_bricks():
                graphics.win_line()  # show 'You Win!!'
                if graphics.score > self.breakout_record:
                    self.breakout_record = graphics.score
                break

            graphics.move_rewards()
            graphics.earn_reward()

    # The starter of whack a mole
    def play_whack_a_mole(self):
        """
        This program plays a game called "whack a mole" in which players clicking the popping moles on screen to gain
        scores.
        """
        graphics = MoleGraphics()

        # Add animation loop here!
        while True:
            pause(DELAY)

            if graphics.lives <= 0:
                graphics.lose()  # show 'Game Over'
                if graphics.score > self.mole_record:
                    self.mole_record = graphics.score
                break

            graphics.mole_hide()
            graphics.mole_show()

            if graphics.score >= self.mole_win_score:
                graphics.win_line()
                if graphics.score > self.mole_record:
                    self.mole_record = graphics.score
                break

    # The starter of zone
    def play_zone(self):
        """
        A ball will be bouncing around the GWindow. Players must defend the zone indicated by black line at the middle
        of the GWindow by clicking on the bouncing ball
        """
        graphics = ZoneGraphics()

        # Add animation loop here!
        lives = NUM_LIVES
        while True:
            pause(FRAME_RATE)
            if graphics.ball_in_zone():
                lives -= 1
                graphics.remove_heart()
                if lives > 0:
                    graphics.reset_ball()
                else:
                    graphics.lose()
                    if graphics.score > self.zone_record:
                        self.zone_record = int(graphics.score)
                    break

            graphics.move_ball()
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.dx = -graphics.dx
            if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.dy = -graphics.dy

            graphics.score += 0.1
            graphics.score_label.text = 'Score: ' + str(int(graphics.score))

            if graphics.score >= self.time_win_score:
                graphics.win_line()
                if graphics.score > self.zone_record:
                    self.zone_record = int(graphics.score)
                break

    # The starter of UFO
    def play_ufo(self):
        graphics = UfoGraphics()
        last_show = -1

        lives = NUM_LIVES
        while True:
            pause(FRAME_RATE)

            graphics.hit_pillar()
            if graphics.was_pillar:
                lives -= 1
                graphics.was_pillar = False
                graphics.remove_heart()
                if lives <= 0:
                    graphics.lose()
                    if graphics.score > self.ufo_record:
                        self.ufo_record = int(graphics.score)
                    break

            if int(graphics.score) % 10 == 0 and int(graphics.score) != last_show:
                graphics.show_pillar()
                last_show = int(graphics.score)

            graphics.move_pillar()

            graphics.score += 0.1
            graphics.score_label.text = 'Score: ' + str(int(graphics.score))

            if graphics.score >= self.time_win_score:
                graphics.win_line()
                if graphics.score > self.ufo_record:
                    self.ufo_record = int(graphics.score)
                break

    # The starter of Boggle
    @staticmethod
    def play_boggle():
        graphics = BoggleGraphics()

    # The starter of painter
    @staticmethod
    def play_painter():
        """
        Use campy mouse event to draw GOval
        """
        graphics = PainterGraphics()
