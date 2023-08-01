from tensorflow.keras.preprocessing.sequence import pad_sequences


def padding_sequence(max_length , x ,x_value, y ,y_value ):
    
    max_len = max_length
    X = []
    X = pad_sequences(maxlen=max_len, sequences= x, padding="post", value= x_value)
    Y = []
    Y = pad_sequences(maxlen=max_len, sequences= y, padding="post", value= y_value)
    return X , Y