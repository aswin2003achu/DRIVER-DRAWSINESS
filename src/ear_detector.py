```python
def _euclidean(a, b):
return math.dist(a, b)




def eye_aspect_ratio(landmarks, eye_indices) -> float:
"""Compute a metric similar to EAR using MediaPipe landmarks.


landmarks: list-like of (x, y) tuples in pixel coordinates
eye_indices: indices of 6 eye landmarks
"""
p = [landmarks[i] for i in eye_indices]
# vertical distances
A = _euclidean(p[1], p[5])
B = _euclidean(p[2], p[4])
# horizontal distance
C = _euclidean(p[0], p[3])
if C == 0:
return 0.0
ear = (A + B) / (2.0 * C)
return ear




class EYEClosureDetector:
def __init__(self, ear_thresh=0.20, consecutive_frames=48):
"""
ear_thresh: threshold for EAR to consider 'eye closed'
consecutive_frames: number of frames of closed eye to trigger alarm (approx at 30FPS)
"""
self.ear_thresh = ear_thresh
self.consecutive_frames = consecutive_frames
self.counter = 0


def reset(self):
self.counter = 0


def process(self, ear: float) -> bool:
"""Return True if drowsiness detected (alarm condition)."""
if ear < self.ear_thresh:
self.counter += 1
else:
self.counter = 0
return self.counter >= self.consecutive_frames
```


---
