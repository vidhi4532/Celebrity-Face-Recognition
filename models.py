import keras
from keras.layers import Conv2D,Dense,Dropout,Flatten,BatchNormalization
from keras.models import Sequential, model_from_json
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt 
import pickle
import numpy as np

X = np.array(pickle.load(open("Xall.pickle","rb")))
Y = np.array(pickle.load(open("Yall.pickle","rb")))

Y = to_categorical(Y)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

# json_file = open("Cnn_model.json","r").read()
# model = model_from_json()
model = Sequential()
model.add(Conv2D(64,(6,6),activation="relu",strides=(2,2),input_shape=(100,100,1)))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Conv2D(32,(6,6),activation="relu",strides=(2,2)))

model.add(Dense(128,activation="relu"))
model.add(Flatten())
model.add(Dense(4,activation="softmax"))

sgd = keras.optimizers.SGD(learning_rate=0.1,momentum=0.9)
# adam = keras.optimizers.Adam(learning_rate=0.05)

model_json = model.to_json()
with open("Cnn_model.json", "w") as json_file:
    json_file.write(model_json)

checkpoint = ModelCheckpoint("Best_new_weights.hdf5",monitor = 'val_accuracy',save_best_only = True, mode = 'max')

model.load_weights("Best_new_weights.hdf5")
print("Loaded Weights")

model.compile(optimizer='sgd',loss="categorical_crossentropy",metrics=['accuracy'])
m = model.fit(X_train,Y_train,batch_size=5,epochs=10,shuffle=True,validation_data=(X_test,Y_test),callbacks=[checkpoint])

n = np.arange(10)
plt.style.use("ggplot")
plt.plot(n,m.history["loss"],label="Train Loss")
plt.plot(n,m.history["accuracy"],label="Train accuracy")
plt.plot(n,m.history["val_loss"],label="Test Loss")
plt.plot(n,m.history["val_accuracy"],label="Test accuracy")
plt.xlabel("EPOCHES")
plt.ylabel("Acc/Loss")
plt.legend(loc="upper left")
plt.show()