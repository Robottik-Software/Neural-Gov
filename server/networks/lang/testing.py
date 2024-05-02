from textblob import TextBlob


def break_down_into_sentences(paragraph):
    blob = TextBlob(paragraph)
    sentences = blob.sentences
    return sentences


paragraph = "Demonstrative content example. Later we will be testing other content."
sentences = break_down_into_sentences(paragraph)
for sentence in sentences:
    print(sentence)
