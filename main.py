import sys
from src.example.load_face import capture_dataset
from src.example.train_facenet import train_facenet
from src.face_detect.main import face_detect
from src.excel.main import excel_attendance


def main():
    # Supports: python main.py [train|capture|detect] (defaults to train)
    mode = "train"
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower().lstrip("-")
        if arg in ("capture", "load", "dataset"):
            mode = "capture"
        elif arg in ("train", "facenet"):
            mode = "train"
        elif arg in ("detect", "face_detect", "recognize"):
            mode = "detect"
        elif arg in ("excel", "attendance"):
            mode = "excel"
        elif arg in ("help", "h"):
            print("Usage: python main.py [train|capture|detect|excel]")
            print("  train   : Train FaceNet + SVM model on dataset (default)")
            print("  capture : Capture new face dataset using webcam")
            print("  detect  : Run real-time face recognition via webcam")
            print("  excel   : Run face recognition with Excel attendance logging")
            return

    if mode == "capture":
        capture_dataset()
    elif mode == "detect":
        face_detect()
    elif mode == "excel":
        excel_attendance()
    else:
        train_facenet()


if __name__ == "__main__":
    main()
