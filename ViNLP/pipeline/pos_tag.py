from os.path import join

from ViNLP.features import TokenizeFeature
from ViNLP.models import CRFPosTagger

from .word_tokenize import word_tokenize


def pos_tag(sentence, format=None):
    crf_model = CRFPosTagger.load(join("pipeline", "bin", "pos_tag.crfsuite"))

    tokens = word_tokenize(sentence)
    _tokens = [(token, "X") for token in tokens]
    x = TokenizeFeature().transform([_tokens])[0]
    tags = crf_model.predict(x)[0]

    output = []
    for tag, token in zip(tags, tokens):
        output.append([token, tag])
    return output
