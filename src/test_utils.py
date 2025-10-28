```python
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image




def predict_image(model_path, image_path, target_size=(128,128)):
model = load_model(model_path)
img = Image.open(image_path).convert('RGB').resize(target_size)
arr = np.asarray(img) / 255.0
arr = np.expand_dims(arr, axis=0)
preds = model.predict(arr)
return preds
```


---


## tests/test_utils.py


```python
from src.utils import timestamp


def test_timestamp():
t = timestamp()
assert isinstance(t, str)
assert len(t) > 0
```


---


## assets/alarm.wav


- Add a short alarm sound in `assets/alarm.wav`. You can use any short beep or alarm clip.


---


## Dockerfile (optional)


```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "src/app.py"]
```
