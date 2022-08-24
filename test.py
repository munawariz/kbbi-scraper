from kbbi_scraper import Word

WORD_BENCHMARK = [
    'kambing',
    'ikan'
]

kambing = Word('kambing')
print(kambing.base_word)
print(kambing.syllables)
print(kambing.definition)
print(kambing.pribahasa)