from os.path import join
from .corpus import Corpus

class WordTokenizeCorpus(Corpus):
    pass

def load_wordtokenize_corpus(data_folder, train_file=None, dev_file=None, test_file=None):
    train = __read_ws_data(join(data_folder, train_file)) if train_file else None
    dev = __read_ws_data(join(data_folder, dev_file)) if dev_file else None
    test = __read_ws_data(join(data_folder, test_file)) if test_file else None
    tagged_corpus = WordTokenizeCorpus(train, dev, test)
    return tagged_corpus

def __read_ws_data(data_file):
    sentences = []
    raw_sentences = open(data_file).read().strip().split("\n")
    for s in raw_sentences:
        sentence = []
        for item in s.split():
            tokens = item.split("_")
            tokens = [token for token in tokens if token != ""]
            for i, token in enumerate(tokens):
                sentence.append((token, "B-W" if i == 0 else "I-W"))
        sentences.append(sentence)
    return sentences