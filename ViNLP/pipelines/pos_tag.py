from os import path

from ..features.pos_feature import POSFeature
from ..models.pos_crf import POS_CRF
from .word_tokenize import word_tokenize

crf_model = POS_CRF.load(path.join(path.dirname(__file__), "bin", "pos.crfsuite"))


def pos_tag(sentence):
    global crf_model
    tokens = word_tokenize(sentence)
    _tokens = [(token, "X") for token in tokens]
    x = POSFeature().transform([_tokens])[0]
    tags = crf_model.predict(x)[0]

    output = []
    for tag, token in zip(tags, tokens):
        output.append((token, tag))
    return output
