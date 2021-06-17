from os import path

from ..features.chunk_feature import ChunkFeature
from ..models.chunk_crf import Chunk_CRF
from .pos_tag import pos_tag

crf_model = Chunk_CRF.load(path.join(path.dirname(__file__), "bin", "chunk.crfsuite"))


def chunk(sentence):
    global crf_model
    tokens = pos_tag(sentence)
    _tokens = [(token[0], token[1], "X") for token in tokens]
    x = ChunkFeature().transform([_tokens])[0]
    tags = crf_model.predict(x)[0]

    output = []
    for tag, token in zip(tags, tokens):
        output.append((token[0], token[1], tag))
    return output
