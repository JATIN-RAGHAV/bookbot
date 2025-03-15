def getWordCount(text):
    return len(text.split())

def getCharacterCount(text):
    dict = {}
    for c in text:
        c = c.lower()
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    return dict
