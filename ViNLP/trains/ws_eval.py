from ..datasets.ws_dataset import WSDataset
from ..features.ws_feature import WSFeature
from ..models.ws_crf import WS_CRF


def _get_tags(sents):
    tags = []
    for sent_idx, iob_tags in enumerate(sents):
        curr_tag = {'type': None, 'start_idx': None,
                'end_idx': None, 'sent_idx': None}
        for i, tag in enumerate(iob_tags):
            if tag.startswith('B') and curr_tag['type']:
                tags.append(tuple(curr_tag.values()))
                curr_tag = {'type': None, 'start_idx': None,
                            'end_idx': None, 'sent_idx': None}
            if tag.startswith('B'):
                curr_tag['type'] = tag[2:]
                curr_tag['start_idx'] = i
                curr_tag['end_idx'] = i
                curr_tag['sent_idx'] = sent_idx
            elif tag.startswith('I'):
                curr_tag['end_idx'] = i
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


test_set = WSDataset('ViNLP/data/vlsp2013/ws/test.txt')

postag_features = WSFeature()
X_test, y_test = postag_features.transform(test_set.data)


model = WS_CRF.load("ViNLP/pipeline/bin/ws.crfsuite")
y_pred = model.predict(X_test)
print(f_measure(y_test, y_pred))
