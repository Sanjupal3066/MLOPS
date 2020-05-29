from keras.datasets import fashion_mnist
from keras.utils.np_utils import to_categorical
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

X_train = X_train.reshape((-1, 28, 28, 1)).astype('float32')
X_test = X_test.reshape((-1, 28, 28, 1)).astype('float32')

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

X_train_norm = X_train / 255
X_test_norm = X_test / 255

model = Sequential()

model.add(Convolution2D(filters=64, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(filters=32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(10, activation='softmax'))
h = model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

trained_model = model.fit(X_train, y_train,
         epochs=10,batch_size=32,
          validation_data=(X_test, y_test),
          )

final_acc=int(trained_model.history['accuracy'][-1]*100)


final_acc

loss , acc = model.evaluate(X_test, y_test)


acc

f = open("demofile3.txt", "w")
f.write(str(final_acc))
f.close()