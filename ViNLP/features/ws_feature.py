from os import path

from ..datasets.dictionary import Dictionary
from .base_feature import BaseFeature

words = Dictionary(path.join(path.dirname(__file__), "..", "data", "Viet74K.txt")).words
lower_words = set([word.lower() for word in words])


def is_in_dict(word):
    return word.lower() in lower_words


class WSFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        features = {
            'bias': 1.0,
            '[0]'           : word,
            '[0].lower'     : word.lower(),
            '[0].isdigit'   : word.isdigit(),
            '[0].istitle'   : word.istitle(),
            '[0].is_in_dict': is_in_dict(word),
        }
        if i > 0:
            word1 = s[i - 1][0]
            features.update({
                '[-1]'             : word1,
                '[-1].lower'       : word1.lower(),
                '[-1].isdigit'     : word1.isdigit(),
                '[-1].istitle'     : word1.istitle(),
                '[-1].is_in_dict'  : is_in_dict(word1),
                '[-1,0]'           : "%s %s" % (word1, word),
                '[-1:0].is_in_dict': is_in_dict("%s %s" % (word1, word)),
            })
            if i > 1:
                word2 = s[i - 2][0]
                features.update({
                    '[-2]'              : word2,
                    '[-2].lower'        : word2.lower(),
                    '[-2].isdigit'      : word2.isdigit(),
                    '[-2].istitle'      : word2.istitle(),
                    '[-2].is_in_dict'   : is_in_dict(word2),
                    '[-2,-1]'           : "%s %s" % (word2, word1),
                    '[-2,-1].istitle'   : ("%s %s" % (word2, word1)).istitle(),
                    '[-2,-1].is_in_dict': is_in_dict("%s %s" % (word2, word1)),
                    '[-2,0]'            : "%s %s %s" % (word2, word1, word),
                    '[-2,0].istitle'    : ("%s %s %s" % (word2, word1, word)).istitle(),
                    '[-2,0].is_in_dict' : is_in_dict("%s %s %s" % (word2, word1, word)),
                })
        else:
            features['BOS'] = True

        if i < len(s) - 1:
            word1 = s[i + 1][0]
            features.update({
                '[+1]'             : word1,
                '[+1].lower'       : word1.lower(),
                '[+1].isdigit'     : word1.isdigit(),
                '[+1].istitle'     : word1.istitle(),
                '[+1].is_in_dict'  : is_in_dict(word1),
                '[0,+1]'           : "%s %s" % (word, word1),
                '[0,+1].istitle'   : ("%s %s" % (word, word1)).istitle(),
                '[0,+1].is_in_dict': is_in_dict("%s %s" % (word, word1)),
            })
            if i < len(s) - 2:
                word2 = s[i + 2][0]
                features.update({
                    '[+2]'              : word2,
                    '[+2].lower'        : word2.lower(),
                    '[+2].isdigit'      : word2.isdigit(),
                    '[+2].istitle'      : word2.istitle(),
                    '[+2].is_in_dict'   : is_in_dict(word2),
                    '[+1,+2]'           : "%s %s" % (word1, word2),
                    '[+1,+2].istitle'   : ("%s %s" % (word1, word2)).istitle(),
                    '[+1,+2].is_in_dict': is_in_dict("%s %s" % (word1, word2)),
                    '[0,+2]'            : "%s %s %s" % (word, word1, word2),
                    '[0,+2].istitle'    : ("%s %s %s" % (word, word1, word2)).istitle(),
                    '[0,+2].is_in_dict' : is_in_dict("%s %s %s" % (word, word1, word2)),
                })
        else:
            features['EOS'] = True

        if 0 < i < len(s) - 1:
            wordn1 = s[i - 1][0]
            wordp1 = s[i + 1][0]
            features.update({
                '[-1,+1]'           : "%s %s %s" % (wordn1, word, wordp1),
                '[-1,+1].istitle'   : ("%s %s %s" % (wordn1, word, wordp1)).istitle(),
                '[-1,+1].is_in_dict': is_in_dict("%s %s %s" % (wordn1, word, wordp1)),
            })
        return features
