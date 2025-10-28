# Driver Drowsiness Detection


A starter repository for a driver drowsiness detection system. This repo provides:


- A real-time webcam app using MediaPipe face mesh to monitor the eyes and detect prolonged eye closure.
- Training scaffolding for building a deep learning model (if you have a labeled dataset).
- Utility scripts and a simple alarm.


## Quick start


1. Create a Python virtual environment and install requirements:


```bash
python -m venv venv
source venv/bin/activate # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```


2. Run the real-time app (webcam):


```bash
python src/app.py
```


3. To train a model (placeholder):


```bash
python src/train_model.py --data_dir data/your_dataset --output models/my_model.h5
```


## Files


- `src/app.py` — real-time drowsiness detector using MediaPipe.
- `src/ear_detector.py` — uses face landmarks to compute an eye-closure metric and monitors duration.
- `src/train_model.py` — skeleton to train a CNN if you have labeled images.
- `assets/alarm.wav` — alarm sound played when drowsiness is detected.


## Notes


- This repository uses a heuristic approach (eye-closure duration) which works reasonably well for demonstrations. For production, consider adding head-pose, yawning detection, and a trained temporal model (LSTM) over features.
