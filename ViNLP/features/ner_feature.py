from .base_feature import BaseFeature


class NERFeature(BaseFeature):
    def word2features(self, s, i):
        word   = s[i][0]
        pos    = s[i][1]
        chunk  = s[i][2]
        features = {
            'bias'       : 1.0,
            '[0]'        : word,
            '[0].lower'  : word.lower(),
            '[0].istitle': word.istitle(),
            '[0].pos'    : pos,
            '[0].chunk'  : chunk
        }
        if i > 0:
            word1  = s[i - 1][0]
            pos1   = s[i - 1][1]
            chunk1 = s[i - 1][2]
            ner1   = s[i - 1][3]
            features.update({
                '[-1]'        : word1,
                '[-1].lower'  : word1.lower(),
                '[-1].istitle': word1.istitle(),
                '[-1].pos'    : pos1,
                '[-1].chunk'  : chunk1,
                '[-1].ner'    : ner1,
                '[-1,0]'      : "%s %s" % (word1, word),
                '[-1,0].pos'  : "%s %s" % (pos1, pos),
                '[-1,0].chunk': "%s %s" % (chunk1, chunk),
            })
            if i > 1:
                word2  = s[i - 2][0]
                pos2   = s[i - 2][1]
                chunk2 = s[i - 2][2]
                ner2   = s[i - 2][3]
                features.update({
                    '[-2]': word2,
                    '[-2].lower'   : word2.lower(),
                    '[-2].istitle' : word2.istitle(),
                    '[-2].pos'     : pos2,
                    '[-2].chunk'   : chunk2,
                    '[-2].ner'     : ner2,
                    '[-2,-1]'      : "%s %s" % (word2, word1),
                    '[-2,-1].pos'  : "%s %s" % (pos2, pos1),
                    '[-2,-1].chunk': "%s %s" % (chunk2, chunk1),
                    '[-2,-1].ner'  : "%s %s" % (ner2, ner1),
                })
        else:
            features['BOS'] = True

        if i < len(s) - 1:
            word1  = s[i + 1][0]
            pos1   = s[i + 1][1]
            chunk1 = s[i + 1][2]
            features.update({
                '[+1]'        : word1,
                '[+1].lower'  : word1.lower(),
                '[+1].istitle': word1.istitle(),
                '[+1].pos'    : pos1,
                '[+1].chunk'  : chunk1,
                '[0,+1]'      : "%s %s" % (word, word1),
                '[0,+1].pos'  : "%s %s" % (pos, pos1),
                '[0,+1].chunk': "%s %s" % (chunk, chunk1),
            })
            if i < len(s) - 2:
                word2  = s[i + 2][0]
                pos2   = s[i + 2][1]
                chunk2 = s[i + 2][2]
                features.update({
                    '[+2]'         : word2,
                    '[+2].lower'   : word2.lower(),
                    '[+2].istitle' : word2.istitle(),
                    '[+2].pos'     : pos2,
                    '[+2].chunk'   : chunk2,
                    '[+1,+2]'      : "%s %s" % (word1, word2),
                    '[+1,+2].pos'  : "%s %s" % (pos1, pos2),
                    '[+1,+2].chunk': "%s %s" % (chunk1, chunk2),
                })
        else:
            features['EOS'] = True
        return features
