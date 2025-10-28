```python
"""
Skeleton training script — this is a placeholder that shows how to load images,
create a simple CNN, and train. You will need to adapt this to your dataset.
"""
import argparse
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models




def build_simple_cnn(input_shape=(128,128,3), n_classes=2):
model = models.Sequential([
layers.Input(shape=input_shape),
layers.Conv2D(16, 3, activation='relu'),
layers.MaxPool2D(),
layers.Conv2D(32, 3, activation='relu'),
layers.MaxPool2D(),
layers.Flatten(),
layers.Dense(64, activation='relu'),
layers.Dense(n_classes, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
return model




def main(data_dir, output):
train_dir = os.path.join(data_dir, 'train')
val_dir = os.path.join(data_dir, 'val')


datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True)
train_gen = datagen.flow_from_directory(train_dir, target_size=(128,128), batch_size=32, class_mode='sparse')
val_gen = datagen.flow_from_directory(val_dir, target_size=(128,128), batch_size=32, class_mode='sparse')


model = build_simple_cnn(input_shape=(128,128,3), n_classes=len(train_gen.class_indices))
model.summary()
model.fit(train_gen, validation_data=val_gen, epochs=10)
model.save(output)




if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', required=True)
parser.add_argument('--output', default='models/model.h5')
args = parser.parse_args()
main(args.data_dir, args.output)
```
