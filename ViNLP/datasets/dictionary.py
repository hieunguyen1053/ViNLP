from ..utils.file_io import read

class Dictionary:
    def __init__(self, filepath):
        self.filepath = filepath
        self.words_data = None

    @property
    def words(self):
        if not self.words_data:
            content = read(self.filepath).strip()
            words = content.split('\n')
            self.words_data = words
        return self.words_data
