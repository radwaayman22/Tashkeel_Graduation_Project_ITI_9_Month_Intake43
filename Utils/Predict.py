
def predict(text , saved_model , padding_length):
    """
    parmeters : arabic text without daicritics , saved model , padding max length
    functions : mapping text into numbers and apply padding and predict using model 
    Return : 2 lists :-
    1-list of predictions as probalities list for each  char without taking armax probalities
    2- list of predictions as value for each  char with taking armax of probalities
    
    """
    max_len = padding_length
    X = []
    for char in text :
        X.append(CHAR2INDEX.get(char, len(CHAR2INDEX)-1) )
    X = pad_sequences(maxlen=max_len, sequences=[X], padding="post", value=len(CHAR2INDEX)-1)
    y = saved_model.predict(X)
#     print(y.shape)
    y_crop = y[0][:min(len(text), padding_length)][:]
    p = np.argmax(y_crop, axis=-1)
#     print(y_crop.shape)
    return y_crop ,p