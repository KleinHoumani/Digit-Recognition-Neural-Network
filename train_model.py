import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time


mnist = tf.keras.datasets.mnist
(train, labels_train), (test, labels_test) = mnist.load_data()


train = tf.keras.utils.normalize(train, axis=1)
test = tf.keras.utils.normalize(test, axis=1)

print(train[0])
plt.imshow(train[0])
plt.show()
time.sleep(100)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train, labels_train, epochs=5)
model.save('num_reader')

val_loss, val_acc = model.evaluate(test, labels_test)
print('loss', val_loss, 'accuracy', val_acc)
print('Finished training')
