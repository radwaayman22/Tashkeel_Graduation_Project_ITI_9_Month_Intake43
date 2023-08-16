

# Removing anything else arabic letters ,space and daicritics
def data_wrangling(text):
    import re
    """ 
    Paramter : Arabic text
    Function : Applying regex pattern for removing (white spaces , kasheeda (tatweela) ,punctuations) and anything else arabic letters ,space and daicritics
    Return : Cleaned arabic text containing only arabic letters ,space and daicritics
    """
    content_1 = re.sub(r'[^\u0600-\u06FF]+', ' ', text)
    content_2 = re.sub(r'[\u06D2]+', ' ', content_1)
    content_3 = re.sub(r'ـ', '', content_2)

    return content_3