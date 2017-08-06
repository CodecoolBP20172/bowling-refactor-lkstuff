def score(game):
    result = 0
    frame = 1
    first_ball_of_frame = True
    for i in range(len(game)):
        if is_spare(game[i]):
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10  and get_value(game[i]) == 10:
            if is_spare(game[i]):
                result += get_value(game[i+1])
            elif is_strike(game[i]):
                result += get_value(game[i+1])
                if is_spare(game[i+2]):
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not first_ball_of_frame:
            frame += 1
        first_ball_of_frame = not first_ball_of_frame
        if is_strike(game[i]):
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

