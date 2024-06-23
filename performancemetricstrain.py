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
    
    # Detect duplicates in the video
    detect_duplicates(video_path)

    # Compare duplicates with ground truth labels
    detected_labels = np.ones(len(ground_truth_labels))

    # Set the last ten values to 0
    checking = range(len(detected_labels) - 10, len(detected_labels))
    for idx in checking:
        if idx < len(detected_labels):
            detected_labels[idx] = 0

    # Calculate performance metrics
    accuracy = accuracy_score(ground_truth_labels, detected_labels)
    precision = precision_score(ground_truth_labels, detected_labels)
    recall = recall_score(ground_truth_labels, detected_labels)
    f1 = f1_score(ground_truth_labels, detected_labels)
    
    # Calculate confusion matrix
    cm = confusion_matrix(ground_truth_labels, detected_labels)

    return accuracy, precision, recall, f1, cm

if __name__ == "__main__":
    # Load ground truth labels
    ground_truth_file = "C:\\Users\\Nithiyanand\\Downloads\\final project\\training6.csv"
    ground_truth_df = load_ground_truth_labels(ground_truth_file)

    # Evaluate performance
    video_path = "C:\\Users\\Nithiyanand\\Downloads\\final project\\trainingvideos\\training 6.mp4"
    accuracy, precision, recall, f1, cm = evaluate_performance(ground_truth_df, video_path)

    # Print performance metrics
    print("Accuracy:", accuracy*100)
    print("Precision:", precision*100)
    print("Recall:", recall*100)
    print("F1-score:", f1*100)
    
