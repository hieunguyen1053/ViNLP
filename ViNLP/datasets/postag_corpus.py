from .corpus import Corpus


class PostagCorpus(Corpus):
    def read_data(self, path):
        sentences = []
        raw_sentences = open(path).read().strip().split("\n\n")
        for s in raw_sentences:
            tagged_sentence = [node.split("/") if node != "/" else ["/", "/"] for node in s.split()]
            sentences.append(tagged_sentence)
        return sentences
