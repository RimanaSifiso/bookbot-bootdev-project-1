def get_number_of_words(file_contents: str) -> int:
    return len(file_contents.split())


def get_char_frequency(file_contents:str) -> dict[str, int]:
    chars = file_contents.lower()
    char_freq = {}
    for char in chars:
        if char in char_freq.keys():
            char_freq[char] += 1
        elif char != " ":
            char_freq[char] = 1
    
    return char_freq

def chars_dict_to_sorted_list(char_freq: dict[str, int]) -> list[dict[str, int]]:
    result_list = []
    for char, char_count in char_freq.items():
        result_list.append(dict(char=char, num=char_count))
    
    result_list.sort(reverse=True, key=lambda o: o['num'])
    return result_list

