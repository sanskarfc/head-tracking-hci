import cv2
import dlib
import pyautogui
import math

# Initialize dlib's face detector and the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Define a function to map the position of the head to mouse movement
def map_position(x, y):
    # Map the position to the screen size
    mapped_x = int((x / screen_width) * 1920)
    mapped_y = screen_height - int((y / screen_height) * 1080)  # Invert the y-coordinate
    
    # Move the mouse
    pyautogui.moveTo(mapped_x, mapped_y)

# Define a function to calculate the head tilt angle
def get_head_tilt_angle(landmarks):
    # Get the 2D coordinates of the facial landmarks
    left_eye = (landmarks.part(36).x, landmarks.part(36).y)
    right_eye = (landmarks.part(39).x, landmarks.part(39).y)
    nose_top = (landmarks.part(27).x, landmarks.part(27).y)
    
    # Calculate the vectors between the eyes and the nose
    left_eye_vector = (left_eye[0] - nose_top[0], left_eye[1] - nose_top[1])
    right_eye_vector = (right_eye[0] - nose_top[0], right_eye[1] - nose_top[1])
    
    # Calculate the angle between the eye vectors
    dot_product = left_eye_vector[0] * right_eye_vector[0] + left_eye_vector[1] * right_eye_vector[1]
    magnitude_product = math.sqrt(left_eye_vector[0] ** 2 + left_eye_vector[1] ** 2) * math.sqrt(right_eye_vector[0] ** 2 + right_eye_vector[1] ** 2)
    angle = math.acos(dot_product / magnitude_product)
    
    return angle

# Define a function to detect head nods
def is_head_nod(angle, threshold=0.3):
    if angle > threshold:
        return True
    return False

# Main loop
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = detector(gray)
    
    # Loop over each detected face
    for face in faces:
        # Predict facial landmarks
        landmarks = predictor(gray, face)
        
        # Get the position of the nose
        nose = (landmarks.part(30).x, landmarks.part(30).y)
        
        # Map the position of the nose to mouse movement
        map_position(nose[0], nose[1])
        
        # Calculate the head tilt angle
        angle = get_head_tilt_angle(landmarks)
        
        # Check if a head nod is detected
        if is_head_nod(angle):
            print("Head nod detected, performing left click")
            pyautogui.click()
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
