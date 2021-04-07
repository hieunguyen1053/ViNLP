from sklearn.metrics import f1_score

from ..datasets.postag_corpus import PostagCorpus
from ..models.crf_pos_tagger import CRFPosTagger
from ..features.postag_feature import PostagFeature
from ..utils import flatten

corpus = PostagCorpus()
corpus.load_corpus(data_folder="ViNLP/data", train_file="vi_train.pos", test_file="vi_test.pos")
train_data = corpus.train
test_data = corpus.test

postag_features = PostagFeature()
X_train, y_train = postag_features.transform(train_data)
X_test, y_test = postag_features.transform(test_data)

model = CRFPosTagger(
    c1=1.0,
    c2=1e-3,
    max_iterations=50,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train)
model.save("model.crfsuite")

# model = CRFPosTagger.load("ViNLP/pipelines/bin/pos_tag.crfsuite")
y_pred = model.predict(X_test)
print(f1_score(flatten(y_test), flatten(y_pred), average='micro'))
print(model.predict([X_test[0]]))
print(y_test[0])
print(test_data[0])