def single_root_words(root_word: str, *other_words: str):
    same_words = []
    for i in other_words:
        if (i.lower()).__contains__(root_word.lower()):
            same_words.append(i)
        elif (root_word.lower()).__contains__(i.lower()):
            same_words.append(i)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'Richies'))
print(single_root_words('Disablement', 'able', 'Mable', 'Disable', 'Bagel'))
