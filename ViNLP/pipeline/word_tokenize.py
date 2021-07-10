from os import path

from ..features.ws_feature import WSFeature
from ..models.ws_crf import WS_CRF
from ..utils.regex_tokenize import tokenize

crf_model = WS_CRF.load(path.join(path.dirname(__file__), "bin", "ws.crfsuite"))


def word_tokenize(sentence):
    global crf_model
    tokens = tokenize(sentence)
    _tokens = [(token, "X") for token in tokens]
    x = WSFeature().transform([_tokens])[0]
    tags = crf_model.predict(x)[0]

    output = []
    for tag, token in zip(tags, tokens):
        if tag == "I-W":
            output[-1] = output[-1] + "_" + token
        else:
            output.append(token)
    return output
