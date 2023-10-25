#keep only the arabic text to feed it to the model to predict the corresponding diacritics
import re
def DeploymentTextPreprocessing(text):
    #remove any non-arabic characters
    cleaned_sentence = re.sub(r'[^\u0600-\u06FF]+', ' ', text)
    #remove all diacritical marks (harakat)
    cleaned_sentence = re.sub(r'[\u064b-\u0652]', '', cleaned_sentence)
    #remove tatweel (ـ)
    cleaned_sentence = re.sub('\u0640', '', cleaned_sentence)
    return cleaned_sentence
