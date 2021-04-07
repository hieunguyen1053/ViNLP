# https://github.com/flairNLP/flair/blob/master/flair/data.py#L1049
from abc import ABC, abstractmethod
from os import path
from typing import List, Optional, Union

from .dataset import Dataset


class Corpus:
    def __init__(
        self,
        train: Union[Dataset, List, None] = None,
        dev: Union[Dataset, List, None] = None,
        test: Union[Dataset, List, None] = None,
        name: str = "corpus"
    ):
        self.name: str = name
        if not isinstance(train, Dataset):
            train = Dataset(train)
        if not isinstance(dev, Dataset):
            dev = Dataset(dev)
        if not isinstance(test, Dataset):
            test = Dataset(test)
        self._train: Optional[Dataset] = train
        self._dev: Optional[Dataset] = dev
        self._test: Optional[Dataset] = test

    @property
    def train(self):
        return self._train

    @property
    def dev(self):
        return self._dev

    @property
    def test(self):
        return self._test

    def load_corpus(self, data_folder: str, train_file: Optional[str] = None, dev_file: Optional[str] = None, test_file: Optional[str] = None):
        train = self.read_data(
            path.join(data_folder, train_file)) if train_file else None
        dev = self.read_data(
            path.join(data_folder, dev_file)) if dev_file else None
        test = self.read_data(
            path.join(data_folder, test_file)) if test_file else None

        self._train = Dataset(train)
        self._dev = Dataset(dev)
        self._test = Dataset(test)

    @abstractmethod
    def read_data(self, path: str):
        pass

    def downsample(
        self,
        percentage: float = 0.1,
        downsample_train: bool = True,
        downsample_dev: bool = True,
        downsample_test: bool = True
    ):
        if downsample_train and self.train is not None:
            n = int(len(self.train) * percentage)
            self._train = self.train[:n]
        if downsample_dev and self.dev is not None:
            n = int(len(self.dev) * percentage)
            self._dev = self.dev[:n]
        if downsample_test and self.test is not None:
            n = int(len(self.test) * percentage)
            self._test = self.test[:n]
