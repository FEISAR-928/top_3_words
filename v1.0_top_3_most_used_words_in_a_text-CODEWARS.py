import re

def top_3_words(text):
    top3words_list = []
    k = 0
    
    text = text.lower()
    text_cleaned = re.sub('[^a-z \']'," ",text)
    text_words = text_cleaned.split()
    
    tallywords_list = [(i,text_words.count(i)) for i in set(text_words)]
    tallywords_list.sort(key=lambda x: x[1], reverse=True)

    if tallywords_list != []:
        while (k < 3):
            top3words_list.append(tallywords_list[k][0])
            k = k + 1
            if k >= len(tallywords_list):
                break
    else:
        top3words_list = tallywords_list
        return top3words_list
    
    for l in top3words_list:
        if ( ("'" in l) and (bool(re.search('[a-z]', l)) == False) ):
            top3words_list.remove(l)
    
    return top3words_list
