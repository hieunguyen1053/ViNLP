# https://github.com/flairNLP/flair/blob/master/flair/data.py#L1049


class Corpus:
    def __init__(self, train=None, dev=None, test=None, name: str = "corpus"):
        self.name: str = name

        self._train = train
        self._dev = dev
        self._test = test

    @property
    def train(self):
        return self._train

    @property
    def dev(self):
        return self._dev

    @property
    def test(self):
        return self._test

    def downsample(self, percentage: float = 0.1, downsample_train=True, downsample_dev=True, downsample_test=True):
        if downsample_train:
            n = int(len(self.train) * percentage)
            self._train = self.train[:n]
        if downsample_dev:
            n = int(len(self.dev) * percentage)
            self._dev = self.dev[:n]
        if downsample_test:
            n = int(len(self.test) * percentage)
            self._test = self.test[:n]
