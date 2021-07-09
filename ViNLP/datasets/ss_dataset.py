from .base_dataset import BaseDataset


class SSDataset(BaseDataset):
    def __init__(self, filepath):
        super(SSDataset, self).__init__()
        self.data = self.read_file(filepath)

    def read_file(self, filepath):
        data = []
        raw = open(filepath, 'r', encoding='utf8').read()
        sents = raw.split('\n\n')
        for sent in sents:
            _sent = []
            items = sent.split('\n')
            for item in items:
                word, tag = item.split('\t')
                _sent.append((word, tag))
            data.append(_sent)
        return data
