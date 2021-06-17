from ..datasets.pos_dataset import POSDataset
from ..features.pos_feature import POSFeature
from ..models.pos_crf import POS_CRF


def _get_tags(sents):
    tags = []
    for sent_idx, iob_tags in enumerate(sents):
        curr_tag = {'type': None, 'word_idx': None, 'sent_idx': None}
        for i, tag in enumerate(iob_tags):
            if tag == 'X' and curr_tag['type']:
                tags.append(tuple(curr_tag.values()))
                curr_tag = {'type': None, 'word_idx': None, 'sent_idx': None}
            else:
                curr_tag['type'] = tag
                curr_tag['word_idx'] = i
                curr_tag['sent_idx'] = sent_idx
        if curr_tag['type']:
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


test_set = POSDataset('ViNLP/data/vlsp2013/pos/test.txt')

postag_features = POSFeature()
X_test, y_test = postag_features.transform(test_set.data)


model = POS_CRF.load("ViNLP/pipelines/bin/pos.crfsuite")
y_pred = model.predict(X_test)
print(f_measure(y_test, y_pred))
