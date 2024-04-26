import cv2
import numpy as np

def count_white_spots(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Threshold the grayscale image to get binary image
    _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Count the number of contours
    white_spots_count = len(contours)
    
    return white_spots_count

# Example usage
image_path = R'C:\Users\Hezid\Documents\3rd Party\Plant_Counting\Tutorial\Output_General\small_piece\Output\Session_1\Otsu_R\OTSU_R_piece_0.jpg'
count = count_white_spots(image_path)
print("Number of white spots:", count)
