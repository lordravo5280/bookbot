def num_words(text):
        words = text.split()
        return len(words)

def num_characters(text):
        counts = {}
        characters = list(text.lower())
        for character in characters:
                if character in counts:
                        counts[character] += 1
                else:
                        counts[character] = 1
        return(counts)

def sort_by_count(dict_item):
        return dict_item["count"]

def sorted_list(counts):
        chars_list = []
        for char, count in counts.items():
                char_dict = {"char": char, "count": count}
                chars_list.append(char_dict)
        chars_list.sort(reverse=True, key=sort_by_count)
        return chars_list
