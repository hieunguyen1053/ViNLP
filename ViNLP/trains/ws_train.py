from ..datasets.ws_dataset import WSDataset
from ..features.ws_feature import WSFeature
from ..models.ws_crf import WS_CRF

train_set = WSDataset('ViNLP/data/vlsp2013/ws/train.txt')
dev_set = WSDataset('ViNLP/data/vlsp2013/ws/test.txt')

ws_features = WSFeature()
X_train, y_train = ws_features.transform(train_set.data)
X_dev, y_dev = ws_features.transform(dev_set.data)

model = WS_CRF(
    c1=1.0,
    c2=1e-3,
    max_iterations=50,
    all_possible_states=True,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train, X_dev, y_dev)
model.save("ViNLP/pipeline/bin/ws.crfsuite")