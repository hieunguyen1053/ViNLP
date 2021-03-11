from os.path import join

from .corpus import Corpus


class TaggedCorpus(Corpus):
    pass


def load_tagged_corpus(data_folder, train_file=None, dev_file=None, test_file=None):
    train = __read_tagged_data(join(data_folder, train_file)) if train_file else None
    dev = __read_tagged_data(join(data_folder, dev_file)) if dev_file else None
    test = __read_tagged_data(join(data_folder, test_file)) if test_file else None
    tagged_corpus = TaggedCorpus(train, dev, test)
    return tagged_corpus

def __read_tagged_data(data_file):
    sentences = []
    raw_sentences = open(data_file).read().strip().split("\n\n")
    for s in raw_sentences:
        tagged_sentence = [node.split("/") if node != "/" else ["/", "/"] for node in s.split()]
        sentences.append(tagged_sentence)
    return sentences
