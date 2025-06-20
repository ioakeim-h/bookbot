from collections import Counter

def count_words(text):
    return len(text.split())

def count_characters(text):
    return dict(Counter(text.lower()))

def sort_characters_dict(n_chars_dict):
    def sort_on(items):
        return items["num"]
    
    list_of_dicts = [{"char": k, "num": v} for k, v in n_chars_dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts





