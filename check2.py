import cv2
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from detect import detect_duplicates

def load_ground_truth_labels(csv_file):
    df = pd.read_csv(csv_file)
    return df['Is_Duplicate']

def evaluate_performance(video_path):
    # Detect duplicates in the video
    detected_labels = detect_duplicates(video_path)
    return detected_labels

if __name__ == "__main__":
    # Load ground truth labels
    ground_truth_file = "test1frame.csv"
    ground_truth_labels = load_ground_truth_labels(ground_truth_file)

    # Evaluate performance
    video_path = "C:\\Users\\Nithiyanand\\Downloads\\final project\\test1.avi"
    detected_labels = evaluate_performance(video_path)

    # Calculate performance metrics
    accuracy = accuracy_score(ground_truth_labels, detected_labels)
    precision = precision_score(ground_truth_labels, detected_labels)
    recall = recall_score(ground_truth_labels, detected_labels)
    f1 = f1_score(ground_truth_labels, detected_labels)

    # Print performance metrics
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)
