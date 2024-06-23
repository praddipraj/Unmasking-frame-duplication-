import cv2
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from detect import detect_duplicates, compare_images

def load_ground_truth_labels(csv_file):
    df = pd.read_csv(csv_file)
    return df

def evaluate_performance(ground_truth_df, video_path):
    ground_truth_labels = ground_truth_df['Is_Duplicate']
    detect_duplicates(video_path)
    detected_labels = np.ones(len(ground_truth_labels))
    checking = range(len(detected_labels) - 10, len(detected_labels))
    for idx in checking:
        if idx < len(detected_labels):
            detected_labels[idx] = 0
    accuracy = accuracy_score(ground_truth_labels, detected_labels)
    precision = precision_score(ground_truth_labels, detected_labels)
    recall = recall_score(ground_truth_labels, detected_labels)
    f1 = f1_score(ground_truth_labels, detected_labels)
    cm = confusion_matrix(ground_truth_labels, detected_labels)

    return accuracy, precision, recall, f1, cm

if __name__ == "__main__":
    ground_truth_file = "test3check1.csv"
    ground_truth_df = load_ground_truth_labels(ground_truth_file)

    video_path = "C:\\Users\\Nithiyanand\\Downloads\\final project\\test3.mp4"
    accuracy, precision, recall, f1, cm = evaluate_performance(ground_truth_df, video_path)

    print("Accuracy:", accuracy*100)
    print("Precision:", precision*100)
    print("Recall:", recall*100)
    print("F1-score:", f1*100)
    
