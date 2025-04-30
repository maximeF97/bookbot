def words_counte(text):
    words_count = 0
    words = text.split()
    words_count = len(words) 
    return words_count 

def char_count(text):
    char_dict = {} 
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

    
def char_organizer(char_dict):
    char_list = []
    
    
    for char, count in char_dict.items():
        
        char_dict_item = {"char": char, "num": count}
        char_list.append(char_dict_item)
    
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list