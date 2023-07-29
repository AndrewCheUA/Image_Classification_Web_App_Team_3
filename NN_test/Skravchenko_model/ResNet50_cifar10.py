import json

from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras_preprocessing.image import ImageDataGenerator
from tensorflow import keras

import matplotlib.pyplot as plt

from keras.applications import ResNet50
from keras.applications.resnet import preprocess_input
from keras.datasets import cifar10
from keras.utils import to_categorical
from keras.layers import Flatten, Dense, Dropout, BatchNormalization
from keras.models import Sequential
from keras.optimizers import Adam, SGD, Adamax

NUM_CLASSES = 10
EPOCH = 5
BATCH_SIZE = 128
OPTIMIZER = Adam
LEARNING_RATE = 0.0001
LOSS = 'categorical_crossentropy'
METRICS = ['accuracy']
# resize
img_rows = img_cols = 100
channels = 3

# (x_train, y_train), (x_test, y_test) = cifar10.load_data()
# # img_rows, img_cols , channels= 32,32,3
# for i in range(0,9):
#     plt.subplot(330 + 1 + i)
#     plt.imshow(x_train[i])
# plt.show()
#

# ------------------------------------------------------------------------
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

datagen = ImageDataGenerator(
    rotation_range=15,
    horizontal_flip=True,
    width_shift_range=0.15,
    height_shift_range=0.15,
    zoom_range=0.3
)

X_train = keras.preprocessing.image.smart_resize(X_train, (img_rows, img_cols))
X_test = keras.preprocessing.image.smart_resize(X_test, (img_rows, img_cols))

# предобработка для ResNet50
X_train = preprocess_input(X_train)
X_test = preprocess_input(X_test)
#
# Перетворюємо мітки по категоріям

y_train = to_categorical(y_train, NUM_CLASSES)
y_test = to_categorical(y_test, NUM_CLASSES)

# донавчання
resnet50_base = ResNet50(weights='imagenet', include_top=False, input_shape=(img_rows, img_cols, channels))

resnet50_base.trainable = True

# Заморозка сверточных слоев
for layer in resnet50_base.layers:
    layer.trainable = False

# Training n outs layers
# for layer in resnet50_base.layers[-5:]:
#     layer.trainable = True

addtrain_model = Sequential([
    resnet50_base,
    Flatten(),
    Dense(512, activation="relu"),
    BatchNormalization(),
    Dropout(0.2),
    Dense(NUM_CLASSES, activation="softmax"),
])

addtrain_model.compile(
    optimizer=OPTIMIZER(learning_rate=LEARNING_RATE),
    loss=LOSS,
    metrics=METRICS)

addtrain_model.summary()

checkpoint = ModelCheckpoint("cifar10_best_result1.h5", save_best_only=True)
early_stop = EarlyStopping(
    monitor="val_loss",
    min_delta=0,
    patience=5,
    verbose=0,
    mode="auto",
    baseline=None,
    restore_best_weights=False
)

history = addtrain_model.fit(datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
                             steps_per_epoch=len(X_train) / BATCH_SIZE, epochs=EPOCH,
                             validation_data=(X_test, y_test), callbacks=[checkpoint, early_stop])

results = addtrain_model.evaluate(X_test, y_test)
print(results)


# plotting helper function
def plothist(hist):
    plt.rcParams["figure.figsize"] = (16, 8)
    plt.plot(hist.history['accuracy'])
    plt.plot(hist.history['val_accuracy'])
    plt.title('Точність моделі')
    plt.ylabel('Точність')
    plt.xlabel('Епохи')
    plt.legend(['навчання', 'тестування'], loc='upper left')
    plt.grid()
    plt.savefig('hystory.png')
    plt.show()


plothist(history)

history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

epochs = range(1, len(history_dict['accuracy']) + 1)

plt.rcParams["figure.figsize"] = (16, 8)
plt.plot(epochs, loss_values, 'go', label='Втрати на навчання')
plt.plot(epochs, val_loss_values, 'g', label='Втрати на валідацію')
plt.title('Втрати на навчання та валідацію')
plt.xlabel('Епохи')
plt.ylabel('Втрати')
plt.legend()
plt.grid()
plt.savefig('Training and validation loss.png')
plt.show()

plt.plot(epochs, history_dict['accuracy'], 'go', label='Точність навчання')
plt.plot(epochs, history_dict['val_accuracy'], 'g', label='Точність валідації')
plt.title('Точність навчання та валідації')
plt.xlabel('Епохи')
plt.ylabel('Втрати')
plt.legend()
plt.grid()
plt.savefig('Training and validation accuracy.png')
plt.show()

addtrain_model.save("cifar10_best1.h5")
addtrain_model.save("cifar10_best1.hdf5")
addtrain_model.save_weights("cifar10_best1.h5")

# Гиперпараметры
params = {
    'dataset': 'cifar10',
    'model_name': 'ResNet50',
    'resize': f'32x32x3 to {img_rows}x{img_cols}x3',
    'trainable_model_layers': '10',
    'additional_layers': ['Flatten', 'Dense(512, activation="relu")', 'BatchNormalization()', 'Dropout(0.2)',
                          'Dense(num_classes, activation="softmax")'],
    'num_classes': NUM_CLASSES,
    'epochs': EPOCH,
    'batch_size': BATCH_SIZE,
    'optimizer': f'{OPTIMIZER}',
    'learning_rate': LEARNING_RATE,
    'loss': LOSS,
    'metrics': METRICS,
    'hystory': history.history,
    'model_test_acc': results
}

# Запись в JSON
json_string = json.dumps(params)
with open('model_data.json', 'w') as f:
    f.write(json_string)

print("done")
