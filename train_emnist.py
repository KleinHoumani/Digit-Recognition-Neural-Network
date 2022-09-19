import tensorflow as tf
from emnist import extract_training_samples, extract_test_samples
import matplotlib.pyplot as plt
import cv2
import time

x_train, y_train = extract_training_samples('letters')
x_test, y_test = extract_test_samples('letters')


# x_train, x_test = x[:60000], x[60000:70000]
# y_train, y_test = y[:60000], y[60000:70000]

# x_train = x_train.reshape(60000, 784)
# x_test = x_test.reshape(10000, 784)

# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()



# img_index = 2
# img = x_train[img_index]
# print("Image Label: " + str(chr(y_train[img_index]+96)))
# plt.imshow(img.reshape(28, 28), cmap=plt.cm.binary)
# plt.show()


# time.sleep(10)

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.softmax))

model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

# model.save('letter_reader.model')

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

