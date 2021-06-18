from ..datasets.ws_dataset import WSDataset
from ..features.ws_feature import WSFeature
from ..models.ws_crf import WS_CRF

train_set = WSDataset('ViNLP/data/vlsp2013/ws/train.txt')

postag_features = WSFeature()
X_train, y_train = postag_features.transform(train_set.data)

model = WS_CRF(
    c1=1.0,
    c2=1e-3,
    max_iterations=100,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train)
model.save("ViNLP/pipeline/bin/ws.crfsuite")