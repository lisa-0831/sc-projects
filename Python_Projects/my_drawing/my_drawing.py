"""
File: my_drawing.py
Name: PEI-WEN(Lisa) WANG
----------------------
Kaonashi is one of my favorite characters in Hayao Miyazaki's works.
When I first watched this animation when I was a child, I was scared of this character. However, when I grew up, I
realized that this role is very close to our lives. At some moments, I'm also left with a feeling of emptiness that
people usually resist as soon as possible because they think it is a negative emotion.
However, I think it is not a bad thing to have these emotions. Instead of resisting them, I think it is better to
embrace them and learn how to get along with them. So, I let users decide the character's emotion, which means users
can draw a mouth in this drawing. No matter it's a happy face or a sad face, they all look good. :)
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged, onmouseclicked

# Constants
SIZE = 16

# Global Variables
window = GWindow(width=800, height=600, title='無臉男 (カオナシ / Kaonashi)')


def main():
    """
    Life has its ups and downs. Users can finish this drawing according to their current feelings.
    They can draw a happy face, sad face, angry face, or they can do nothing and get a poker face.
    """
    onmouseclicked(draw_mouth)
    onmousedragged(draw_mouth)

    # background
    sky = GRect(800, 500)
    sky.color = 'skyblue'
    sky.filled = True
    sky.fill_color = 'skyblue'
    window.add(sky)

    cloud_1 = GOval(150, 100, x=0, y=450)
    cloud_1.color = 'snow'
    cloud_1.filled = True
    cloud_1.fill_color = 'snow'
    window.add(cloud_1)

    cloud_2 = GOval(200, 150, x=80, y=400)
    cloud_2.color = 'snow'
    cloud_2.filled = True
    cloud_2.fill_color = 'snow'
    window.add(cloud_2)

    cloud_3 = GOval(300, 250, x=400, y=350)
    cloud_3.color = 'snow'
    cloud_3.filled = True
    cloud_3.fill_color = 'snow'
    window.add(cloud_3)

    cloud_4 = GOval(250, 200, x=600, y=450)
    cloud_4.color = 'snow'
    cloud_4.filled = True
    cloud_4.fill_color = 'snow'
    window.add(cloud_4)

    cloud_5 = GOval(200, 80, x=650, y=250)
    cloud_5.color = 'snow'
    cloud_5.filled = True
    cloud_5.fill_color = 'snow'
    window.add(cloud_5)

    cloud_6 = GOval(100, 60, x=600, y=250)
    cloud_6.color = 'snow'
    cloud_6.filled = True
    cloud_6.fill_color = 'snow'
    window.add(cloud_6)

    cloud_7 = GOval(100, 60, x=650, y=230)
    cloud_7.color = 'snow'
    cloud_7.filled = True
    cloud_7.fill_color = 'snow'
    window.add(cloud_7)

    sea = GRect(800, 100, x=0, y=500)
    sea.color = 'seagreen'
    sea.filled = True
    sea.fill_color = 'steelblue'
    window.add(sea)

    water_pattern_1 = GLine(50, 505, 780, 505)  # the first line
    water_pattern_1.color = 'skyblue'
    window.add(water_pattern_1)

    water_pattern_2 = GLine(25, 510, 200, 510)  # the second line
    water_pattern_2.color = 'skyblue'
    window.add(water_pattern_2)

    water_pattern_3 = GLine(600, 510, 740, 510)
    water_pattern_3.color = 'skyblue'
    window.add(water_pattern_3)

    water_pattern_4 = GLine(30, 515, 250, 515)  # the third line
    water_pattern_4.color = 'skyblue'
    window.add(water_pattern_4)

    water_pattern_5 = GLine(590, 515, 760, 515)
    water_pattern_5.color = 'skyblue'
    window.add(water_pattern_5)

    water_pattern_6 = GLine(35, 520, 180, 520)  # the fourth line
    water_pattern_6.color = 'skyblue'
    window.add(water_pattern_6)

    water_pattern_7 = GLine(595, 520, 770, 520)
    water_pattern_7.color = 'skyblue'
    window.add(water_pattern_7)

    water_pattern_8 = GLine(40, 525, 190, 525)  # the fifth line
    water_pattern_8.color = 'skyblue'
    window.add(water_pattern_8)

    water_pattern_9 = GLine(588, 525, 730, 525)
    water_pattern_9.color = 'skyblue'
    window.add(water_pattern_9)

    # label
    label_background = GRect(680, 45, x=40, y=25)
    label_background.color = 'ivory'
    label_background.filled = True
    label_background.fill_color = 'ivory'
    window.add(label_background)

    label = GLabel('Embrace All Your Emotions')
    label.font = 'Courier-45-bold'
    window.add(label, 40, 70)

    reminder = GLabel('*** You can draw a mouth if you want to. ')
    reminder.font = 'Times New Roman-20-italic'
    window.add(reminder, 40, 100)

    emoji = GLabel(chr(128578))
    emoji.font = '-20'
    window.add(emoji, 380, 100)

    # body
    body_1 = GOval(300, 300, x=250, y=150)
    body_1.filled = True
    body_1.fill_color = 'black'
    window.add(body_1)

    body_2 = GPolygon()
    body_2.add_vertex((250, 300))  # top
    body_2.add_vertex((200, 750))  # left
    body_2.add_vertex((370, 750))  # right
    body_2.filled = True
    body_2.fill_color = 'black'
    window.add(body_2)

    body_3 = GPolygon()
    body_3.add_vertex((550, 300))  # top
    body_3.add_vertex((430, 750))  # left
    body_3.add_vertex((600, 750))  # right
    body_3.filled = True
    body_3.fill_color = 'black'
    window.add(body_3)

    body_4 = GRect(300, 500, x=250, y=300)
    body_4.filled = True
    body_4.fill_color = 'black'
    window.add(body_4)

    # face
    face = GOval(210, 250, x=295, y=200)
    face.color = 'white'
    face.filled = True
    face.fill_color = 'white'
    window.add(face)

    # left eye
    left_eye = GOval(35, 35, x=330, y=300)
    left_eye.filled = True
    left_eye.fill_color = 'black'
    window.add(left_eye)

    left_eye_up = GPolygon()
    left_eye_up.add_vertex((333, 285))  # left
    left_eye_up.add_vertex((363, 285))  # right
    left_eye_up.add_vertex((348, 250))  # top
    left_eye_up.color = 'salmon'
    left_eye_up.filled = True
    left_eye_up.fill_color = 'salmon'
    window.add(left_eye_up)

    left_eye_down = GPolygon()
    left_eye_down.add_vertex((333, 350))  # left
    left_eye_down.add_vertex((363, 350))  # right
    left_eye_down.add_vertex((348, 390))  # down
    left_eye_down.color = 'salmon'
    left_eye_down.filled = True
    left_eye_down.fill_color = 'salmon'
    window.add(left_eye_down)

    # right eye
    right_eye = GOval(35, 35, x=435, y=300)
    right_eye.filled = True
    right_eye.fill_color = 'black'
    window.add(right_eye)

    right_eye_up = GPolygon()
    right_eye_up.add_vertex((437, 285))  # left
    right_eye_up.add_vertex((467, 285))  # right
    right_eye_up.add_vertex((452, 250))  # top
    right_eye_up.color = 'salmon'
    right_eye_up.filled = True
    right_eye_up.fill_color = 'salmon'
    window.add(right_eye_up)

    right_eye_down = GPolygon()
    right_eye_down.add_vertex((437, 350))  # left
    right_eye_down.add_vertex((467, 350))  # right
    right_eye_down.add_vertex((452, 390))  # down
    right_eye_down.color = 'salmon'
    right_eye_down.filled = True
    right_eye_down.fill_color = 'salmon'
    window.add(right_eye_down)

    # supporting role 1
    dust_hair_1 = GLine(85, 290, 85, 370)
    window.add(dust_hair_1)
    dust_hair_2 = GLine(40, 330, 130, 330)
    window.add(dust_hair_2)
    dust_hair_3 = GLine(50, 300, 120, 360)
    window.add(dust_hair_3)
    dust_hair_4 = GLine(50, 360, 120, 300)
    window.add(dust_hair_4)
    dust_hair_5 = GLine(70, 295, 105, 365)
    window.add(dust_hair_5)
    dust_hair_6 = GLine(45, 315, 125, 345)
    window.add(dust_hair_6)
    dust_hair_7 = GLine(45, 345, 125, 315)
    window.add(dust_hair_7)
    dust_hair_8 = GLine(105, 295, 70, 364)
    window.add(dust_hair_8)

    dust = GOval(70, 60, x=50, y=300)
    dust.color = 'black'
    dust.filled = True
    dust.fill_color = 'black'
    window.add(dust)

    dust_left_eye = GOval(15, 15, x=70, y=320)
    dust_left_eye.color = 'white'
    dust_left_eye.filled = True
    dust_left_eye.fill_color = 'white'
    window.add(dust_left_eye)

    dust_left_eyeball = GOval(5, 5, x=77, y=324)
    dust_left_eyeball.filled = True
    dust_left_eyeball.fill_color = 'black'
    window.add(dust_left_eyeball)

    dust_right_eye = GOval(15, 15, x=90, y=320)
    dust_right_eye.color = 'white'
    dust_right_eye.filled = True
    dust_right_eye.fill_color = 'white'
    window.add(dust_right_eye)

    dust_right_eyeball = GOval(5, 5, x=93, y=324)
    dust_right_eyeball.filled = True
    dust_right_eyeball.fill_color = 'black'
    window.add(dust_right_eyeball)

    # supporting role 2
    dust2_hair_1 = GLine(685, 140, 685, 220)
    window.add(dust2_hair_1)
    dust2_hair_2 = GLine(640, 180, 730, 180)
    window.add(dust2_hair_2)
    dust2_hair_3 = GLine(650, 150, 720, 210)
    window.add(dust2_hair_3)
    dust2_hair_4 = GLine(650, 210, 720, 150)
    window.add(dust2_hair_4)
    dust2_hair_5 = GLine(670, 145, 705, 215)
    window.add(dust2_hair_5)
    dust2_hair_6 = GLine(645, 165, 725, 195)
    window.add(dust2_hair_6)
    dust2_hair_7 = GLine(645, 195, 725, 165)
    window.add(dust2_hair_7)
    dust2_hair_8 = GLine(705, 145, 670, 214)
    window.add(dust2_hair_8)

    dust2 = GOval(70, 60, x=650, y=150)
    dust2.color = 'black'
    dust2.filled = True
    dust2.fill_color = 'black'
    window.add(dust2)

    dust2_left_eye = GOval(15, 15, x=670, y=170)
    dust2_left_eye.color = 'white'
    dust2_left_eye.filled = True
    dust2_left_eye.fill_color = 'white'
    window.add(dust2_left_eye)

    dust2_left_eyeball = GOval(5, 5, x=677, y=170)
    dust2_left_eyeball.filled = True
    dust2_left_eyeball.fill_color = 'black'
    window.add(dust2_left_eyeball)

    dust2_right_eye = GOval(15, 15, x=690, y=170)
    dust2_right_eye.color = 'white'
    dust2_right_eye.filled = True
    dust2_right_eye.fill_color = 'white'
    window.add(dust2_right_eye)

    dust2_right_eyeball = GOval(5, 5, x=693, y=170)
    dust2_right_eyeball.filled = True
    dust2_right_eyeball.fill_color = 'black'
    window.add(dust2_right_eyeball)


def draw_mouth(mouse):
    stroke = GOval(SIZE, SIZE)
    stroke.filled = True
    stroke.fill_color = 'black'
    window.add(stroke, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)


if __name__ == '__main__':
    main()
