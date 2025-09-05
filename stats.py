def num_word_count(text):
    return len(text.split())
    
def num_char(text):
    my_dict = {}
    for i in text:
        lower_char = i.lower()
        if lower_char in my_dict:
            my_dict[lower_char] += 1
        else:
            my_dict[lower_char] = 1
    return my_dict

def get_char_num(d):
    return d["num"]

def dict_sorted(my_dict):
    new_list = []
    for char, num in my_dict.items():
        new_dict = {"char": char, "num": num}
        new_list.append(new_dict)
    new_list.sort(key=get_char_num, reverse=True)
    return new_list
