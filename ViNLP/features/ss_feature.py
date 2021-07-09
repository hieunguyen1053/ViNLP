from string import punctuation

from .base_feature import BaseFeature


def is_punct(token):
    return token in punctuation

def has_punct(token):
    for punct in punctuation:
        if punct in token:
            return True
    return False


class SSFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        features = {
            'bias': 1.0,
            '[0]'           : word,
            '[0].lower'     : word.lower(),
            '[0].isdigit'   : word.isdigit(),
            '[0].istitle'   : word.istitle(),
            '[0].is_punct'  : is_punct(word),
            '[0].has_punct' : has_punct(word),
        }
        if i > 0:
            word1 = s[i - 1][0]
            features.update({
                '[-1]'           : word1,
                '[-1].lower'     : word1.lower(),
                '[-1].isdigit'   : word1.isdigit(),
                '[-1].istitle'   : word1.istitle(),
                '[-1].is_punct'  : is_punct(word1),
                '[-1].has_punct' : has_punct(word1),
                '[-1,0]'         : "%s_%s" % (word1, word),
            })

        if i < len(s) - 1:
            word1 = s[i + 1][0]
            features.update({
                '[+1]'             : word1,
                '[+1].lower'       : word1.lower(),
                '[+1].isdigit'     : word1.isdigit(),
                '[+1].istitle'     : word1.istitle(),
                '[+1].is_punct'    : is_punct(word1),
                '[+1].has_punct'   : has_punct(word1),
                '[0,+1]'           : "%s_%s" % (word, word1),
            })
        return features