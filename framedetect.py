import cv2
from skimage.metrics import structural_similarity
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

# Function to compare images using SSIM, CNN similarity, and signal processing techniques
def compare_images(imageA, imageB):
    # SSIM comparison
    ssim = structural_similarity(imageA, imageB)
    
    # CNN similarity comparison
    cnn_similarity = 0  # Placeholder, as the model needs to be trained
    
    # Signal processing comparison
    # Temporal difference
    blurred_imageA = cv2.GaussianBlur(imageA, (5, 5), 0)
    blurred_imageB = cv2.GaussianBlur(imageB, (5, 5), 0)
    temporal_diff = cv2.absdiff(imageA, blurred_imageA)

    signal_processing_similarity = np.mean(temporal_diff == blurred_imageB)

    return ssim, cnn_similarity, signal_processing_similarity

# Function to detect duplicated frames in a video
def detect_duplicates(video_path):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()

    count = 0
    success = True

    while success:
        cv2.imwrite("./frames/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        if not success:
            break
        count += 1

    dup_count = 0

    for i in range(count):
        if i == 0:
            continue
        else:
            prev_image = cv2.imread('./frames/frame' + str(i-1) + '.jpg')
            curr_image = cv2.imread('./frames/frame' + str(i) + '.jpg')

            grey_prev_image = cv2.cvtColor(prev_image, cv2.COLOR_BGR2GRAY)
            grey_curr_image = cv2.cvtColor(curr_image, cv2.COLOR_BGR2GRAY)

            # Compare images
            ssim, cnn_similarity, signal_processing_similarity = compare_images(grey_prev_image, grey_curr_image)

            # Decide if the frames are duplicates based on thresholds
            if ssim > 0.99  or signal_processing_similarity > 0.8:
                dup_count += 1
                print(f"Frames {i} and {i+1} are duplicates.")
    print(dup_count)
# Example usage
if __name__ == "__main__":
    video_path = 'C:\\Users\\Nithiyanand\\Downloads\\final project\\test3.mp4'
    detect_duplicates(video_path)
