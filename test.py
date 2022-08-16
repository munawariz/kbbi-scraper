from kbbi_scraper import Word

kambing = Word('kambing')

for arti in kambing.definition:
    print(arti.word)
    print(arti.meaning)