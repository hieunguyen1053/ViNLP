from .base_feature import BaseFeature


class POSFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        features = {
            'bias'       : 1.0,
            '[0]'        : word,
            '[0].lower'  : word.lower(),
            '[0].istitle': word.istitle(),
        }
        if i > 0:
            word1 = s[i - 1][0]
            pos1  = s[i - 1][1]
            features.update({
                '[-1]'        : word1,
                '[-1].lower'  : word1.lower(),
                '[-1].istitle': word1.istitle(),
                '[-1].pos'    : pos1,
                '[-1,0]'      : "%s %s" % (word1, word)
            })
            if i > 1:
                word2 = s[i - 2][0]
                pos2  = s[i - 2][1]
                features.update({
                    '[-2]': word2,
                    '[-2].lower'  : word2.lower(),
                    '[-2].istitle': word2.istitle(),
                    '[-2].pos'    : pos2,
                    '[-2,-1]'     : "%s %s" % (word2, word1),
                    '[-2,-1].pos' : "%s %s" % (pos2, pos1)
                })
        else:
            features['BOS'] = True

        if i < len(s) - 1:
            word1 = s[i + 1][0]
            features.update({
                '[+1]'        : word1,
                '[+1].lower'  : word1.lower(),
                '[+1].istitle': word1.istitle(),
                '[0,+1]'      : "%s %s" % (word, word1)
            })
            if i < len(s) - 2:
                word2 = s[i + 2][0]
                features.update({
                    '[+2]'        : word2,
                    '[+2].lower'  : word2.lower(),
                    '[+2].istitle': word2.istitle(),
                    '[+1,+2]'     : "%s %s" % (word1, word2)
                })
        else:
            features['EOS'] = True
        return features
