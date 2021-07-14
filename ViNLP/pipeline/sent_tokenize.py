from os import path

from ..features.ss_feature import SSFeature
from ..models.ss_crf import SS_CRF
from ..utils.regex_tokenize import tokenize

crf_model = SS_CRF.load(path.join(path.dirname(__file__), "bin", "ss.crfsuite"))


def sent_tokenize(sentence):
    global crf_model
    tokens = tokenize(sentence)
    _tokens = [(token, "O") for token in tokens]
    x = SSFeature().transform([_tokens])[0]
    tags = crf_model.predict(x)[0]

    output = []
    sent = []
    for tag, token in zip(tags, tokens):
        sent.append(token)
        if tag == "EOS":
            output.append(' '.join(sent))
            sent = []
    if len(sent) != 0:
        output.append(' '.join(sent))
    return output
