from abc import ABC, abstractmethod

class BaseFeature(ABC):
    def transform(self, sentences):
        X = [self.sentence2features(s) for s in sentences]
        y = [self.sentence2labels(s) for s in sentences]
        return X, y

    def sentence2features(self, s):
        return [self.word2features(s, i) for i in range(len(s))]

    def sentence2labels(self, s):
        return [row[-1] for row in s]

    @abstractmethod
    def word2features(self, s, i):
        pass