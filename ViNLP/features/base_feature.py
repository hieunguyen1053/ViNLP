from abc import ABC, abstractmethod


class BaseFeature(ABC):
    def transform(self, sents):
        X = [self.sentence2features(sent) for sent in sents]
        y = [self.sentence2labels(sent) for sent in sents]
        return X, y

    def sentence2features(self, sent):
        return [self.word2features(sent, i) for i in range(len(sent))]

    def sentence2labels(self, sent):
        return [row[-1] for row in sent]

    @abstractmethod
    def word2features(self, s, i):
        raise NotImplementedError
