def score(game):
    result = 0
    frame = 1
    first_ball_of_frame = True
    previous_point = 0
    for roll in range(len(game)):
        roll_char = game[roll]
        roll_point = get_value(roll_char)
        result += get_frame_result(roll_char, previous_point, roll_point)
        if frame < 10 and roll_point == 10:
            next_frame_ball_1 = game[roll + 1] 
            next_frame_ball_2 = game[roll + 2]
            result += get_value(next_frame_ball_1)
            if is_strike(roll_char):
                result += get_frame_result(next_frame_ball_2, get_value(next_frame_ball_1), get_value(next_frame_ball_2))
        previous_point = roll_point
        if not first_ball_of_frame:
            frame += 1
        first_ball_of_frame = not first_ball_of_frame
        if is_strike(roll_char):
            first_ball_of_frame = True
            frame += 1
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif is_strike(char):
        return 10
    elif is_spare(char):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def is_strike(char):
    return char == 'X' or char == 'x'


def is_spare(char):
    return char == '/'


def get_spare_result(previous_point):
    return 10 - previous_point


def get_frame_result(char, spare_point, normal_point):
    if is_spare(char):
        return get_spare_result(spare_point)
    else:
        return normal_point
