from kbbi_scraper import Word, load_soup_bowl

WORD_BENCHMARK = [
    'kambing',
    'ikan'
]

kambing = Word('kambing')

print(kambing.definition)

# Will be a lot faster since this is using data available locally
kambinglagi = Word('kambing')

print(kambinglagi.definition)

# related_words will return a list of Word object, so any function available in its parent is used in the same way
rumputkambing = kambinglagi.related_words[0]
print(rumputkambing.definition[0])