from os import path
from string import punctuation

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

def is_punct(word):
    return all([char in punctuation for char in word])

def is_number(word):
    try:
        float(word)
        return True
    except ValueError:
        return False


class WSFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        features = {
            'bias'          : 1.0,
            '[0]'           : word,
            '[0].lower'     : word.lower(),
            '[0].istitle'   : word.istitle(),
            '[0].is_punct'  : is_punct(word),
            '[0].is_number' : is_number(word),
            '[0].is_vi_word': is_vi_word(word.lower()),
            '[0].is_in_dict': is_in_dict(word.lower()),
        }
        if i > 0:
            word1 = s[i - 1][0]
            features.update({
                '[-1]'             : word1,
                '[-1].lower'       : word1.lower(),
                '[-1].istitle'     : word1.istitle(),
                '[-1].is_punct'    : is_punct(word1),
                '[-1].is_number'   : is_number(word1),
                '[-1].is_vi_word'  : is_vi_word(word1.lower()),
                '[-1].is_in_dict'  : is_in_dict(word1.lower()),
                '[-1,0]'           : "%s %s" % (word1, word),
                '[-1,0].is_in_dict': is_in_dict(("%s %s" % (word1, word)).lower()),
            })
            if i > 1:
                word2 = s[i - 2][0]
                features.update({
                    '[-2]'              : word2,
                    '[-2].lower'        : word2.lower(),
                    '[-2].istitle'      : word2.istitle(),
                    '[-2].is_punct'     : is_punct(word2),
                    '[-2].is_number'    : is_number(word2),
                    '[-2].is_in_dict'   : is_in_dict(word2.lower()),
                    '[-2].is_vi_word'   : is_vi_word(word2.lower()),
                    '[-2,-1]'           : "%s %s" % (word2, word1),
                    '[-2,-1].is_in_dict': is_in_dict(("%s %s" % (word2, word1)).lower()),
                    '[-2,0]'            : "%s %s %s" % (word2, word1, word),
                    '[-2,0].is_in_dict' : is_in_dict(("%s %s %s" % (word2, word1, word)).lower()),
                })
            else:
                features['[-2].BOS'] = True
        else:
            features['[-1].BOS'] = True

        if i < len(s) - 1:
            word1 = s[i + 1][0]
            features.update({
                '[+1]'             : word1,
                '[+1].lower'       : word1.lower(),
                '[+1].istitle'     : word1.istitle(),
                '[+1].is_punct'    : is_punct(word1),
                '[+1].is_number'   : is_number(word1),
                '[+1].is_vi_word'  : is_vi_word(word1.lower()),
                '[+1].is_in_dict'  : is_in_dict(word1.lower()),
                '[0,+1]'           : "%s %s" % (word, word1),
                '[0,+1].istitle'   : word.istitle() and word1.istitle(),
                '[0,+1].is_in_dict': is_in_dict(("%s %s" % (word, word1)).lower()),
            })
            if i < len(s) - 2:
                word2 = s[i + 2][0]
                features.update({
                    '[+2]'              : word2,
                    '[+2].lower'        : word2.lower(),
                    '[+2].istitle'      : word2.istitle(),
                    '[+2].is_punct'     : is_punct(word2),
                    '[+2].is_number'    : is_number(word2),
                    '[+2].is_vi_word'   : is_vi_word(word2.lower()),
                    '[+2].is_in_dict'   : is_in_dict(word2.lower()),
                    '[+1,+2]'           : "%s %s" % (word1, word2),
                    '[+1,+2].is_in_dict': is_in_dict(("%s %s" % (word1, word2)).lower()),
                    '[0,+2]'            : "%s %s %s" % (word, word1, word2),
                    '[0,+2].istitle'    : word.istitle() and word1.istitle() and word2.istitle(),
                    '[0,+2].is_in_dict' : is_in_dict(("%s %s %s" % (word, word1, word2)).lower()),
                })
            else:
                features['[+2].EOS'] = True
        else:
            features['[+1].EOS'] = True

        if 0 < i < len(s) - 1:
            wordn1 = s[i - 1][0]
            wordp1 = s[i + 1][0]
            features.update({
                '[-1,+1]'           : "%s %s %s" % (wordn1, word, wordp1),
                '[-1,+1].is_in_dict': is_in_dict(("%s %s %s" % (wordn1, word, wordp1)).lower()),
            })
        return features