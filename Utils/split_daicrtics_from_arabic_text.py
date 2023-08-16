# import sys
# sys.path.append('/content/drive/MyDrive/Utils - Copy')
from is_char import is_char
from is_diacritic import is_diacritic

ARABIC_LETTERS = frozenset([chr(x) for x in (list(range(0x0621, 0x63B)) + list(range(0x0641, 0x064B)))])
diacritic = ['َ', 'ً', 'ُ', 'ٌ', 'ِ', 'ٍ', 'ْ', 'ّ', 'َّ', 'ًّ', 'ُّ', 'ٌّ', 'ِّ', 'ٍّ','']
CHAR2INDEX = dict((l, n) for n, l in enumerate(sorted(ARABIC_LETTERS)))
CHAR2INDEX.update(dict((v, k) for k, v in enumerate([' '], len(CHAR2INDEX))))
DIAC2INDEX= {char: i for i, char in enumerate(diacritic)}

def split_daicrtics_from_arabic_text(text):
    """
    Paramters : arabic text
    Return : list of arabic letters mapped into numbers + list of daicrtics mapped into numbers
    Functionaity : remove daicrtics from arabic letters
    """
    arabic_lett = []
    arabic_daic = []
    for i in range(len(text)):
        if not is_char(text[i]) and not is_diacritic(text[i]):#other 
            continue
        if is_diacritic(text[i]) and i ==0 : # the first char in daicritic 
            continue 
        if text[i-1].isspace() and  is_diacritic(text[i]):
            arabic_daic.append(DIAC2INDEX[''])
        elif not is_diacritic(text[i]):
            arabic_lett.append(CHAR2INDEX[text[i]])
            if ( i < len(text)-1  and  not is_diacritic(text[i+1]) ) or i ==len(text)-1:
                arabic_daic.append(DIAC2INDEX[''])
        elif i < len(text)-1 and is_diacritic(text[i]) and is_diacritic(text[i+1]): #shadda
            try:
                arabic_daic.append(DIAC2INDEX[text[i] +text[i+1]] )
            except :
                try:
                    arabic_daic.append(DIAC2INDEX[text[i+1] +text[i]])
                except:
                    arabic_daic.append(DIAC2INDEX[text[i]])
        elif i < len(text)-1 and  is_diacritic(text[i]) and not is_diacritic(text[i+1]) and not is_diacritic(text[i-1]): # normal
            arabic_daic.append(DIAC2INDEX[text[i]])
        elif i == len(text)-1 and  is_diacritic(text[i]) and not is_diacritic(text[i-1]):
            arabic_daic.append(DIAC2INDEX[text[i]])
                    
    return arabic_lett , arabic_daic     
                
        