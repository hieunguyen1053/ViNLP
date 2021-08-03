from ..datasets.ss_dataset import SSDataset
from ..features.ss_feature import SSFeature
from ..models.ss_crf import SS_CRF


def _get_tags(sents):
    tags = []
    for sent_idx, iob_tags in enumerate(sents):
        for i, tag in enumerate(iob_tags):
            if tag == 'O':
                continue
            curr_tag = {'type': None, 'word_idx': None, 'sent_idx': None}
            curr_tag['type'] = tag
            curr_tag['word_idx'] = i
            curr_tag['sent_idx'] = sent_idx
            tags.append(tuple(curr_tag.values()))
    tags = set(tags)
    return tags


def f_measure(y_true, y_pred):
    tags_true = _get_tags(y_true)
    tags_pred = _get_tags(y_pred)

    ne_ref = len(tags_true)
    ne_true = len(set(tags_true).intersection(tags_pred))
    ne_sys = len(tags_pred)
    if ne_ref == 0 or ne_true == 0 or ne_sys == 0:
        return 0
    p = ne_true / ne_sys
    r = ne_true / ne_ref
    f1 = (2 * p * r) / (p + r)

    return f1


test_set = SSDataset('ViNLP/data/sentence-segmentation/test.txt')

ss_features = SSFeature()
X_test, y_test = ss_features.transform(test_set.data)


model = SS_CRF.load("ViNLP/pipeline/bin/ss.crfsuite")
y_pred = model.predict(X_test)
print(f_measure(y_test, y_pred))
