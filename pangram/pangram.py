import string

def is_pangram(sentence):

    if len(sentence) > 0:
        sentence = sentence.lower()
        for char in string.ascii_lowercase:
            count = sentence.count(char)
            if count == 0:
                return False
        return True
    
    return False
