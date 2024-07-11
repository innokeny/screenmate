import random

def choose_action(screen_mate):
    action = random.choice(['stand', 'evade', 'chase'])
    print(f"Action chosen: {action}")  # Отладочное сообщение

    if action == 'evade':
        screen_mate.mode = 'evade'
    elif action == 'chase':
        screen_mate.mode = 'chase'
    else:
        screen_mate.stop_moving()

def move_relative_to_mouse(screen_mate, chase=True):
    mouse_pos = screen_mate.cursor().pos()
    screen_mate_pos = screen_mate.pos()
    
    if chase:
        x_diff = mouse_pos.x() - screen_mate_pos.x()
        y_diff = mouse_pos.y() - screen_mate_pos.y()
    else:
        x_diff = screen_mate_pos.x() - mouse_pos.x()
        y_diff = screen_mate_pos.y() - mouse_pos.y()

    if abs(x_diff) > abs(y_diff):
        direction = 'move_r' if x_diff > 0 else 'move_l'
    else:
        direction = 'move_d' if y_diff > 0 else 'move_u'

    if direction == 'move_l':
        screen_mate.movie = screen_mate.mLeft
    elif direction == 'move_r':
        screen_mate.movie = screen_mate.mRight
    elif direction == 'move_u':
        screen_mate.movie = screen_mate.mUp
    elif direction == 'move_d':
        screen_mate.movie = screen_mate.mDown

    screen_mate.setMovie(screen_mate.movie)
    screen_mate.start_moving()


# def choose_action(screen_mate):
#     action = random.choice(['stand', 'move_r', 'move_l', 'move_u', 'move_d'])
#     print(f"Action chosen: {action}")  # Отладочное сообщение

#     if action == 'move_r':
#         screen_mate.movie = screen_mate.mRight
#         screen_mate.setMovie(screen_mate.movie)
#         screen_mate.start_moving()
#     elif action == 'move_l':
#         screen_mate.movie = screen_mate.mLeft
#         screen_mate.setMovie(screen_mate.movie)
#         screen_mate.start_moving()
#     elif action == 'move_u':
#         screen_mate.movie = screen_mate.mUp
#         screen_mate.setMovie(screen_mate.movie)
#         screen_mate.start_moving()
#     elif action == 'move_d':
#         screen_mate.movie = screen_mate.mDown
#         screen_mate.setMovie(screen_mate.movie)
#         screen_mate.start_moving()
#     else:
#         screen_mate.stop_moving()