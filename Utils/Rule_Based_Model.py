
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


def harka_correction(word ,probs ):
    """
    Rules for haraka :-
    1-If it is the first letter in the word, forbid Sukoon.
    2-If it is'إ' , set the current diacritic to Kasra, by setting the probability of its class to 1 and the others to 0 .
    3-If it 'ى' is or 'ة' , set the diacritic of the previous character to Fatha .
    4-If it  is 'ا' and the last letter of the word, allow only Fatha, Fathatan, or no diacritic .
    5-If it is 'ا' and not the last letter of the word, set Fatha on the previous character.
    6-If it is not the last character of the word, prohibit any Tanween diacritic from appearing on it.    
    7-If it is a space, 0 or any of the following characters 'آ', 'ى'  ,'ا' to choice to no-diacritic.
    8-If it is the last letter, prohibit Fathatan unless this character is 'ء' or 'ة'.

    """
    for i, (char, prob) in enumerate(zip(word, probs)):
#         print("i: " , i)
#         print("char : " , char)
#         print("prob : ", prob)
        if ((i == 0) or (word[i-1])==' ') :   # first and sukon

#             print("argmax ",np.argmax(prob))

            probs[i][6] = 0.0
        if char == 'إ' : #  hamza maksora
            probs[i][4] = 1.0
            probs[i][0:4] = [0.0 ,0.0 ,0.0 ,0.0]
            probs[i][5:] = [0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 ,0.0 ,0.0 ,0.0 ,0.0  ]
            #print("Kasraaaaa")
        if  char == 'ى' or char == 'ة'  or char =='ا' : #set before fatha
            probs[i-1][0] = 1.0

        if i == (len(word)-1) and char == 'ا': # last
            probs[i][2:14] = [0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 ,0.0 ,0.0 ,0.0 ,0.0 , 0.0 , 0.0 ]

        if i != (len(word)-1) and char == 'ا':
            probs[i][14] = 1.0


        if i != (len(word)-1) : #tanween
            probs[i][1] = 0.0
            probs[i][3] = 0.0
            probs[i][5] = 0.0
            probs[i][9] = 0.0
            probs[i][11] = 0.0
            probs[i][13] = 0.0

        if char == 'آ' or char == 'ى' or char == ' ' :
            probs[i][0:14] = [0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 ,0.0 ,0.0 ,0.0 ,0.0 , 0.0 , 0.0 , 0.0 , 0.0 ]
            probs[i][14] = 1.0
        if i == (len(word)-1) and (char !=  'ء'  and char != 'ة' and char != 'ا' ) :
            probs[i][1] = 0.0



    return probs



def visualize_diacritic_by_index(probs):
    lst = []
    for i in range(len(probs)):
        lst.append(np.argmax(probs[i]))

    return lst




def correction(word , probs ):
    shadda_probs = shadda_correction(word , probs)
    harka_probs = harka_correction(word ,shadda_probs )
    lst = visualize_diacritic_by_index(harka_probs)
    return lst



def fix_predicted_daicritics(x , y_pred , padding_length ):
    ls = []
    for i in range (len(x)):
        
        if len(x[i])<= padding_length:
            lst = correction(x[i] ,y_pred[i] )
            ls.append(lst)
        else:
            lst = correction(x[i][:padding_length] ,y_pred[i] )
            ls.append(lst)
    return ls 