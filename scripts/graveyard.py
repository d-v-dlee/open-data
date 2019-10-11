def shot_location_numeric(shot_location_start):
    """
    takes a location that is a string '[103.0, 21.0]' and turn it into a list of floats [103.0, 21.0]
    """
    # pull only numbers and punctuation
    numbers = ''.join(x for x in shot_location_start if x in string.digits or x in [',', '.'])
    # split
    number_list = numbers.split(',')
    # turn into list of ints
    final_location = [float(x) for x in number_list]

    return final_location

def transpose_shot(shot_location_start):
    """
    if a shot occurs past the halfway line, tranpose the shot in x and y.
    NOTE: Unnecessary cause all shots are on the right side of the field...
    """
    if shot_location_start[0] > 60:
        x = 120 - shot_location_start[0]
        y = 80 - shot_location_start[1]
        return [x, y]
    else:
        return shot_location_start