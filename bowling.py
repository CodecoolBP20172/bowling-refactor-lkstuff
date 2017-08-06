def score(game):
    result = 0
    frame = 1
    first_ball_of_frame = True
    for roll in range(len(game)):
        roll_char = game[roll]
        roll_point = get_value(roll_char)
        if is_spare(roll_char):
            result += get_spare_result(previous_point)
        else:
            result += roll_point
        if frame < 10 and roll_point == 10:
            result += get_value(game[roll+1])
            if is_strike(roll_char):
                if is_spare(game[roll+2]):
                    result += get_spare_result(get_value(game[roll+1]))
                else:
                    result += get_value(game[roll+2])
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
