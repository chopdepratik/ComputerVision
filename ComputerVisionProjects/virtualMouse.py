import cv2
import mediapipe as mp
import pyautogui as pa
import numpy as np

pa.FAILSAFE = False

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pa.size()
 
 
 

 
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        continue
    
    frame = cv2.resize(frame, (1920, 1080))

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
    
         

           mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=6, circle_radius=3),)

           index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
           index_tip_x = int(index_tip.x * screen_width)
           index_tip_y = int(index_tip.y * screen_height)
           middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

           middle_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
           middle_MCP_x_x = int(middle_MCP_x.x * frame.shape[1])
           middle_MCP_x_y = int(middle_MCP_x.y * frame.shape[0])

           ring_tip=hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
           ring_tip_x=int(ring_tip.x*frame.shape[1])
           ring_tip_y=int(ring_tip.y*frame.shape[0])

           pinky_tip=hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
           pinky_tip_x=int(pinky_tip.x*frame.shape[1])
           pinky_tip_y=int(pinky_tip.y*frame.shape[0])

           thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
           thumb_tip_x = int(thumb_tip.x * frame.shape[1])
           thumb_tip_y = int(thumb_tip.y * frame.shape[0])

           ring_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP]
           ring_MCP_x_x = int(ring_MCP_x.x * frame.shape[1])
           ring_MCP_x_y = int(ring_MCP_x.y * frame.shape[0])

           pinky_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
           pinky_MCP_x_x = int(pinky_MCP_x.x * frame.shape[1])
           pinky_MCP_x_y = int(pinky_MCP_x.y * frame.shape[0])


           thumb_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
           thumb_MCP_x_x = int(thumb_MCP_x.x * frame.shape[1])
           thumb_MCP_x_y = int(thumb_MCP_x.y * frame.shape[0])
       

        
           cv2.circle(frame, (index_tip_x, index_tip_y), 5, (0,255,0), -1)
        
        
           pa.moveTo(index_tip_x, index_tip_y)

        
           middle_tip_y = int(middle_tip.y * screen_height)
           middle_tip_x=int(middle_tip.x*screen_width)
           index_tip_y=int(index_tip_y*screen_height)
           ring_tip_y=int(ring_tip_y*screen_height)
           ring_MCP_x_y=int(ring_MCP_x_y*screen_height)
           thumb_tip_x=int(thumb_tip_x*screen_width)
           thumb_MCP_x_x=int(thumb_MCP_x_x*screen_width)
           pinky_MCP_x_y=int(pinky_MCP_x.y*screen_height)
           pinky_tip_y=int(pinky_tip.y*screen_height)
         
           if middle_tip_y < middle_MCP_x_y:
              pa.click()
        
           if pinky_tip_y < pinky_MCP_x_y:
              pa.doubleClick()
        
    
    cv2.imshow('Hand Tracking and Cursor Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
