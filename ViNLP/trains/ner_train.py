from ..datasets.ner_dataset import NERDataset
from ..features.ner_feature import NERFeature
from ..models.ner_crf import NER_CRF

train_set = NERDataset('ViNLP/data/vlsp2016/train.txt')
dev_set = NERDataset('ViNLP/data/vlsp2016/dev.txt')

postag_features = NERFeature()
X_train, y_train = postag_features.transform(train_set.data)
X_dev, y_dev = postag_features.transform(dev_set.data)

model = NER_CRF(
    c1=1.0,
    c2=1e-3,
    max_iterations=100,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train, X_dev, y_dev)
model.save("ViNLP/pipeline/bin/ner.crfsuite")