global screen_size
screen_size = (400, 400)
screen_color = (255, 255, 255)
screen_border_color = (79, 124, 186)
n = 4  # kích thước bảng trò chơi
dosau = 2
# board config
# 0 = ô trống, 1 = x, -1 = o


border_thickness = 1 #độ dày viền ô
square_size = 40 #kích thước một ô trong bàn cờ
# tic - tac config

X_color = (0,0,255)
O_color = (255,0,0)
tic_tac_thickness = 5 # độ dày của ký tự X, O
from_border = 12 #khoảng cách từ ký tự X, O đến viền ô

# analyze points
connect_multiple_four1 = 1e9 + 500
connect_four_has_obstacles1 = 1e9
connect_four1 = 1e9
connect_multiple_three1 = 1e7
connect_three_has_obstacles1 = 1e6
connect_three1 = 1e6
connect_multiple_two1 = 300
connect_two_has_obstacles1 = 50
connect_two1 = 200

connect_multiple_four2 = 1e8
connect_four_has_obstacles2 = 1e9
connect_four2 = 1e9
connect_multiple_three2 = 1e7-1
connect_three_has_obstacles2 = 1e5-1
connect_three2 = 1e6-1
connect_multiple_two2 = 10-1
connect_two_has_obstacles2 = 20-1
connect_two2 = 150

dict = {
    'connect_multiple_four1' : connect_multiple_four1,
    'connect_four_has_obstacles1' : connect_four_has_obstacles1,
    'connect_four1' : connect_four1,
    'connect_multiple_three1' :  connect_multiple_three1,
    'connect_three_has_obstacles1' : connect_three_has_obstacles1,
    'connect_three1' : connect_three1,
    'connect_multiple_two1' : connect_multiple_two1,
    'connect_two_has_obstacles1' : connect_two_has_obstacles1,
    'connect_two1' : connect_two1,

    'connect_multiple_four2' : connect_multiple_four2,
    'connect_four_has_obstacles2' : connect_four_has_obstacles2,
    'connect_four2' : connect_four2,
    'connect_multiple_three2' :  connect_multiple_three2,
    'connect_three_has_obstacles2' : connect_three_has_obstacles2,
    'connect_three2' : connect_three2,
    'connect_multiple_two2' : connect_multiple_two2,
    'connect_two_has_obstacles2' : connect_two_has_obstacles2,
    'connect_two2' : connect_two2
}

# text config 
win_text = "Win!"
lose_text = "Lost!"
tie_text = "Tie!"

text_size = 70
text_color = (251, 255, 0)
text_font = 'freesansbold.ttf'