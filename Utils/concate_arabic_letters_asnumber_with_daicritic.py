
def concate_arabic_letters_asnumber_with_daicritic(arabic_lett ,arabic_daic ,max_padding_length ): 
    """
    paramters : taking mapped text into numbers and it's daicritics mapped into numbers and max padding length
    functions : mapped them into arabic letters & original daicritics and join them
    return : arabic text joined with it's daicritics
    """
    char_lis=[INDEX2CHAR[arabic_lett[i]] for i in range(len(arabic_lett))]
    diac_lis=[INDEX2DIAC[arabic_daic[i]] for i in range(len(arabic_daic))]
    str_with_daic = ""
    for i in range(min(len(arabic_lett) , max_padding_length )):
        a = char_lis[i]+diac_lis[i]
        str_with_daic = str_with_daic + a
    return str_with_daic