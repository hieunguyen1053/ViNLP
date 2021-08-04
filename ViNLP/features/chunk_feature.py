from .base_feature import BaseFeature


class ChunkFeature(BaseFeature):
    def word2features(self, s, i):
        word = s[i][0]
        pos  = s[i][1]
        features = {
            'bias'       : 1.0,
            '[0]'        : word,
            '[0].lower'  : word.lower(),
            '[0].istitle': all(w.istitle() for w in word.split('_')),
            '[0].pos'    : pos,
        }
        if i > 0:
            word1  = s[i - 1][0]
            pos1   = s[i - 1][1]
            chunk1 = s[i - 1][2]
            features.update({
                '[-1]'        : word1,
                '[-1].lower'  : word1.lower(),
                '[-1].istitle': all(w.istitle() for w in word1.split('_')),
                '[-1].pos'    : pos1,
                '[-1].chunk'  : chunk1,
                '[-1,0]'      : "%s %s" % (word1, word),
                '[-1,0].pos'  : "%s %s" % (pos1, pos),
            })
            if i > 1:
                word2  = s[i - 2][0]
                pos2   = s[i - 2][1]
                chunk2 = s[i - 2][2]
                features.update({
                    '[-2]': word2,
                    '[-2].lower'   : word2.lower(),
                    '[-2].istitle' : all(w.istitle() for w in word2.split('_')),
                    '[-2].pos'     : pos2,
                    '[-2].chunk'   : chunk2,
                    '[-2,-1]'      : "%s %s" % (word2, word1),
                    '[-2,-1].pos'  : "%s %s" % (pos2, pos1),
                    '[-2,-1].chunk': "%s %s" % (chunk2, chunk1)
                })
                if i > 2:
                    chunk3 = s[i - 3][2]
                    features.update({
                        '[-3].chunk': chunk3,
                        '[-3,-2].chunk': "%s %s" % (chunk3, chunk2)
                    })
                else:
                    features['[-3].BOS'] = True
            else:
                features['[-2].BOS'] = True
        else:
            features['[1-].BOS'] = True

        if i < len(s) - 1:
            word1 = s[i + 1][0]
            pos1  = s[i + 1][1]
            features.update({
                '[+1]'        : word1,
                '[+1].lower'  : word1.lower(),
                '[+1].istitle': all(w.istitle() for w in word1.split('_')),
                '[+1].pos'    : pos1,
                '[0,+1]'      : "%s %s" % (word, word1),
                '[0,+1].pos'  : "%s %s" % (pos, pos1),
            })
            if i < len(s) - 2:
                word2 = s[i + 2][0]
                pos2  = s[i + 2][1]
                features.update({
                    '[+2]'        : word2,
                    '[+2].lower'  : word2.lower(),
                    '[+2].istitle': all(w.istitle() for w in word2.split('_')),
                    '[+2].pos'    : pos2,
                    '[+1,+2]'     : "%s %s" % (word1, word2),
                    '[+1,+2].pos' : "%s %s" % (pos1, pos2),
                })
            else:
                features['[+2].EOS'] = True
        else:
            features['[+1].EOS'] = True
        return features
