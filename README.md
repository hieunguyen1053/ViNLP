# ViNLP

## Installation

To install ViNLP:

```
$ pip install ViNLP
```

## F-measure

|                   | F1(%) |
| ----------------- | ----- |
| Pos tagging       | 98.36 |
| Word segmentation | 98.57 |

## Tutorials

- [1. Word Segmentation](#1-word-segmentation)
- [2. POS Tagging](#2-pos-tagging)

### 1. Word Segmentation

Usage

```python
>>> from ViNLP import word_tokenize
>>> sentence = 'Hà Nội test nhanh SARS-CoV-2 cho hành khách từ TP.HCM đến sân bay Nội Bài'

>>> word_tokenize(sentence)
['Hà_Nội', 'test', 'nhanh', 'SARS-CoV-2', 'cho', 'hành_khách', 'từ', 'TP.HCM', 'đến', 'sân_bay', 'Nội_Bài']
```

### 2. POS Tagging

Usage

```python
>>> from ViNLP import pos_tag
>>> sentence = 'Bộ Y tế công bố kế hoạch phân bổ vaccine COVID-19 đợt 5, TP.HCM nhiều nhất'
>>> pos_tag(sentence)
[('Bộ', 'N'),
 ('Y_tế', 'N'),
 ('công_bố', 'V'),
 ('kế_hoạch', 'N'),
 ('phân_bổ', 'V'),
 ('vaccine', 'N'),
 ('COVID-19', 'V'),
 ('đợt', 'N'),
 ('5', 'M'),
 (',', 'CH'),
 ('TP.HCM', 'Ny'),
 ('nhiều', 'A'),
 ('nhất', 'R')]
```