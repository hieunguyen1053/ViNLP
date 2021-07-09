from ..datasets.chunk_dataset import ChunkDataset
from ..features.chunk_feature import ChunkFeature
from ..models.chunk_crf import Chunk_CRF

train_set = ChunkDataset('ViNLP/data/vlsp2016/train.txt')
dev_set = ChunkDataset('ViNLP/data/vlsp2016/dev.txt')

chunk_features = ChunkFeature()
X_train, y_train = chunk_features.transform(train_set.data)
X_dev, y_dev = chunk_features.transform(dev_set.data)

model = Chunk_CRF(
    c1=1.0,
    c2=1e-3,
    max_iterations=100,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train, X_dev, y_dev)
model.save("ViNLP/pipeline/bin/chunk.crfsuite")