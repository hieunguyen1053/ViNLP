# ViNLP

## Installation

To install ViNLP:

```
$ pip install ViNLP
```

## Tutorials

* [1. Word Segmentation](#1-word-segmentation)
* [2. POS Tagging](#2-pos-tagging)

### 1. Word Segmentation

Usage

```python
>>> from ViNLP import word_tokenize
>>> sentence = 'Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò'

>>> word_tokenize(sentence)
['Chàng trai', '9X', 'Quảng Trị', 'khởi nghiệp', 'từ', 'nấm', 'sò']
```

### 2. POS Tagging

Usage

```python
>>> from ViNLP import pos_tag
>>> pos_tag('Chợ thịt chó nổi tiếng ở Sài Gòn bị truy quét')
[('Chợ', 'N'),
 ('thịt', 'N'),
 ('chó', 'N'),
 ('nổi tiếng', 'A'),
 ('ở', 'E'),
 ('Sài Gòn', 'Np'),
 ('bị', 'V'),
 ('truy quét', 'V')]
```