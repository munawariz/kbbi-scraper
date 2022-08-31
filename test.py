from kbbi_scraper import Word, load_soup_bowl

WORD_BENCHMARK = [
    'kambing',
    'kambing-2',
    'kambing-3',
    'kerah',
    'ikan'
]

for word in WORD_BENCHMARK:
    obj = Word(word)

    print(obj.syllables)
    print(obj.word)
    print(obj.meanings)
    print(obj.derived_words)
    print(obj.proverbs)

# Will be a lot faster since this is using data available locally
# kambinglagi = Word('ikan', cache=False)

# print(kambinglagi.definition)

# # related_words will return a list of Word object, so any function available in its parent is used in the same way
# rumputkambing = kambinglagi.related_words[0]
# print(rumputkambing.definition[0])