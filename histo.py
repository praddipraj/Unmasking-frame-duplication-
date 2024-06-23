import cv2
import matplotlib.pyplot as plt
from detect import detect_duplicates
def draw_histogram(video_path):
    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    success, frame = vidcap.read()
    
    while success:
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Calculate histogram
        hist = cv2.calcHist([gray_frame], [0], None, [256], [0,256])
        
        # Plot the histogram
        plt.plot(hist, color='black')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.title('Grayscale Histogram')
        plt.show()
        
        # Read the next frame
        success, frame = vidcap.read()
    
    # Release the video capture object
    vidcap.release()

# Example usage:
if __name__ == "__main__":
    video_path = 'test1.avi'  # Replace 'example_video.mp4' with the path to your video
    draw_histogram(video_path)
