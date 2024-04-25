import cv2
import mediapipe as mp
import pyautogui

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
capture = cv2.VideoCapture(0)
index_y = 0

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            lankmarks = hand.landmark
            for id, landmark in enumerate(lankmarks):
                if id == 8:
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255,255))
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y
                        pyautogui.moveTo(index_x, index_y)
                        
                    
                if id == 4: 
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width * landmark.x
                    thumb_y = screen_height * landmark.y
                    print('outsie', abs(index_y - thumb_y))

                    if abs(index_y - thumb_y) < 15:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print('click')

    cv2.imshow('virtual Mouse', frame)
    cv2.waitKey(1)