from os.path import dirname, join

from ViNLP.corpus import Dictionary

from .base_feature import BaseFeature

words = Dictionary(join(dirname(__file__), "..", "data", "Viet74K.txt")).words
lower_words = set([word.lower() for word in words])

def is_in_dict(word):
    return str(word.lower() in lower_words)

class TokenizeFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        features = {
            'bias': 1.0,
            'T[0]': word,
            'T[0].lower': word.lower(),
            'T[0].isdigit': word.isdigit(),
            'T[0].istitle': word.istitle(),
            'T[0].is_in_dict': is_in_dict(word),
        }
        if i > 0:
            word1 = s[i - 1][0]
            features.update({
                'T[-1]': word1,
                'T[-1].lower': word1.lower(),
                'T[-1].isdigit': word1.isdigit(),
                'T[-1].istitle': word1.istitle(),
                'T[-1].is_in_dict': is_in_dict(word1),
                'T[-1,0]': "%s %s" % (word1, word),
                'T[-1:0].is_in_dict': is_in_dict("%s %s" % (word1, word)),
            })
            if i > 1:
                word2 = s[i - 2][0]
                features.update({
                    'T[-2]': word2,
                    'T[-2].lower': word2.lower(),
                    'T[-2].is_in_dict': is_in_dict(word2),
                    'T[-2,-1]': "%s %s" % (word2, word1),
                    'T[-2,-1].is_in_dict': is_in_dict("%s %s" % (word2, word1)),
                    'T[-2,0]': "%s %s %s" % (word2, word1, word),
                    'T[-2,0].is_in_dict': is_in_dict("%s %s %s" % (word2, word1, word)),
                })
        else:
            features['BOS'] = True

        if i < len(s) - 1:
            word1 = s[i + 1][0]
            features.update({
                'T[+1]': word1,
                'T[+1].lower': word1.lower(),
                'T[+1].isdigit': word1.isdigit(),
                'T[+1].istitle': word1.istitle(),
                'T[+1].is_in_dict': is_in_dict(word1),
                'T[0,+1]': "%s %s" % (word, word1),
                'T[0,+1].is_in_dict': is_in_dict("%s %s" % (word, word1)),
                'T[0,+1].istitle': ("%s %s" % (word, word1)).istitle(),
            })
            if i < len(s) - 2:
                word2 = s[i + 2][0]
                features.update({
                    'T[+2]': word2,
                    'T[+2].lower': word2.lower(),
                    'T[+2].is_in_dict': is_in_dict(word2),
                    'T[+1,+2]': "%s %s" % (word1, word2),
                    'T[+1,+2].is_in_dict': is_in_dict("%s %s" % (word1, word2)),
                    'T[0,+2]': "%s %s %s" % (word, word1, word2),
                    'T[0,+2].istitle': ("%s %s %s" % (word, word1, word2)).istitle(),
                    'T[0,+2].is_in_dict': is_in_dict("%s %s %s" % (word, word1, word2)),
                })
        else:
            features['EOS'] = True

        if 0 < i < len(s) - 1:
            wordn1 = s[i - 1][0]
            wordp1 = s[i + 1][0]
            features.update({
                'T[-1,+1]': "%s %s %s" % (wordn1, word, wordp1),
                'T[-1,+1].is_in_dict': is_in_dict("%s %s %s" % (wordn1, word, wordp1)),
            })
        return features
