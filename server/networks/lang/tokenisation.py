import re


class TokenisationNetwork:
    def __init__(self, *args, **kwargs):
        pass

    def tokenise(self, sentence):
        pattern = r"[\w']+|[.,!?;]+"
        tokens = re.findall(pattern, sentence)
        phrases = []
        current_phrase = ""

        for token in tokens:
            # If token is punctuation, add it to the current phrase
            if re.match(r"[.,!?;]+", token):
                current_phrase += token
                phrases.append(current_phrase.strip())
                current_phrase = ""
            # If token is a word, add it to the current phrase
            else:
                current_phrase += " " + token.strip()

        if current_phrase:
            phrases.append(current_phrase.strip())

        return phrases


new = TokenisationNetwork()

print(new.tokenise("Hi Im steve and I love cheese! Every so often I go to halifax. Wait, where do you live?"))
