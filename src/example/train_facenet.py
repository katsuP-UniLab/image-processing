import os
import cv2
import pickle
import numpy as np

from keras_facenet import FaceNet
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import warnings
from sklearn.metrics import accuracy_score, classification_report

# Suppress sklearn future warnings for cleaner output
warnings.filterwarnings("ignore", category=FutureWarning)


def train_facenet(
    dataset_path="dataset",
    model_save_path="facenet_svm.pkl",
    encoder_save_path="label_encoder.pkl",
    batch_size=32,
):
    # ----------------------------
    # Validate dataset path
    # ----------------------------
    if not os.path.exists(dataset_path):
        print(f"❌ Error: Dataset directory '{dataset_path}' not found.")
        print("   Please create a dataset first (e.g., using load_face.py / capture_dataset()).")
        return None, None

    person_dirs = [
        d for d in sorted(os.listdir(dataset_path))
        if os.path.isdir(os.path.join(dataset_path, d))
    ]

    if len(person_dirs) == 0:
        print(f"❌ Error: No person subdirectories found in '{dataset_path}'.")
        return None, None

    print(f"📂 Found {len(person_dirs)} person folder(s): {', '.join(person_dirs)}")

    # ----------------------------
    # Load all face images
    # ----------------------------
    images = []
    labels = []

    print(f"\n📸 Loading images from '{dataset_path}'...")
    for person_name in person_dirs:
        person_path = os.path.join(dataset_path, person_name)
        file_names = sorted(os.listdir(person_path))

        count = 0
        for image_name in file_names:
            if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
                continue

            image_path = os.path.join(person_path, image_name)
            img = cv2.imread(image_path)

            if img is None:
                continue

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (160, 160))

            images.append(img)
            labels.append(person_name)
            count += 1

        print(f"   - {person_name}: {count} images loaded")

    if len(images) == 0:
        print("❌ Error: No valid images found in dataset folders.")
        return None, None

    # Check distinct classes
    unique_labels, class_counts = np.unique(labels, return_counts=True)
    if len(unique_labels) < 2:
        print(f"\n⚠️  Warning: Found only 1 class ({unique_labels[0]}) with {len(images)} images.")
        print("   SVM classifier requires at least 2 distinct persons to train.")
        print("   Please add images for at least one more person.")
        return None, None

    # ----------------------------
    # Load FaceNet model & extract embeddings
    # ----------------------------
    print("\n🧠 Initializing FaceNet model...")
    embedder = FaceNet()

    print(f"⚡ Extracting embeddings for {len(images)} images...")
    X = embedder.embeddings(images)

    # ----------------------------
    # Normalize embedding (L2 Norm)
    # ----------------------------
    norm = np.linalg.norm(X, axis=1, keepdims=True)
    X = np.divide(X, norm, out=np.zeros_like(X), where=norm != 0)

    # ----------------------------
    # Encode labels
    # ----------------------------
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(labels)

    # ----------------------------
    # Split dataset
    # ----------------------------
    can_stratify = np.all(class_counts >= 2)
    stratify_arg = y_encoded if can_stratify else None

    if not can_stratify:
        print("ℹ️  Some classes have fewer than 2 samples; skipping stratification.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=stratify_arg
    )

    # ----------------------------
    # Train SVM
    # ----------------------------
    print(f"\n🏋️ Training SVM classifier on {len(X_train)} samples (testing on {len(X_test)})...")
    model = SVC(kernel="linear", probability=True, C=1.0)
    model.fit(X_train, y_train)

    # ----------------------------
    # Evaluate
    # ----------------------------
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy: {acc * 100:.2f}%\n")
    print("📊 Classification Report:\n")
    print(classification_report(y_test, y_pred, target_names=encoder.classes_, zero_division=0))

    # ----------------------------
    # Save model
    # ----------------------------
    with open(model_save_path, "wb") as f:
        pickle.dump(model, f)
    with open(encoder_save_path, "wb") as f:
        pickle.dump(encoder, f)

    print(f"💾 Saved model to: {model_save_path}")
    print(f"💾 Saved encoder to: {encoder_save_path}")
    print("Training Complete ✔")

    return model, encoder


if __name__ == "__main__":
    train_facenet()
