from .corpus import Corpus

class WordTokenizeCorpus(Corpus):
    def read_data(self, path):
        sentences = []
        raw_sentences = open(path).read().strip().split("\n")
        for s in raw_sentences:
            sentence = []
            for item in s.split():
                tokens = item.split("_")
                tokens = [token for token in tokens if token != ""]
                for i, token in enumerate(tokens):
                    sentence.append((token, "B-W" if i == 0 else "I-W"))
            sentences.append(sentence)
        return sentences