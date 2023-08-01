def shadda_correction(word ,probs ):
    """
    Rules for Shadda :-
    It is a space, 0(for number ) or one of the following: 'ا' ,'ء' , 'أ' ,'إ' ,'ة' , 'ئ' ,'آ', 'ى'
    It is the first letter of the Arabic word

    """
    forbidden_chars = ['ء' , 'أ' ,'إ' ,'ة' , 'ئ' , 'ى']
    for i, (char, prob) in enumerate(zip(word, probs)):

        if (np.argmax(prob) in [7 , 8 , 9 , 10 , 11 , 12 , 13]) and ((char in forbidden_chars )or (i == 0 ) or word[i-1] ==' '):

            if np.argmax(prob) == 8 :
                probs[i][0] = 1.0
           
            elif np.argmax(prob) == 9:
                probs[i][1] = 1.0
               
            elif np.argmax(prob) == 10:
                probs[i][2] = 1.0
               
            elif np.argmax(prob) == 11:
                probs[i][3] = 1.0
                
            elif np.argmax(prob) == 12:
                probs[i][4] = 1.0
            elif np.argmax(prob) == 13:
                probs[i][5] = 1.0

            probs[i][7:14] = [0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0]
        if char == ' ':
            probs[i][0:14] = [0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 ,0.0 ,0.0 ,0.0 ,0.0 , 0.0 , 0.0 , 0.0 , 0.0 ]
            probs[i][14] = 1.0



    return probs

