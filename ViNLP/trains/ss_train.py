from ..datasets.ss_dataset import SSDataset
from ..features.ss_feature import SSFeature
from ..models.ss_crf import SS_CRF

train_set = SSDataset('ViNLP/data/sentence-segmentation/train.txt')
dev_set = SSDataset('ViNLP/data/sentence-segmentation/dev.txt')

ss_feature = SSFeature()
X_train, y_train = ss_feature.transform(train_set.data)
X_dev, y_dev = ss_feature.transform(dev_set.data)

model = SS_CRF(
    c1=1.0,
    c2=1e-3,
    max_iterations=100,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train, X_dev, y_dev)
model.save("ViNLP/pipeline/bin/ss.crfsuite")