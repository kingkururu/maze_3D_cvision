import cv2
import mediapipe as mp
import math
import sys
from enum import Enum, auto

class Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    NONE = 5

currDir = Direction.NONE

# 1. Setup MediaPipe Tools
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize the hand processor
# static_image_mode=False is much faster for webcam streams
hand_tracker = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    h, w, _ = frame.shape

    # Flip the image for a 'selfie' view and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 2. The Core Processing Line
    results = hand_tracker.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 1. Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 2. Robust Finger Open Check (Distance-based)
            wrist = hand_landmarks.landmark[0]
            other_fingers_up = []
            
            # Landmark pairs for Index, Middle, Ring, Pinky
            # Compare if the Tip (id) is further from the wrist than the PIP joint (id-2)
            for tip_id in [8, 12, 16, 20]:
                pip_id = tip_id - 2
                
                tip = hand_landmarks.landmark[tip_id]
                pip = hand_landmarks.landmark[pip_id]

                dist_tip = math.sqrt(((tip.x - wrist.x) * w)**2 +
                                    ((tip.y - wrist.y) * h)**2)

                dist_pip = math.sqrt(((pip.x - wrist.x) * w)**2 +
                                    ((pip.y - wrist.y) * h)**2)

                # If the tip is further from the wrist than the middle joint, it's extended
                if dist_tip > dist_pip:
                    other_fingers_up.append(True)
                else:
                    other_fingers_up.append(False)

            # 3. Determine Gesture
            if any(other_fingers_up):
                direction = "None (Fingers Open)"
                currDir = Direction.NONE
                color = (0, 0, 255)
            else:
                # --- Your Existing Angle Logic (Thumb Tip vs Wrist) ---
                thumb_tip = hand_landmarks.landmark[4]
                delta_x = (thumb_tip.x - wrist.x) * w
                delta_y = (thumb_tip.y - wrist.y) * h

                angle = math.degrees(math.atan2(delta_y, delta_x))

                if -125 < angle <= -55: 
                    direction = "FORWARD"
                    currDir = Direction.FORWARD
                elif 55 < angle <= 125: 
                    direction = "BACKWARD"
                    currDir = Direction.BACKWARD    
                elif -55 < angle <= 55:
                    direction = "RIGHT"
                    currDir = Direction.RIGHT
                else: 
                    direction = "LEFT"
                    currDir = Direction.LEFT
                color = (255, 255, 0)

            # 4. Print to screen
            cv2.putText(frame, f"DIR: {direction}", (50, 100), 
                        cv2.FONT_HERSHEY_SIMPLEX, 3, color, 10)
        
    window_name = 'Webcam Feed'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow(window_name, 100, 100)
    small_frame = cv2.resize(frame, (512, 320))
    cv2.putText(small_frame, 'Do a thumbs up to move!', (90, 255), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    cv2.imshow(window_name, small_frame)

    # Replace your sys.exit() logic with this:
    if currDir == Direction.FORWARD:
        print(1, flush=True)
    elif currDir == Direction.BACKWARD:
        print(2, flush=True)
    elif currDir == Direction.LEFT:
        print(3, flush=True)
    elif currDir == Direction.RIGHT:
        print(4, flush=True)
    elif currDir == Direction.NONE:
        print(5, flush=True)

    try:
        sys.stdout.flush()
    except BrokenPipeError:
        sys.exit(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()