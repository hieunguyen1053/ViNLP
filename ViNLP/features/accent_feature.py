from .base_feature import BaseFeature
from string import punctuation

class AccentFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        features = {
            'bias': 1.0,
            '[0]': word,
            '[0].isdigit': word.isdigit(),
            '[0].ispunct': word in punctuation,
        }
        if i > 0:
            word1 = s[i - 1][0]
            features.update({
                '[-1]': word1,
                '[-1].isdigit': word1.isdigit(),
                '[-1].ispunct': word1 in punctuation,
            })
            if i > 1:
                word2 = s[i - 1][0]
                features.update({
                    '[-2]': word2,
                    '[-2].isdigit': word2.isdigit(),
                    '[-2].ispunct': word2 in punctuation,
                    '[-1,-2]': "%s %s" % (word1, word2),
                })
        if i < len(s) - 1:
            word1 = s[i + 1][0]
            features.update({
                '[+1]': word1,
                '[+1].isdigit': word1.isdigit(),
                '[+1].ispunct': word1 in punctuation,
            })
            if i < len(s) - 2:
                word2 = s[i + 2][0]
                features.update({
                    '[+2]': word2,
                    '[+2].isdigit': word2.isdigit(),
                    '[+2].ispunct': word2 in punctuation,
                    '[+1,+2]': "%s %s" % (word1, word2),
                })
        return features