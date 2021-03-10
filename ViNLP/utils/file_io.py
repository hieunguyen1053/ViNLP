def read(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        text = f.read()
    return text


def write(filepath, text):
    with open(filepath, 'w', encoding='utf8') as f:
        f.write(text)
