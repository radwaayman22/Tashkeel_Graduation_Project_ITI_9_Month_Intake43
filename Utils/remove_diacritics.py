def remove_diacritics(content):
    # remove daicritic from arabic text and return text without daicritic
    DIACRITICS_LIST = ['َ', 'ً', 'ُ', 'ٌ', 'ِ', 'ٍ', 'ْ', 'ّ', 'َّ', 'ًّ', 'ُّ', 'ٌّ', 'ِّ', 'ٍّ','']
    return content.translate(str.maketrans('', '', ''.join(DIACRITICS_LIST)))