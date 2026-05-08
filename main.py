import cv2
import face_recognition

class FaceAttendance:
    def __init__(self):
        self.confidence_threshold = 0.5
        self.video_path = 0
        
    def resize(self, frame, scale):
        height, width, _ = frame.shape
        dimensions = (int(width * scale), int(height * scale))
        return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

    def find_encodings(self, images):
        encoding_list = []
        for image in images:
            image = self.resize(image, 0.7)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            encoding = face_recognition.face_encodings(image)
            if encoding:
                encoding_list.append(encoding[0])
        
        return encoding_list