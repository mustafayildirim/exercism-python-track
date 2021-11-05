def abbreviate(words):
    words = words.replace(', ', ' ').replace('-', ' ').replace("'", '').replace('_', '')
    splitted_word = words.split()
    acronym = ''
    for word in splitted_word:
        acronym += word[0]

    return acronym.upper()
