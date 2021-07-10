from os import path

from ..datasets.dictionary import Dictionary
from .base_feature import BaseFeature

words = Dictionary(path.join(path.dirname(__file__), "..", "data", "Viet74K.txt")).words
lower_words = set([word.lower() for word in words])

viwords = Dictionary(path.join(path.dirname(__file__), "..", "data", "all-vietnamese-syllables.txt")).words
lower_viwords = set([word.lower() for word in viwords])


def is_in_dict(word):
    return word.lower() in lower_words

def is_vi_word(word):
    return word.lower() in lower_viwords


class WSFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        features = {
            'bias': 1.0,
            '[0]'           : word,
            '[0].lower'     : word.lower(),
            '[0].isdigit'   : word.isdigit(),
            '[0].istitle'   : word.istitle(),
            '[0].is_vi_word': is_vi_word(word),
            '[0].is_in_dict': is_in_dict(word),
        }
        if i > 0:
            word1 = s[i - 1][0]
            features.update({
                '[-1]'             : word1,
                '[-1].lower'       : word1.lower(),
                '[-1].isdigit'     : word1.isdigit(),
                '[-1].istitle'     : word1.istitle(),
                '[-1].is_vi_word'  : is_vi_word(word1),
                '[-1].is_in_dict'  : is_in_dict(word1),
                '[-1,0]'           : "%s_%s" % (word1, word),
            })
            if i > 1:
                word2 = s[i - 2][0]
                features.update({
                    '[-2]'              : word2,
                    '[-2].lower'        : word2.lower(),
                    '[-2].isdigit'      : word2.isdigit(),
                    '[-2].istitle'      : word2.istitle(),
                    '[-2].is_in_dict'   : is_in_dict(word2),
                    '[-2].is_vi_word'   : is_vi_word(word2),
                    '[-2,-1]'           : "%s_%s" % (word2, word1),
                    '[-2,-1].istitle'   : word2.istitle() and word1.istitle(),
                    '[-2,0]'            : "%s_%s_%s" % (word2, word1, word),
                    '[-2,0].istitle'    : word2.istitle() and word1.istitle() and word.istitle(),
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
                '[+1].is_vi_word'  : is_vi_word(word1),
                '[+1].is_in_dict'  : is_in_dict(word1),
                '[0,+1]'           : "%s_%s" % (word, word1),
                '[0,+1].istitle'   : word.istitle() and word1.istitle(),
            })
            if i < len(s) - 2:
                word2 = s[i + 2][0]
                features.update({
                    '[+2]'              : word2,
                    '[+2].lower'        : word2.lower(),
                    '[+2].isdigit'      : word2.isdigit(),
                    '[+2].istitle'      : word2.istitle(),
                    '[+2].is_vi_word'   : is_vi_word(word2),
                    '[+2].is_in_dict'   : is_in_dict(word2),
                    '[+1,+2]'           : "%s_%s" % (word1, word2),
                    '[+1,+2].istitle'   : word1.istitle() and word2.istitle(),
                    '[0,+2]'            : "%s_%s_%s" % (word, word1, word2),
                    '[0,+2].istitle'    : word.istitle() and word1.istitle() and word2.istitle(),
                })
        else:
            features['EOS'] = True

        if 0 < i < len(s) - 1:
            wordn1 = s[i - 1][0]
            wordp1 = s[i + 1][0]
            features.update({
                '[-1,+1]'           : "%s_%s_%s" % (wordn1, word, wordp1),
                '[-1,+1].istitle'   : wordn1.istitle() and word.istitle() and wordp1.istitle(),
                '[-1,+1].is_in_dict': is_in_dict("%s_%s_%s" % (wordn1, word, wordp1)),
            })
        return features
