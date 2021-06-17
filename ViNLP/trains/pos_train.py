from ..datasets.pos_dataset import POSDataset
from ..features.pos_feature import POSFeature
from ..models.pos_crf import POS_CRF

train_set = POSDataset('ViNLP/data/vlsp2013/pos/train.txt')

postag_features = POSFeature()
X_train, y_train = postag_features.transform(train_set.data)

model = POS_CRF(
    c1=1.0,
    c2=1e-3,
    max_iterations=100,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train)
model.save("ViNLP/pipelines/bin/pos.crfsuite")