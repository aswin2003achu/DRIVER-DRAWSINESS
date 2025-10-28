```python
import os
import time
from playsound import playsound


def play_alarm(path: str):
"""Play alarm sound (blocking)."""
if os.path.exists(path):
try:
playsound(path)
except Exception as e:
print(f"Could not play alarm: {e}")
else:
print(f"Alarm file not found: {path}")




def timestamp():
return time.strftime('%Y-%m-%d %H:%M:%S')
```
