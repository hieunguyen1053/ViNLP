from os import path

from ..features.tokenize_feature import TokenizeFeature
from ..models.crf_pos_tagger import CRFPosTagger

from .word_tokenize import word_tokenize


def pos_tag(sentence):
    crf_model = CRFPosTagger.load(path.join(path.dirname(__file__), "bin", "pos_tag.crfsuite"))

    tokens = word_tokenize(sentence)
    _tokens = [(token, "X") for token in tokens]
    x = TokenizeFeature().transform([_tokens])[0]
    tags = crf_model.predict(x)[0]

    output = []
    for tag, token in zip(tags, tokens):
        output.append([token, tag])
    return output
