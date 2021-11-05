points = {"AEIOULNRST": 1, "DG": 2,"BCMP":3, "FHVWY": 4, "K":5, "JX": 8, "QZ": 10 }

def score(word):
    letter_points = {}
    for item in points.items():
        key, letter_value = item
        for letter in key:
            letter_points[letter.lower()] = letter_value

    total_point = 0
    for letter in word.lower():
        total_point += letter_points[letter]

    return total_point
