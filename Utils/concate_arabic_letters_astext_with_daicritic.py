def concate_arabic_letters_astext_with_daicritic(arabic_lett ,arabic_daic ,max_padding_length ):
    """
    paramters : taking  original text  and it's daicritics mapped into numbers and max padding length
    functions : mapped daicritics into original daicritics and join arabic letters with it 
    return : arabic text joined with it's daicritics
    """
    daic_lis = [INDEX2DIAC[arabic_daic[i]] for i in range(len(arabic_daic))]
    str_with_daic = ""
    for i in range(min(len(arabic_lett) , max_padding_length )):
        a = arabic_lett[i] + daic_lis[i]
        str_with_daic = str_with_daic + a
    return str_with_daic
        