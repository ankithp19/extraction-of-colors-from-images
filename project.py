import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the range of colors in HSV
def define_color_ranges():
    # Example ranges for colors found in Ayurvedic foods
    color_ranges = {
        'Turmeric': ([20, 100, 100], [30, 255, 255]),  # Yellow
        'Spinach': ([35, 100, 100], [85, 255, 255]),  # Green
        'Tomato': ([0, 100, 100], [10, 255, 255]),   # Red
    }
    return color_ranges

# Function to detect colors in the image and show the process
def detect_colors(image_path, color_ranges):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    detected_colors = {}

    plt.figure(figsize=(15, 10))
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    
    mask_combined = np.zeros(image.shape[:2], dtype="uint8")

    i = 2
    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv_image, lower, upper)
        mask_combined = cv2.bitwise_or(mask_combined, mask)
        
        num_pixels = cv2.countNonZero(mask)
        if num_pixels > 0:
            detected_colors[color_name] = num_pixels

        plt.subplot(2, 2, i)
        plt.imshow(mask, cmap='gray')
        plt.title(f'{color_name} Mask')
        i += 1
    
    highlighted_image = cv2.bitwise_and(image, image, mask=mask_combined)
    
    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(highlighted_image, cv2.COLOR_BGR2RGB))
    plt.title('Highlighted Image')
    
    plt.show()

    return detected_colors

# Main function
def main(image_path):
    color_ranges = define_color_ranges()
    detected_colors = detect_colors(image_path, color_ranges)
    for color, count in detected_colors.items():
        print(f"{color} detected with {count} pixels.")

if __name__ == "__main__":
    image_path = r"C:\Users\nisha\OneDrive\Pictures\desktop-wallpaper-chocolate-lab-puppy-labrador-puppies.jpg"    # Change this to your image path
    main(image_path)
