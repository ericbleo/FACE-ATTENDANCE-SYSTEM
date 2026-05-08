import cv2
import cvzone
import face_recognition
import os
import numpy as np
import datetime

class FaceAttendance:
    def __init__(self):
        self.confidence_threshold = 0.5
        self.video_path = 0
        self.faces_folder = "./FACES"
        self.video = cv2.VideoCapture(self.video_path)
        
    def resize(self, frame, scale):
        height, width, _ = frame.shape
        dimensions = (int(width * scale), int(height * scale))
        return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

    def find_face_encodings(self, images):
        face_encodings = []
        for image in images:
            image = self.resize(image, 0.7)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            encoding = face_recognition.face_encodings(image)
            if encoding:
                face_encodings.append(encoding[0])
        
        return face_encodings

    def load_faces_and_names(self):
        faces_folder = os.listdir(self.faces_folder)
        face_names = []
        face_images = []

        for face in faces_folder:
            current_face = cv2.imread(f"{self.faces_folder}/{face}")
            if current_face is not None:
                face_images.append(current_face)
                face_names.append(os.path.splitext(face)[0])

        return face_names, face_images

    def mark_attendance(self, name):
        #create a csv file if it doesn't exist
        if not os.path.exists("attendance.csv"):
            with open("attendance.csv", "w") as file:
                file.write("name,time")
        
        with open("attendance.csv", "r+") as file:
            mydatalist = file.readlines()
            namelist = []
            for line in mydatalist:
                entry = line.split(",")
                namelist.append(entry[0])
            if name not in namelist:
                now = datetime.datetime.now()
                timestring = now.strftime("%H:%M:%S")
                file.writelines(f"\n{name},{timestring}")
                print(f"Attendance marked for {name} at {timestring}")

    def run(self):
        face_names, face_images = self.load_faces_and_names()
        face_encodings = self.find_face_encodings(face_images)

        video = self.video
        while True:
            ret, frame = video.read()
            frame = cv2.flip(frame, 1)
            frame = self.resize(frame, 1.3)
            faces_in_frame = face_recognition.face_locations(frame)
            encode_faces_in_frame = face_recognition.face_encodings(frame, faces_in_frame)

            recognized_faces = []

            for encode_face, face_location in zip(encode_faces_in_frame, faces_in_frame):
                matches = face_recognition.compare_faces(face_encodings, encode_face, tolerance=self.confidence_threshold)
                face_distance = face_recognition.face_distance(face_encodings, encode_face)

                if face_encodings:
                    match_index = np.argmin(face_distance)
                    if matches[match_index] and min(face_distance) < self.confidence_threshold:
                        name = face_names[match_index].upper()
                        y1, x2, y2, x1 = face_location
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        cvzone.putTextRect(frame, f"{name}", (x1, y1 - 5), 1, 2, colorT=(0, 0, 0), offset=3)
                        self.mark_attendance(name)

                        recognized_face = self.resize(face_images[match_index], 0.2)
                        recognized_faces.append(recognized_face)

            # Arrange recognized faces vertically on the top right
            if recognized_faces:
                vertical_offset = 0
                for recognized_face in recognized_faces:
                    h, w, _ = recognized_face.shape
                    frame[vertical_offset:vertical_offset + h, -w:] = recognized_face
                    # Add a small gap between images
                    vertical_offset += h + 10

            cv2.imshow("tiktok: @ericbleo", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_attendance = FaceAttendance()
    face_attendance.run()