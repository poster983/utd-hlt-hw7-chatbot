import nltk
from nltk.corpus import stopwords
def summarize(text: str): 
    #preprocess
    #text = text.lower()
    # get all stopwords
    stop_words = stopwords.words("english")
    #tokenize 
    tokens = nltk.word_tokenize(text);
    # remove stopwords
    tokens = [t.lower() for t in tokens if t not in stop_words]


    #create a freq dict 
    word_freq_dict = {word:tokens.count(word) for word in tokens}

    sentences = nltk.sent_tokenize(text)
    # calc the term frequency by sentence
    sentence_freq_dict = {}
    for s in sentences: 
        for word, tf in word_freq_dict.items():
            if word in s.lower():
                if sentence_freq_dict.get(s, None) != None:
                    sentence_freq_dict[s] += tf #add the term frequency to the sentence to see how relavent it is 
                else:
                    sentence_freq_dict[s] = tf

    # get the total tf from sent dict
    total_value = 0
    for sentence, tf in sentence_freq_dict.items():
        total_value += tf

    #average tf value for each sentence
    averave_tf = total_value/len(sentence_freq_dict)

    # print(averave_tf)

    summary = [s for s in sentences if sentence_freq_dict[s] > averave_tf]
    
    return ' '.join(summary)


