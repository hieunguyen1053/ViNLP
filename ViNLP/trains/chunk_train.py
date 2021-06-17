from ..datasets.chunk_dataset import ChunkDataset
from ..features.chunk_feature import ChunkFeature
from ..models.chunk_crf import Chunk_CRF

train_set = ChunkDataset('ViNLP/data/vlsp2016/train.txt')
dev_set = ChunkDataset('ViNLP/data/vlsp2016/dev.txt')

postag_features = ChunkFeature()
X_train, y_train = postag_features.transform(train_set.data)
X_dev, y_dev = postag_features.transform(train_set.data)

model = Chunk_CRF(
    c1=1.0,
    c2=1e-3,
    max_iterations=100,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train, X_dev, y_dev)
model.save("ViNLP/pipelines/bin/chunk.crfsuite")