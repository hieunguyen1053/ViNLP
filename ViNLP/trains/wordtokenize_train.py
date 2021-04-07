from sklearn.metrics import f1_score

from ..datasets.wordtokenize_corpus import WordTokenizeCorpus
from ..models.crf_word_tokenizer import CRFTokenizer
from ..features.tokenize_feature import TokenizeFeature
from ..utils import flatten

corpus = WordTokenizeCorpus()
corpus.load_corpus(data_folder="ViNLP/data", train_file="vi_train.wt", test_file="vi_test.wt")
train_data = corpus.train
test_data = corpus.test

token_features = TokenizeFeature()
X_train, y_train = token_features.transform(train_data)
X_test, y_test = token_features.transform(test_data)

model = CRFTokenizer(
    c1=1.0,
    c2=1e-3,
    max_iterations=100,
    all_possible_transitions=True,
    verbose=True,
)

model.fit(X_train, y_train)
model.save("/Users/hieunguyen/Desktop/ViNLP/ViNLP/pipeline/bin/tokenize.crfsuite")

model = CRFTokenizer.load("/Users/hieunguyen/Desktop/ViNLP/ViNLP/pipeline/bin/tokenize.crfsuite")
y_pred = model.predict(X_test)
print(f1_score(flatten(y_test), flatten(y_pred), average='micro'))
print(model.predict([X_test[0]]))
print(y_test[0])
print(test_data[0])