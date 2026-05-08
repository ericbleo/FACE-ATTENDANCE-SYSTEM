# Face Attendance System

This project detects faces from a video (or webcam) and marks attendance in a CSV file.

If a known face is found, the person name is written to `attendance.csv` with the current time.

---

## 1) What you need

- Python 3.11
- A camera **or** a video file
- A folder named `FACES` with clear face images

---

## 2) Project structure (important)

Your folder should look like this:

```text
FACE-ATTENDANCE-SYSTEM/
  main.py
  attendance.csv              (auto-created if missing)
  FACES/
    eric.jpg
    alex.png
    maria.jpeg
  barca.mp4                   (optional, if using video file)
```

Notes:
- Image filename becomes the person name.
  - `eric.jpg` -> `ERIC`
- Keep **one person per image** for best results.

---

## 3) Install packages

Open terminal inside this folder and run:

```powershell
python -m pip install --upgrade pip
pip install opencv-python cvzone face_recognition numpy
```

If `face_recognition` installation fails on Windows, install Visual Studio C++ Build Tools, then run the same command again.

Official links:
- [Visual Studio C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- [Direct installer (vs_BuildTools.exe)](https://aka.ms/vs/17/release/vs_BuildTools.exe)

In the installer, select:
- `Desktop development with C++`
- `MSVC v143`
- `Windows 10/11 SDK`
- `C++ CMake tools for Windows`

---

## 4) Choose input source (video file or webcam)

Open `main.py` and find this line in `__init__`:

```python
self.video_path = "barca.mp4"
```

Use one of these:

- Video file:
  ```python
  self.video_path = "barca.mp4"
  ```
- Webcam:
  ```python
  self.video_path = 0
  ```

---

## 5) Run the app

```powershell
python main.py
```

- A window opens with face detection.
- Press `q` to close.

---

## 6) Check attendance output

The app writes attendance to:

- `attendance.csv`

Format:

```text
name,time
ERIC,09:14:22
ALEX,09:15:10
```

Each name is marked once per run (it does not repeat the same name again in that run).

---

## 7) Beginner troubleshooting

### App closes immediately
- Check that your input source exists:
  - If using file mode, confirm `barca.mp4` is present.
  - If using webcam mode, set `self.video_path = 0`.

### Error about `FACES` folder
- Create a folder named exactly `FACES` in the project root.

### Face not recognized
- Use brighter, clearer reference images.
- Put only one face per image in `FACES`.
- Keep the face front-facing if possible.

### `face_recognition` install problems
- Use Python 3.11.
- Install Visual Studio C++ Build Tools, then retry install.
- Download page: [Visual Studio C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

---

## 8) Quick summary

1. Add known face images in `FACES/`.
2. Set `self.video_path` (file or webcam).
3. Run `python main.py`.
4. Press `q` to stop.
5. Open `attendance.csv`.

