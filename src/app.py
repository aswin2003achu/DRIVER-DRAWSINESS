```python


def main(alarm_path='assets/alarm.wav', ear_thresh=0.20, consec_frames=48, src=0):
cap = cv2.VideoCapture(src)
detector = EYEClosureDetector(ear_thresh=ear_thresh, consecutive_frames=consec_frames)


with mp_face_mesh.FaceMesh(
static_image_mode=False,
max_num_faces=1,
refine_landmarks=True,
min_detection_confidence=0.5,
min_tracking_confidence=0.5) as face_mesh:
while True:
ret, frame = cap.read()
if not ret:
break
img_h, img_w = frame.shape[:2]
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
results = face_mesh.process(rgb)
alarm = False


if results.multi_face_landmarks:
face_landmarks = results.multi_face_landmarks[0].landmark
pts = landmarks_to_xy(face_landmarks, img_w, img_h)
left_ear = eye_aspect_ratio(pts, LEFT_EYE)
right_ear = eye_aspect_ratio(pts, RIGHT_EYE)
ear = (left_ear + right_ear) / 2.0


# draw
cv2.putText(frame, f"EAR: {ear:.3f}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)


if detector.process(ear):
alarm = True
cv2.putText(frame, "DROWSINESS ALERT!", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 3)


cv2.imshow('Driver Drowsiness Detection', frame)


if alarm:
# play alarm in a non-blocking way by spawning a process or thread
# to keep it simple we call blocking play once per alert trigger
print(timestamp(), "ALARM TRIGGERED")
play_alarm(alarm_path)
detector.reset()


key = cv2.waitKey(1) & 0xFF
if key == ord('q'):
break


cap.release()
cv2.destroyAllWindows()




if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--alarm', default='assets/alarm.wav')
parser.add_argument('--ear', type=float, default=0.20)
parser.add_argument('--frames', type=int, default=48)
parser.add_argument('--src', default=0)
args = parser.parse_args()
main(alarm_path=args.alarm, ear_thresh=args.ear, consec_frames=args.frames, src=args.src)
```
