def create():
    data = []
    raw = open('/Users/hieunguyen/Desktop/ViNLP/ViNLP/data/vlsp2016/test.txt', 'r', encoding='utf8').read()
    sents = raw.split('\n\n')
    for sent in sents:
        _sent = []
        items = sent.split('\n')
        if len(sent) < 2:
            continue
        for idx, item in enumerate(items):
            word, _, _, _ = item.split('\t')
            if idx == 0:
                _sent.append((word, 'BOS'))
            elif idx == len(items)-1:
                _sent.append((word, 'EOS'))
            else:
                _sent.append((word, 'O'))
        data.append(_sent)

    with open('/Users/hieunguyen/Desktop/ViNLP/ViNLP/data/sent_seg/test.txt', 'w') as writer:
        for i in range(len(data)-1):
            sent = data[i]
            for item in sent:
                writer.write('\t'.join(item) + '\n')
            sent = data[i+1]
            for item in sent:
                writer.write('\t'.join(item) + '\n')
            writer.write('\n')

create()