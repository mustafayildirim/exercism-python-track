MAP = {1: 'jump', 2: 'close your eyes', 3: 'double blink', 4: 'wink'}

def commands(binary_str):

    if not binary_str or len(binary_str) != 5:
        return []

    reverse = False
    output = []
    if binary_str[0] == '1':
        reverse = True
    
    for index in range(4):
        if binary_str[4 - index] == '1':
            output.append(MAP[4 - index])
    
    if reverse:
        output.reverse()

    return output
