import yaml
import numpy as np

data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []

for comando in data ['comandos']:
    inputs.append(comando['input'].lower())
    outputs.append('{}\{}'.format(comando['entity'], comando['action']))

#processar o text

chars = set()

for ch in inputs + outputs:
    if ch not in chars:
        chars.add(ch)

#mapear char-idx

chr2idx = {}
idx2chr = {}

for i, ch in enumerate(chars):
    chr2idx[ch] = i
    idx2chr[i] = ch




max_seq = max([len(x) for x in inputs])

print('Número de chars:', len(chars))
print('Maior seq:', max_seq)
#criar o dataset
input_data = np.zeros((len(inputs), max_seq, len(chars)), dtype='int32')

for i, input in enumerate(inputs):
    for k, ch in enumerate(inputs):
        input_data[i, k, chr2idx[ch]] = 1.0
    



print(input_data[0])
