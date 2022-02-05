"""
Games Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 64       # Height of a brick (in pixels). 40
BRICK_HEIGHT = 24      # Height of a brick (in pixels). 15
BRICK_ROWS = 8        # Number of rows of bricks.
BRICK_COLS = 16        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 100     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
INITIAL_X_SPEED = 1
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3		   # Number of attempts


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.long_paddle_w = paddle_width * 2
        self.long_paddle = GRect(self.long_paddle_w, paddle_height)
        self.long_paddle.color = 'white'
        self.long_paddle.filled = True
        self.long_paddle.fill_color = 'white'
        self.window.add(self.long_paddle, x=(window_width - self.long_paddle_w) / 2,
                        y=window_height - paddle_offset - paddle_height)
        self.show_long_paddle = False

        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)

        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = INITIAL_X_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

        self.__extra_dy = INITIAL_Y_SPEED
        self.__extra_dx = INITIAL_X_SPEED + 1
        if random.random() > 0.5:
            self.__extra_dx = -self.__extra_dx

        # Initialize our mouse listeners
        onmousemoved(self.handle_move)
        onmouseclicked(self.handle_click)
        self.game_start = False  # the ball should start to move or not

        # Score board
        self.score = 0
        self.score_board = GLabel('Score: ' + str(self.score))
        self.score_board.font = 'Times New Roman-40-italic'
        self.window.add(self.score_board, x=5, y=self.window.height)

        # lives
        self.lives = NUM_LIVES
        for i in range(1, self.lives):
            heart = GImage('pic/lives.png')
            self.heart_width = heart.width
            self.heart_height = heart.height
            self.window.add(heart, x=self.window.width - heart.width*i, y=self.window.height - heart.height)

        # rewards and punishments
        self.lengthen = GImage('pic/lengthen.png')
        self.shorten = GImage('pic/shorten.png')
        self.speed_up = GImage('pic/speed_up.png')
        self.speed_down = GImage('pic/speed_down.png')
        self.extra_ball = GOval(ball_radius * 2, ball_radius * 2)
        self.extra_ball.filled = True

        # draw bricks
        brick_y = brick_offset  # the y coordinate of the brick
        color_change = brick_rows / 5  # decide when should the color change

        for i in range(brick_rows):
            brick_x = 0  # the x coordinate of the brick
            # decide the color of bricks
            if i // color_change == 0:
                color = 'red'
            elif i // color_change == 1:
                color = 'orange'
            elif i // color_change == 2:
                color = 'yellow'
            elif i // color_change == 3:
                color = 'green'
            else:
                color = 'blue'

            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=brick_x, y=brick_y)
                brick.color = color
                brick.filled = True
                brick.fill_color = color
                self.window.add(brick)
                brick_x += (brick_width + brick_spacing)  # update the x coordinate of the brick
            brick_y += (brick_height + brick_spacing)  # update the y coordinate of the brick
        self.bricks_num = brick_rows * brick_cols  # calculate how many bricks

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width / 2 - ball_radius, y=window_height / 2 - ball_radius)

    def handle_move(self, event):
        if self.paddle.width/2 <= event.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = event.x - self.paddle.width/2
        elif event.x < self.paddle.width/2:  # over the left side of the screen
            self.paddle.x = 0
        elif event.x > self.window.width-self.paddle.width/2:  # over the right side of the screen
            self.paddle.x = self.window.width-self.paddle.width

        # long paddle
        if self.long_paddle.width/2 <= event.x <= self.window.width-self.long_paddle.width/2:
            self.long_paddle.x = event.x - self.long_paddle.width/2
        elif event.x < self.long_paddle.width/2:  # over the left side of the screen
            self.long_paddle.x = 0
        elif event.x > self.window.width-self.long_paddle.width/2:  # over the right side of the screen
            self.long_paddle.x = self.window.width-self.long_paddle.width

    def handle_click(self, event):
        if 0 <= event.x <= self.window.width and 0 <= event.y <= self.window.height:
            self.game_start = True  # the user clicked the mouse to start the game

    @staticmethod
    def confirm_plus_or_minus(number):
        if number > 0:
            return 1
        else:
            return -1

    def move_ball(self):
        if self.game_start:
            if self.score == 3:  # change dx to 2
                self.__dx = (2 * self.confirm_plus_or_minus(self.__dx))
                self.__extra_dx = (2 * self.confirm_plus_or_minus(self.__extra_dx))

            elif self.score == 6:  # change dy to 8
                self.__dy = (8 * self.confirm_plus_or_minus(self.__dy))
                self.__extra_dy = (8 * self.confirm_plus_or_minus(self.__extra_dy))

            elif self.score == 9:  # change dx to 3
                self.__dx = (3 * self.confirm_plus_or_minus(self.__dx))
                self.__extra_dx = (3 * self.confirm_plus_or_minus(self.__extra_dx))

            elif self.score == 12:  # change dy to 9
                self.__dy = (9 * self.confirm_plus_or_minus(self.__dy))
                self.__extra_dy = (9 * self.confirm_plus_or_minus(self.__extra_dy))

            elif self.score == 15:  # change dx to 4
                self.__dx = (4 * self.confirm_plus_or_minus(self.__dx))
                self.__extra_dx = (4 * self.confirm_plus_or_minus(self.__extra_dx))

            elif self.score == 18:  # change dy to 10
                self.__dy = (10 * self.confirm_plus_or_minus(self.__dy))
                self.__extra_dy = (10 * self.confirm_plus_or_minus(self.__extra_dy))

            elif self.score == 21:  # change dx to 5
                self.__dx = (5 * self.confirm_plus_or_minus(self.__dx))
                self.__extra_dx = (5 * self.confirm_plus_or_minus(self.__extra_dx))

            elif self.score == 24:  # change dy to 11
                self.__dy = (11 * self.confirm_plus_or_minus(self.__dy))
                self.__extra_dy = (11 * self.confirm_plus_or_minus(self.__extra_dy))

            elif self.score == 27:  # change dy to 12
                self.__dy = (12 * self.confirm_plus_or_minus(self.__dy))
                self.__extra_dy = (12 * self.confirm_plus_or_minus(self.__extra_dy))

            if self.window.get_object_at(self.ball.x+self.ball.width/2, self.ball.y+self.ball.height/2) is not None:
                self.ball.move(self.__dx, self.__dy)
            if self.window.get_object_at(self.extra_ball.x+self.extra_ball.width/2,
                                         self.extra_ball.y+self.extra_ball.height/2) is not None:
                self.extra_ball.move(self.__extra_dx, self.__extra_dy)

    def get_dx(self):
        return self.__dx

    def set_dx(self, new_speed):
        self.__dx = new_speed

    def get_dy(self):
        return self.__dy

    def set_dy(self, new_speed):
        self.__dy = new_speed

    def get_extra_dx(self):
        return self.__extra_dx

    def set_extra_dx(self, new_speed):
        self.__extra_dx = new_speed

    def get_extra_dy(self):
        return self.__extra_dy

    def set_extra_dy(self, new_speed):
        self.__extra_dy = new_speed

    def confirm_collision_and_rebound(self):

        # Original ball
        ball_x, ball_y = int(self.ball.x), int(self.ball.y)
        hit_brick = False

        for x in range(ball_x, ball_x + 2 * BALL_RADIUS + 1, 2 * BALL_RADIUS):
            for y in range(ball_y, ball_y + 2 * BALL_RADIUS + 1, 2 * BALL_RADIUS):
                hit_obj = self.window.get_object_at(x, y)

                if hit_obj is not None and hit_obj.y < self.paddle.y and self.is_not_reward(hit_obj):
                    self.window.remove(hit_obj)  # remove the brick
                    self.bricks_num -= 1  # update the number of bricks that are still on the window

                    # update the score
                    self.score += 1
                    self.score_board.text = 'Score: ' + str(self.score)

                    self.random_reward(hit_obj.x, hit_obj.y)

                # Hit the paddle and rebound
                if (y == ball_y + 2 * BALL_RADIUS) and hit_obj is self.paddle or \
                        (hit_obj is self.long_paddle and self.show_long_paddle):  # hit the paddle
                    if self.__dy > 0:
                        self.__dy = -self.__dy
                if hit_obj is not None and hit_obj.y < self.paddle.y and self.is_not_reward(hit_obj):  # hit bricks
                    hit_brick = True

        # Hit brick and rebound
        if hit_brick:
            self.__dy = -self.__dy  # rebound (change the direction)

        # Extra ball
        extra_ball_x, extra_ball_y = int(self.extra_ball.x), int(self.extra_ball.y)
        extra_hit_brick = False

        for x in range(extra_ball_x, extra_ball_x + 2 * BALL_RADIUS + 1, 2 * BALL_RADIUS):
            for y in range(extra_ball_y, extra_ball_y + 2 * BALL_RADIUS + 1, 2 * BALL_RADIUS):
                hit_obj = self.window.get_object_at(x, y)

                if hit_obj is not None and hit_obj.y < self.paddle.y and self.is_not_reward(hit_obj):
                    self.window.remove(hit_obj)  # remove the brick
                    self.bricks_num -= 1  # update the number of bricks that are still on the window

                    # update the score
                    self.score += 1
                    self.score_board.text = 'Score: ' + str(self.score)

                    self.random_reward(hit_obj.x, hit_obj.y)

                # Hit the paddle and rebound
                if (y == extra_ball_y + 2 * BALL_RADIUS) and hit_obj is self.paddle or \
                        (hit_obj is self.long_paddle and self.show_long_paddle):  # hit the paddle
                    if self.__extra_dy > 0:
                        self.__extra_dy = -self.__extra_dy
                if hit_obj is not None and hit_obj.y < self.paddle.y and self.is_not_reward(hit_obj):  # hit bricks
                    extra_hit_brick = True

        # Hit brick and rebound
        if extra_hit_brick:
            self.__extra_dy = -self.__extra_dy  # rebound (change the direction)

    def ball_out_of_window(self):
        if self.window.get_object_at(self.ball.x+self.ball.width/2, self.ball.y+self.ball.height/2) is not None:
            if self.ball.y + self.ball.height >= self.window.height:
                self.window.remove(self.ball)
        if self.window.get_object_at(self.extra_ball.x+self.extra_ball.width/2,
                                     self.extra_ball.y+self.extra_ball.height/2) is not None:
            if self.extra_ball.y + self.extra_ball.height >= self.window.height:
                self.window.remove(self.extra_ball)

    def no_ball(self):
        return (self.window.get_object_at(self.ball.x+self.ball.width/2, self.ball.y+self.ball.height/2) is None) and \
               (self.window.get_object_at(self.extra_ball.x+self.extra_ball.width/2,
                                          self.extra_ball.y+self.extra_ball.height/2) is None)

    def is_not_reward(self, obj):
        """
        for fear that the ball will rebound
        """
        if obj is not self.lengthen and obj is not self.shorten and obj is not self.speed_up and \
                obj is not self.speed_down and obj is not self.ball and obj is not self.extra_ball and \
                obj is not self.paddle and obj is not self.long_paddle:
            return True

    def random_reward(self, item_x, item_y):
        num = random.randint(1, 12)
        if num == 1 and self.window.get_object_at(self.lengthen.x, self.lengthen.y) is None and \
                self.show_long_paddle is False:
            self.window.add(self.lengthen, x=item_x, y=item_y)
        elif num == 2 and self.window.get_object_at(self.shorten.x, self.shorten.y) is None and self.show_long_paddle:
            self.window.add(self.shorten, x=item_x, y=item_y)
        elif num == 3 and self.window.get_object_at(self.speed_up.x, self.speed_up.y) is None:
            self.window.add(self.speed_up, x=item_x, y=item_y)
        elif num == 4 and self.window.get_object_at(self.speed_down.x, self.speed_down.y) is None:
            self.window.add(self.speed_down, x=item_x, y=item_y)
        elif num == 5 and self.window.get_object_at(self.ball.x+self.ball.width/2, self.ball.y+self.ball.height) \
                is None:
            self.window.add(self.ball, x=item_x, y=item_y)
        elif num == 6 and self.window.get_object_at(self.extra_ball.x+self.extra_ball.width/2,
                                                    self.extra_ball.y+self.extra_ball.height/2) is None:
            self.window.add(self.extra_ball, x=item_x, y=item_y)

    def move_rewards(self):
        # move items
        if self.window.get_object_at(self.lengthen.x, self.lengthen.y) is not None:
            self.lengthen.move(dx=0, dy=8)
        if self.window.get_object_at(self.shorten.x, self.shorten.y) is not None:
            self.shorten.move(dx=0, dy=5)
        if self.window.get_object_at(self.speed_up.x, self.speed_up.y) is not None:
            self.speed_up.move(dx=0, dy=5)
        if self.window.get_object_at(self.speed_down.x, self.speed_down.y) is not None:
            self.speed_down.move(dx=0, dy=8)

        # remove item that is out of the window
        if self.lengthen.y > self.window.height:
            self.window.remove(self.lengthen)
        if self.shorten.y > self.window.height:
            self.window.remove(self.shorten)
        if self.speed_up.y > self.window.height:
            self.window.remove(self.speed_up)
        if self.speed_down.y > self.window.height:
            self.window.remove(self.speed_down)

    def earn_reward(self):
        # paddle hits rewards
        if self.show_long_paddle:
            left_side = self.window.get_object_at(self.long_paddle.x, self.long_paddle.y - 1)
            middle = self.window.get_object_at(self.long_paddle.x + self.long_paddle.width / 2, self.long_paddle.y - 1)
            right_side = self.window.get_object_at(self.long_paddle.x + self.long_paddle.width, self.long_paddle.y - 1)
        else:
            left_side = self.window.get_object_at(self.paddle.x, self.paddle.y-1)
            middle = self.window.get_object_at(self.paddle.x+self.paddle.width/2, self.paddle.y-1)
            right_side = self.window.get_object_at(self.paddle.x+self.paddle.width, self.paddle.y-1)

        # after hitting rewards
        if left_side is self.lengthen or right_side is self.lengthen or middle is self.lengthen:  # lengthen paddle
            self.show_long_paddle = True
            self.long_paddle.color = 'black'
            self.long_paddle.filled = True
            self.long_paddle.fill_color = 'black'
        if left_side is self.shorten or right_side is self.shorten or middle is self.shorten:  # shorten paddle
            self.show_long_paddle = False
            self.long_paddle.color = 'white'
            self.long_paddle.filled = True
            self.long_paddle.fill_color = 'white'
        if left_side is self.speed_up or right_side is self.speed_up or middle is self.speed_up:  # speed up
            if 1 < self.__dy < 15:
                self.__dy += 1
            elif -15 < self.__dy < -1:
                self.__dy -= 1
            if 1 < self.__extra_dy < 15:
                self.__extra_dy += 1
            elif -15 < self.__extra_dy < -1:
                self.__extra_dy -= 1
        if left_side is self.speed_down or right_side is self.speed_down or middle is self.speed_down:  # speed down
            if 1 < self.__dy < 15:
                self.__dy -= 1
            elif -15 < self.__dy < -1:
                self.__dy += 1
            if 1 < self.__extra_dy < 15:
                self.__extra_dy -= 1
            elif -15 < self.__extra_dy < -1:
                self.__extra_dy += 1

        # remove rewards
        if left_side is not None and left_side is not self.ball and left_side is not self.extra_ball:
            self.window.remove(left_side)
        if middle is not None and middle is not self.ball and middle is not self.extra_ball:
            self.window.remove(middle)
        if right_side is not None and right_side is not self.ball and right_side is not self.extra_ball:
            self.window.remove(right_side)

    # Dealing with Game Start and Over

    def set_ball_position(self):
        self.game_start = False
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

    def no_bricks(self):
        if self.bricks_num <= 0:
            return True

    def lose(self):
        self.remove_all_obj()
        lose = GLabel('Game Over')
        lose.font = 'Courier-80-bold'
        self.window.add(lose, x=(self.window.width-lose.width)/2, y=self.window.height/2)
        self.window.add(self.score_board, x=(self.window.width - self.score_board.width) / 2, y=lose.y + 100)

    def win_line(self):
        self.remove_all_obj()
        win = GLabel('You Win!!')
        win.font = 'Courier-80-bold'
        self.window.add(win, x=(self.window.width-win.width)/2, y=self.window.height/2)
        self.window.add(self.score_board, x=(self.window.width - self.score_board.width) / 2, y=win.y + 100)

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
