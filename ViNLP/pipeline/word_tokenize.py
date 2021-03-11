from os.path import join

from ViNLP.features.tokenize_feature import TokenizeFeature
from ViNLP.models import CRFTokenizer
from ViNLP.utils.tokenize import tokenize


def word_tokenize(sentence, format=None):
    crf_tokenizer = CRFTokenizer.load(join("pipeline", "bin", "tokenize.crfsuite"))

    tokens = tokenize(sentence)
    _tokens = [(token, "X") for token in tokens]
    x = TokenizeFeature().transform([_tokens])[0]
    tags = crf_tokenizer.predict(x)[0]

    output = []
    for tag, token in zip(tags, tokens):
        if tag == "I-W":
            output[-1] = output[-1] + u" " + token
        else:
            output.append(token)
    if format == "text":
        output = u" ".join([item.replace(" ", "_") for item in output])
    return output
