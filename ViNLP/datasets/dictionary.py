from ..utils.file_io import read


class Dictionary:
    def __init__(self, filepath):
        self.filepath = filepath
        self._words = None

    @property
    def words(self):
        if not self._words:
            content = read(self.filepath).strip()
            words = content.split('\n')
            words = map(lambda x: '_'.join(x.split()), words)
            self._words = list(words)
        return self._words
