def is_diacritic(char):
    # if paramter in diacritic list return True else False
    diacritic = ['َ', 'ً', 'ُ', 'ٌ', 'ِ', 'ٍ', 'ْ', 'ّ', 'َّ', 'ًّ', 'ُّ', 'ٌّ', 'ِّ', 'ٍّ','']

    return char in diacritic