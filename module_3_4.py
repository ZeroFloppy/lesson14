def single_root_words(root_word, *other_words):
    same_words = []
    l_root_word = root_word.lower()
    for word in other_words:
        l_word = word.lower()
        if l_root_word in l_word or l_word in l_root_word:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers',
                            'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable',
                            'Bagel')
print(result1)
print(result2)
