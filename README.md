# ViNLP
[![Upload Python Package](https://github.com/hieunguyen1053/ViNLP/actions/workflows/python-publish.yml/badge.svg)](https://github.com/hieunguyen1053/ViNLP/actions/workflows/python-publish.yml)

All tasks are trained on VLSP2013 and VLSP2016

## Installation

To install ViNLP:

```
$ pip install ViNLP
```

<!-- ## F-measure

### Data VLSP 2013

| Task              | F1(%) |
| ----------------- | ----- |
| Word segmentation | 98.64 |
| Pos tagging       | 98.36 |

### Data VLSP 2016 (Use gold POS, Chunk label)

| Task     | F1(%) |
| -------- | ----- |
| Chunking | 98.78 |
| NER      | 92.69 | -->

## Tutorials

- [1. Word Segmentation](#1-word-segmentation)
- [2. Sentence Segmentation](#2-sentence-segmentation)
- [3. POS Tagging](#2-pos-tagging)
- [4. Chunking](#3-chunking)
- [5. Named Entity Recognition](#4-named-entity-recognition)

### 1. Word Segmentation

Usage

```python
>>> from ViNLP import word_tokenize
>>> sentence = 'Hà Nội test nhanh SARS-CoV-2 cho hành khách từ TP.HCM đến sân bay Nội Bài'

>>> word_tokenize(sentence)
['Hà_Nội', 'test', 'nhanh', 'SARS-CoV-2', 'cho', 'hành_khách', 'từ', 'TP.HCM', 'đến', 'sân_bay', 'Nội_Bài']
```

### 2. Sentence Segmentation

Usage

```python
>>> from ViNLP import sent_tokenize
>>> sentences = 'Trung tâm Y tế TP Thủ Đức cho hay trước đó khi xác định được các trường hợp F0 tại công ty nói trên, các F1, F2 đã được cách ly theo quy định. Nhà xưởng nơi phát hiện ca F0 tạm thời đóng cửa. Ngày 9-7, ngành y tế tiếp tục lấy mẫu xét nghiệm tại công ty để truy tìm các ca dương tính.'

>>> sent_tokenize(sentence)
['Trung tâm Y tế TP Thủ Đức cho hay trước đó khi xác định được các trường hợp F0 tại công ty nói trên , các F1 , F2 đã được cách ly theo quy định .',
'Nhà xưởng nơi phát hiện ca F0 tạm thời đóng cửa .',
'Ngày 9-7 , ngành y tế tiếp tục lấy mẫu xét nghiệm tại công ty để truy tìm các ca dương tính .']
```

### 3. POS Tagging

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

## 4. Chunking

Usage

```python
>>> from ViNLP import chunk
>>> sentence = 'Tổng thống Nga Putin tuyên bố sẵn sàng tiếp tục đối thoại với Mỹ'
>>> chunk(sentence)
[('Tổng_thống', 'N', 'B-NP'),
 ('Nga', 'Np', 'B-NP'),
 ('Putin', 'Np', 'I-NP'),
 ('tuyên_bố', 'V', 'B-VP'),
 ('sẵn_sàng', 'A', 'B-AP'),
 ('tiếp_tục', 'V', 'B-VP'),
 ('đối_thoại', 'V', 'B-VP'),
 ('với', 'E', 'B-PP'),
 ('Mỹ', 'Np', 'B-NP')]
```

## 5. Named Entity Recognition

Usage

```python
>>> from ViNLP import ner
>>> sentence = 'Hậu thượng đỉnh, Tổng thống Putin nói ông Biden khác xa truyền thông miêu tả'
>>> ner(sentence)
[('Hậu', 'N', 'B-NP', 'O'),
 ('thượng_đỉnh', 'N', 'B-NP', 'O'),
 (',', 'CH', 'O', 'O'),
 ('Tổng_thống', 'N', 'B-NP', 'O'),
 ('Putin', 'Np', 'B-NP', 'B-PER'),
 ('nói', 'V', 'B-VP', 'O'),
 ('ông', 'Nc', 'B-NP', 'O'),
 ('Biden', 'Np', 'B-NP', 'B-PER'),
 ('khác', 'A', 'B-AP', 'O'),
 ('xa', 'A', 'B-AP', 'O'),
 ('truyền_thông', 'N', 'B-NP', 'O'),
 ('miêu_tả', 'V', 'B-VP', 'O')]
```
