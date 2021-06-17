from .base_dataset import BaseDataset

class ChunkDataset(BaseDataset):
    def __init__(self, filepath):
        super(ChunkDataset, self).__init__()
        self.data = self.read_file(filepath)

    def read_file(self, filepath):
        data = []
        raw = open(filepath, 'r', encoding='utf8').read()
        sents = raw.split('\n\n')
        for sent in sents:
            _sent = []
            items = sent.split('\n')
            for item in items:
                word, pos, chunk, _ = item.split('\t')
                word = '_'.join(word.split())
                _sent.append((word, pos, chunk))
            data.append(_sent)
        return data
