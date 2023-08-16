def visualize_diacritic_by_index(probs):
    lst = []
    for i in range(len(probs)):
        lst.append(np.argmax(probs[i]))

    return lst