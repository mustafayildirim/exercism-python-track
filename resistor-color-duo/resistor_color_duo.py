MAP = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    decoded_value = ''
    if len(colors) > 2:
        colors = colors[:2]

    for color in colors:
        decoded_value += str(MAP.index(color))
    
    return int(decoded_value)