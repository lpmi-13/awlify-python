from awlify.utils.check_word import check_word_in_list
import spacy

nlp = spacy.load('en_core_web_sm')


def check_word_in_sentence(sentence):

    doc = nlp(sentence)

    tokenized = [token.text for token in doc]
    awl_words = []

    for word in tokenized:
        if (check_word_in_list(word) is not None):
            index = tokenized.index(word)
            awl_words.append({
                "index": index,
                "word": word,
                "meta": check_word_in_list(word)
            })
        else:
            continue

    return {"data": {"sentence": sentence, "awl_words": awl_words}}
