from os.path import dirname, join

from ViNLP.corpus import Dictionary

from .base_feature import BaseFeature

words = Dictionary(join(dirname(__file__), "..", "data", "Viet74K.txt")).words
lower_words = set([word.lower() for word in words])


class TaggedFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        features = {
            'bias': 1.0,
            'T[0].lower': word.lower(),
            'T[0].istitle': word.istitle(),
            'T[0]': word,
        }
        if i > 0:
            word1 = s[i - 1][0]
            tag1 = s[i - 1][1]
            features.update({
                'T[-1].lower': word1.lower(),
                'T[-1].istitle': word1.istitle(),
                'T[-1]': word1,
                'T[-1][1]': tag1,
                'T[-1,0]': "%s %s" % (word1, word)
            })
            if i > 1:
                word2 = s[i - 2][0]
                tag2 = s[i - 2][1]
                features.update({
                    'T[-2].lower': word2.lower(),
                    'T[-2].istitle': word2.istitle(),
                    'T[-2]': word2,
                    'T[-2,-1]': "%s %s" % (word2, word1),
                    'T[-2][1]': tag2,
                    'T[-2,-1][1]': "%s %s" % (tag2, tag1)
                })
                if i > 2:
                    tag3 = s[i - 3][1]
                    features.update({
                        'T[-3][1]': tag3,
                        'T[-3,-2][1]': "%s %s" % (tag3, tag2)
                    })
        else:
            features['BOS'] = True

        if i < len(s) - 1:
            word1 = s[i + 1][0]
            features.update({
                'T[+1].lower': word1.lower(),
                'T[+1].istitle': word1.istitle(),
                'T[+1]': word1,
                'T[0,+1]': "%s %s" % (word, word1)
            })
            if i < len(s) - 2:
                word2 = s[i + 2][0]
                features.update({
                    'T[+2].lower': word2.lower(),
                    'T[+2].istitle': word2.istitle(),
                    'T[+2]': word2,
                    'T[+1,+2]': "%s %s" % (word1, word2)
                })
        else:
            features['EOS'] = True
        return features
