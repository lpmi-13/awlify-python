from awlify.utils.awl_full_results import awl_list


def check_word_in_list(word):
    if isinstance(word, str) and word in awl_list:
        return awl_list[word]
    else:
        return None
