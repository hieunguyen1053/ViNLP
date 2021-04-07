from os import path

from ..features.tokenize_feature import TokenizeFeature
from ..models.crf_word_tokenizer import CRFTokenizer
from ..utils.tokenize import tokenize


def word_tokenize(sentence):
    crf_tokenizer = CRFTokenizer.load(path.join(path.dirname(__file__), "bin", "tokenize.crfsuite"))

    tokens = tokenize(sentence)
    _tokens = [(token, "X") for token in tokens]
    x = TokenizeFeature().transform([_tokens])[0]
    tags = crf_tokenizer.predict(x)[0]

    output = []
    for tag, token in zip(tags, tokens):
        if tag == "I-W":
            output[-1] = output[-1] + "_" + token
        else:
            output.append(token)
    return output
