from os.path import join
from .corpus import Corpus

class AccentCorpus(Corpus):
    pass

def load_accent_corpus(data_folder, train_file=None, dev_file=None, test_file=None):
    train = __read_accent_data(join(data_folder, train_file)) if train_file else None
    dev = __read_accent_data(join(data_folder, dev_file)) if dev_file else None
    test = __read_accent_data(join(data_folder, test_file)) if test_file else None
    tagged_corpus = AccentCorpus(train, dev, test)
    return tagged_corpus

def __read_accent_data(data_file):
    sentences = []
    content = open(data_file).read().strip().split("\n\n")
    for pair in content:
        line1, line2 = pair.split("\n")
        line1 = line1.split()
        line2 = line2.split()
        sentence = [[token, label.replace("_", "")] for (token, label) in zip(line1, line2)]
        sentences.append(sentence)
    return sentences
