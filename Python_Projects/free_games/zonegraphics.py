from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gimage import GImage
import random

WINDOW_WIDTH = 1099
WINDOW_HEIGHT = 731
ZONE_WIDTH = 300
ZONE_HEIGHT = 300
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_X_SPEED = 1
MIN_Y_SPEED = 2

NUM_LIVES = 3


class ZoneGraphics:
    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT, zone_width=ZONE_WIDTH,
                 zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        self.window = GWindow(width=window_width, height=window_height, title='Zone Game')

        self.zone = GRect(zone_width, zone_height, x=(window_width-zone_width)/2, y=(window_height-zone_height)/2)
        self.zone.color = 'blue'
        self.window.add(self.zone)

        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True

        self.dx = 0
        self.dy = 0
        self.reset_ball()  # put ball in the window

        # score board
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = 'Times New Roman-40-italic'
        self.window.add(self.score_label, x=5, y=self.score_label.height + 5)

        # lives
        self.lives = NUM_LIVES
        for i in range(1, self.lives):
            heart = GImage('pic/lives.png')
            self.heart_width = heart.width
            self.heart_height = heart.height
            self.window.add(heart, x=self.window.width - heart.width * i, y=self.window.height - heart.height)

        onmouseclicked(self.handle_click)

    def reset_ball(self):
        self.set_ball_position()  # decide the coordinate of the ball
        while self.ball_in_zone():  # whether the ball is in the zone
            self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    def set_ball_position(self):
        self.ball.x = random.randint(0, self.window.width-self.ball.width)
        self.ball.y = random.randint(0, self.window.height-self.ball.height)

    def ball_in_zone(self):
        is_ball_x_in_zone = self.zone.x <= self.ball.x <= self.zone.x + self.zone.width - self.ball.width
        is_ball_y_in_zone = self.zone.y <= self.ball.y <= self.zone.y + self.zone.height
        return is_ball_x_in_zone and is_ball_y_in_zone

    def set_ball_velocity(self):
        self.dx = random.randint(MIN_X_SPEED, MAX_SPEED)
        self.dy = random.randint(MIN_Y_SPEED, MAX_SPEED)
        if random.random() < 0.5:
            self.dx = -self.dx
        if random.random() < 0.5:
            self.dy = -self.dy

    def move_ball(self):
        self.ball.move(self.dx, self.dy)

    def handle_click(self, event):
        obj = self.window.get_object_at(event.x, event.y)
        if obj == self.ball:
            self.reset_ball()

    def lose(self):
        self.remove_all_obj()
        lose = GLabel('Game Over')
        lose.font = 'Courier-80-bold'
        self.window.add(lose, x=(self.window.width-lose.width)/2, y=self.window.height/2)
        self.window.add(self.score_label, x=(self.window.width - self.score_label.width) / 2, y=lose.y + 100)

    def win_line(self):
        self.remove_all_obj()
        win = GLabel('You Win!!')
        win.font = 'Courier-80-bold'
        self.window.add(win, x=(self.window.width-win.width)/2, y=self.window.height/2)
        self.window.add(self.score_label, x=(self.window.width - self.score_label.width) / 2, y=win.y + 100)

    def remove_heart(self):
        self.lives -= 1
        heart = self.window.get_object_at(self.window.width - self.heart_width*self.lives + self.heart_width/2,
                                          self.window.height - self.heart_height/2)
        self.window.remove(heart)

    def remove_all_obj(self):
        for i in range(0, self.window.width, 10):
            for j in range(0, self.window.height, 10):
                maybe_is_obj = self.window.get_object_at(i, j)
                if maybe_is_obj is not None:
                    self.window.remove(maybe_is_obj)
