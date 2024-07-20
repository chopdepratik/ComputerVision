import cv2
import serial
 
ser=serial.Serial('COM9',9600,timeout=1)

import mediapipe as mp

index_tip_x=0
index_tip_y=0
middle_tip_x=0
middle_tip_y=0
ring_tip_x=0
ring_tip_y=0
pinky_tip_x=0
pinky_tip_y=0
thumb_tip_x=0
thumb_tip_y=0
index_MCP_x_x = 0
index_MCP_x_y = 0
middle_MCP_x_x = 0
middle_MCP_x_y = 0
ring_MCP_x_x = 0
ring_MCP_x_y = 0
pinky_MCP_x_x = 0
pinky_MCP_x_y = 0
thumb_MCP_x_x = 0
thumb_MCP_x_y = 0

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe Drawing module for drawing landmarks
mp_drawing = mp.solutions.drawing_utils

# Open a video capture object (0 for the default camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    rec=cv2.rectangle(frame,(10,10),(100,100),(0,255,0),-1)
    
    if not ret:
        continue
    
    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect hands
    results = hands.process(frame_rgb)
    
    # Check if at least one hand is detected
    if results.multi_hand_landmarks:
        # Get landmarks of the first detected hand
        hand_landmarks = results.multi_hand_landmarks[0]

        # Draw landmarks on the frame for the first hand only
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        middle_tip=hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        middle_tip_x=int(middle_tip.x*frame.shape[1])
        middle_tip_y=int(middle_tip.y*frame.shape[0])

        index_tip=hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        index_tip_x=int(index_tip.x*frame.shape[1])
        index_tip_y=int(index_tip.y*frame.shape[0])

        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        thumb_tip_x = int(thumb_tip.x * frame.shape[1])
        thumb_tip_y = int(thumb_tip.y * frame.shape[0])

        ring_tip=hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
        ring_tip_x=int(ring_tip.x*frame.shape[1])
        ring_tip_y=int(ring_tip.y*frame.shape[0])

        pinky_tip=hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
        pinky_tip_x=int(pinky_tip.x*frame.shape[1])
        pinky_tip_y=int(pinky_tip.y*frame.shape[0])

        index_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
        index_MCP_x_x = int(index_MCP_x.x * frame.shape[1])
        index_MCP_x_y = int(index_MCP_x.y * frame.shape[0])

        middle_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
        middle_MCP_x_x = int(middle_MCP_x.x * frame.shape[1])
        middle_MCP_x_y = int(middle_MCP_x.y * frame.shape[0])

        ring_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP]
        ring_MCP_x_x = int(ring_MCP_x.x * frame.shape[1])
        ring_MCP_x_y = int(ring_MCP_x.y * frame.shape[0])

        pinky_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
        pinky_MCP_x_x = int(pinky_MCP_x.x * frame.shape[1])
        pinky_MCP_x_y = int(pinky_MCP_x.y * frame.shape[0])

        thumb_MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
        thumb_MCP_x_x = int(thumb_MCP_x.x * frame.shape[1])
        thumb_MCP_x_y = int(thumb_MCP_x.y * frame.shape[0])
         
         
        cv2.circle(frame,(index_tip_x,index_tip_y),5,(0,255,0),-1)
        cv2.circle(frame,(middle_tip_x,middle_tip_y),5,(0,255,0),-1)
        cv2.circle(frame,(ring_tip_x,ring_tip_y),5,(0,255,0),-1)
        cv2.circle(frame,(pinky_tip_x,pinky_tip_y),5,(0,255,0),-1)
        cv2.circle(frame,(thumb_tip_x,thumb_tip_y),5,(0,255,0),-1)
        cv2.circle(frame,(index_MCP_x_x,index_MCP_x_y),5,(255,0,0),-1)
         
        count=0
        if index_tip_y<index_MCP_x_y:
            count=count+1
            str="ON"
            ser.write(str.encode())
        if middle_tip_y<middle_MCP_x_y:
            count=count+1
        if ring_tip_y<ring_MCP_x_y:
            count=count+1
        if pinky_tip_y<pinky_MCP_x_y:
            count=count+1
        if thumb_tip_x>=thumb_MCP_x_x:
            count=count+1
        
        cv2.putText(rec, str(count), (27,85), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=3, color=(0, 255, 255),thickness=3)
   # Display the frame with hand landmarks
    cv2.imshow('Hand Recognition', frame)
    
    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
