def word_indices(text):
    words = text.lower().split()
    word_dict = {}
    for index, word in enumerate(words):
        
        if word in word_dict:
            word_dict[word].append(index)
        else:
            word_dict[word] = [index]
    
    return word_dict

text = "This is a test. This test is simple."
print(word_indices(text))