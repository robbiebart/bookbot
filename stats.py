def get_num_words(text):
    split_text = text.split()
    return len(split_text)

letters_dict = {}
def character_count(text):
    lowercased = text.lower()


    for character in lowercased:
        if character in letters_dict:
            letters_dict[character] += 1
        else: 
            letters_dict[character] = 1
    # print(letters_dict)
    return letters_dict

def sort_on(dict):
    return dict["num"]

def sort_dictionaries(char_count):
    char_list = []
    alpha_list = []
    
    # def sort_on(dict):
    #     return dict["num"]

    for character in char_count:
        # print(character)
        dictionary = {"char": character, "num": letters_dict[character]}
        char_list.append(dictionary)

    for d in char_list:
        if d["char"].isalpha() == True:
            alpha_list.append(d)
    
    
    alpha_list.sort(reverse=True, key=sort_on)

    return alpha_list