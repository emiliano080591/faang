def get_position(letter: str) -> int:
    abc = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
           'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
           'y': 24, 'z': 25}

    if letter in abc:
        return abc[letter]
    return None


def designer_pdf_viewer(h: [int], word: str) -> int:
    values = []
    for c in word:
        pos = get_position(c)
        if pos is not None:
            values.append(h[pos])

    max_height = max(values)
    return max_height * len(word)


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    print(designer_pdf_viewer(h, word))
