def rovare(msg):
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r",
                  "s", "t", "v", "w", "x", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M",
                  "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    outstring = ""
    for char in msg:
        if char in consonants:
            outstring += char + "o" + char.lower()
        else:
            outstring += char

    return outstring


def swede(msg):
    pass
    # TODO write code  to translate rovarelanguage to swedish
