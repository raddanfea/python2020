TEXT = """"A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata. 
A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során. 
A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekinettel a katalán önállósodási törekvésekre.\""""


def main():
    dict = {'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o',
            'ö': 'o',
            'ő': 'o',
            'ú': 'u',
            'ü': 'u',
            'ű': 'u'
            }

    # nagy betűkre is
    dict2 = {}
    for k, v in dict.items():
        dict2[k.upper()] = v.upper()
    dict.update(dict2)

    outp = ""
    for word in TEXT:
        for char in word:
            if char in dict.keys():
                outp = outp + dict[char]
            else:
                outp = outp + char

    print(outp)


if __name__ == '__main__':
    main()
