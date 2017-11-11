import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# loading the dataset
filename='input.txt'
raw_text = open(filename).read()

# Preprocessing
new_raw_text = ""
for i in raw_text:
    if ('a'<= i <= 'z') or ('A'<= i <= 'Z') or (i == ' '):
        new_raw_text += i
    else:
        new_raw_text += ' '

raw_text = new_raw_text

# Create mapping of unique chars to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

# sumarize
n_chars = len(raw_text)
n_vocab = len(chars)

# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []

for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i: i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])

# total number of pattens



