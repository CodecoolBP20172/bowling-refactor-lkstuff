def score(game):
    result = 0
    frame = 1
    first_ball_of_frame = True
    for roll in range(len(game)):
        if is_spare(game[roll]):
            result += get_spare_result(previous_point)
        else:
            result += get_value(game[roll])
        if frame < 10  and get_value(game[roll]) == 10:
            if is_spare(game[roll]):
                result += get_value(game[roll+1])
            elif is_strike(game[roll]):
                result += get_value(game[roll+1])
                if is_spare(game[roll+2]):
                    result += get_spare_result(get_value(game[roll+1]))
                else:
                    result += get_value(game[roll+2])
        previous_point = get_value(game[roll])
        if not first_ball_of_frame:
            frame += 1
        first_ball_of_frame = not first_ball_of_frame
        if is_strike(game[roll]):
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