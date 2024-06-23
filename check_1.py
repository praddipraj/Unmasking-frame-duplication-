import cv2
import pandas as pd
from skimage.metrics import structural_similarity

def compare_images(imageA, imageB):
    # SSIM comparison
    ssim = structural_similarity(imageA, imageB)
    
    return ssim

def detect_duplicates(video_path):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()

    count = 0
    success = True

    duplicates = []

    while success:
        cv2.imwrite("./frames/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        if not success:
            break
        count += 1

    for i in range(count):
        if i == 0:
            continue
        else:
            prev_image = cv2.imread('./frames/frame' + str(i-1) + '.jpg')
            curr_image = cv2.imread('./frames/frame' + str(i) + '.jpg')

            grey_prev_image = cv2.cvtColor(prev_image, cv2.COLOR_BGR2GRAY)
            grey_curr_image = cv2.cvtColor(curr_image, cv2.COLOR_BGR2GRAY)

            # Compare images
            ssim = compare_images(grey_prev_image, grey_curr_image)

            # Decide if the frames are duplicates based on thresholds
            if ssim > 0.99:
                duplicates.append((i, 1))
            else:
                duplicates.append((i, 0))

    df = pd.DataFrame(duplicates, columns=['Frame_Number', 'Is_Duplicated'])
    df.to_csv('dupl.csv', index=False)

# Example usage
if __name__ == "__main__":
    video_path = "C:\\Users\\Nithiyanand\\Downloads\\final project\\test1.avi"
    detect_duplicates(video_path)
