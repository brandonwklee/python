import numpy as np 
import csv
import matplotlib.pyplot as plt
import sklearn
import re
import collections
from collections import Counter
from sklearn import metrics
from numpy import array, argmax
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Conv1D, Dropout
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import KFold


stopwords = set(stopwords.words("english"))

harassment = []
domestic = []
unequal = []
harassment_tweets = []
domestic_tweets = []
unequal_tweets = []

texts = []
labels = [] #y_true
maxlen = 50
max_words = 5000

with open("tweets_collected_test.csv", "r") as read_csv:
     read_file = csv.reader(read_csv, delimiter = ",")
     for row in read_file:
          tweet = row[0]
          tweet = str(tweet)
          tweet = tweet.lower()
          label = row[1]
          if label == 'domestic violence':
               domestic.append(label)
               tweet = re.sub(r"http\S+", "", tweet)
               tweet = re.sub(r"@\S+", "", tweet)
               tweet = re.sub(r",", "", tweet)
               tweet = re.sub(r"’", "", tweet)
               tweet = re.sub(r",", "", tweet)
               for word in stopwords:
                    token = ' ' + word + ' '
                    tweet = tweet.replace(token, ' ')
                    tweet = tweet.replace(' ', ' ') 
               domestic_tweets.append(tweet)
               
          if label == 'sexual harassment':
               harassment.append(label)
               tweet = re.sub(r"http\S+", "", tweet)
               tweet = re.sub(r"@\S+", "", tweet)
               tweet = re.sub(r",", "", tweet)
               tweet = re.sub(r"’", "", tweet)
               tweet = re.sub(r",", "", tweet)
               for word in stopwords:
                    token = ' ' + word + ' '
                    tweet = tweet.replace(token, ' ')
                    tweet = tweet.replace(' ', ' ') 
               harassment_tweets.append(tweet)
               
          if label == 'unequal pay':
               unequal.append(label)
               tweet = re.sub(r"http\S+", "", tweet)
               tweet = re.sub(r"@\S+", "", tweet)
               tweet = re.sub(r",", "", tweet)
               tweet = re.sub(r"’", "", tweet)
               tweet = re.sub(r",", "", tweet)
               for word in stopwords:
                    token = ' ' + word + ' '
                    tweet = tweet.replace(token, ' ')
                    tweet = tweet.replace(' ', ' ') 
               unequal_tweets.append(tweet)
               
for i in range(0, len(unequal)):
     texts.append(harassment_tweets[i])
     texts.append(domestic_tweets[i])
     texts.append(unequal_tweets[i])

balanced_domestic_labels = domestic[:len(unequal)]
labels = harassment[:len(unequal)] + balanced_domestic_labels + unequal
    
training_ratio = int(len(texts) * .7)
validation_ratio = int(len(texts) * .3)

values = array(labels)
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
onehot_encoder = OneHotEncoder(sparse = False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
labels = onehot_encoded

tokenizer = Tokenizer(num_words = max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen = maxlen)

print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]

x_train, x_val  = data[:training_ratio], data[-validation_ratio:]
y_train, y_val = labels[:training_ratio], labels[-validation_ratio:]


embeddings_index = {}
f = open('C:\\Users\\Brandon\\Desktop\\project\\glove\\glove.twitter\\glove.twitter.27B.100d.txt', encoding = 'utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs

f.close()

print('Found %s word vectors.' % len(embeddings_index))

embedding_dim = 100
embedding_matrix = np.zeros((max_words, embedding_dim))
for word, i in word_index.items():
    if i < max_words:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
   
model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length = maxlen))
#model.add(CNN,....) this helps to learn features better if WORST CASE scenario does occur
model.add(Conv1D(filters = 32, kernel_size = 1, strides = 1, input_shape = data.shape, activation = 'relu'))
model.add(LSTM(32, return_sequences = True))
model.add(LSTM(32))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='sigmoid'))
model.summary()

model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False

model.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['acc'])
history = model.fit(x_train, y_train, epochs = 15000, batch_size = training_ratio, validation_data = (x_val, y_val))

y_pred = model.predict(x_val) #output of test results
y_pred = np.argmax(y_pred, axis = 1, out = None)
y_val = np.argmax(y_val, axis = 1, out = None)

#y_val is ground truth
#y_pred is preditction
print(classification_report(y_val, y_pred))

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')

plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()
