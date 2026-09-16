# Face Recognition & Attendance System

A FaceNet and SVM-based facial recognition and automated attendance tracking system built with OpenCV, TensorFlow/Keras, and scikit-learn.

---

## Features

- **Dataset Collection (`capture`)**: Captures facial images from a webcam with automated quality checks (blurriness detection via Laplacian variance, lighting and brightness validation, and face framing).
- **Model Training (`train`)**: Extracts face embeddings via FaceNet (`keras-facenet`), normalizes feature vectors (L2-norm), and trains a Support Vector Machine (SVM) classifier with probability estimation.
- **Real-Time Recognition (`detect`)**: Detects faces from webcam video streams in real-time, extracts embeddings, and classifies faces with confidence thresholding (marks low-confidence predictions as `Unknown`).
- **Attendance Tracking (`excel`)**: Automatically records student/person check-ins into an Excel spreadsheet (`attendance.xlsx`) with timestamps, duplicate check-in prevention for the current date, and audio confirmation.

---

## Prerequisites

- Python `>= 3.11`
- [`uv`](https://docs.astral.sh/uv/) (Python package and project manager)
- A working webcam

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd image-processing-w4
   ```

2. **Install dependencies with `uv`**:
   ```bash
   uv sync
   ```

> **Note**: This project uses `uv` for environment and package management. All commands should be run using `uv run`.

---

## Usage

The project provides a unified CLI entry point via `main.py`:

```bash
uv run python main.py [mode]
```

### Modes

| Mode | Aliases | Description |
| :--- | :--- | :--- |
| `train` *(default)* | `facenet` | Loads images from `dataset/`, computes FaceNet embeddings, and trains the SVM model (`facenet_svm.pkl` & `label_encoder.pkl`). |
| `capture` | `load`, `dataset` | Opens the webcam to capture and save labeled face images for a person. |
| `detect` | `face_detect`, `recognize` | Starts real-time webcam face recognition with bounding boxes and confidence scores. |
| `excel` | `attendance` | Runs real-time face recognition and automatically logs check-ins to `attendance.xlsx`. |
| `help` | `h` | Displays usage and help information. |

---

### Step-by-Step Workflow

#### 1. Capture Dataset
Collect facial images for each person to train the model:
```bash
uv run python main.py capture
```
- Enter the person's identifier (e.g. `67700033_Vinithorn`).
- Images are automatically inspected for quality (lighting and blurriness) and saved in `dataset/<Person_ID>/`.

#### 2. Train the Model
Train the FaceNet embedding classifier:
```bash
uv run python main.py train
```
This produces:
- `facenet_svm.pkl` — Trained SVM classifier.
- `label_encoder.pkl` — Encoded class labels.

#### 3. Run Live Recognition
Recognize registered faces from the webcam feed:
```bash
uv run python main.py detect
```
Press `q` to exit the video feed window.

#### 4. Automated Attendance Logging
Log check-ins directly into an Excel spreadsheet:
```bash
uv run python main.py excel
```
- Confirmed identities (confidence ≥ 90%) are appended to `attendance.xlsx` with `Name`, `Date`, and `Time`.
- Re-check-ins on the same day are ignored to prevent duplicates.
- Press `q` to stop and save the attendance sheet.

---

## Project Structure

```text
├── dataset/                    # Face image dataset organized by identity
│   ├── 67700033_Vinithorn/
│   ├── 67704982_Tarathorn/
│   └── 67707665_Suphakit/
├── src/
│   ├── example/
│   │   ├── load_face.py        # Dataset capture & preprocessing routines
│   │   └── train_facenet.py    # Embedding extraction and SVM training
│   ├── face_detect/
│   │   └── main.py             # Real-time face recognition function
│   └── excel/
│       └── main.py             # Face recognition with Excel attendance logging
├── main.py                     # Main CLI entry point
├── pyproject.toml              # Dependencies and project configuration
├── uv.lock                     # Lockfile managed by uv
├── AGENTS.md                   # Agent and development rules (uv enforcement)
├── facenet_svm.pkl             # Trained SVM model artifact
└── label_encoder.pkl           # Label encoder artifact
```

---

## Tech Stack

- **Computer Vision**: OpenCV (`opencv-python`)
- **Deep Learning / Embeddings**: FaceNet (`keras-facenet`), TensorFlow / Keras
- **Machine Learning**: scikit-learn (SVM Classifier)
- **Data & Excel**: openpyxl, NumPy
- **Environment Management**: `uv`
