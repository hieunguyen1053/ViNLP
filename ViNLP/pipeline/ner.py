from os import path

from ..features.ner_feature import NERFeature
from ..models.ner_crf import NER_CRF
from .chunking import chunk

crf_model = NER_CRF.load(path.join(path.dirname(__file__), "bin", "ner.crfsuite"))


def ner(sentence):
    global crf_model
    tokens = chunk(sentence)
    _tokens = [(token[0], token[1], token[2], "X") for token in tokens]
    x = NERFeature().transform([_tokens])[0]
    tags = crf_model.predict(x)[0]

    output = []
    for tag, token in zip(tags, tokens):
        output.append((token[0], token[1], token[2], tag))
    return output
