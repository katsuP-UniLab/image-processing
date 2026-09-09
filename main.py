import sys
from src.example.load_face import capture_dataset
from src.example.train_facenet import train_facenet


def main():
    # Supports: python main.py [train|capture] (defaults to train)
    mode = "train"
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower().lstrip("-")
        if arg in ("capture", "load", "dataset"):
            mode = "capture"
        elif arg in ("train", "facenet"):
            mode = "train"
        elif arg in ("help", "h"):
            print("Usage: python main.py [train|capture]")
            print("  train   : Train FaceNet + SVM model on dataset (default)")
            print("  capture : Capture new face dataset using webcam")
            return

    if mode == "capture":
        capture_dataset()
    else:
        train_facenet()


if __name__ == "__main__":
    main()
