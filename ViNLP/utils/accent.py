data = open("/Users/hieunguyen/Desktop/ViNLP/ViNLP/data/vi.accent").read().split("\n")
ACCENT_MAP = {}
REVERSE_ACCENT_MAP = {}

for line in data:
    token, label = line.split()
    ACCENT_MAP[token] = label
    REVERSE_ACCENT_MAP[label] = token