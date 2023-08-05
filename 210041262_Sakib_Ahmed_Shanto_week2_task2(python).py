import cv2
import numpy as np
image = 'GOAT.jpg'
def detect_red_and_white_regions(image):
        # Step 1: Read the image

        original_image = cv2.imread(image)

        # Step 2: Apply image sharpening using the unsharp mask filter
        sharpened_image = cv2.addWeighted(original_image, 1.5, cv2.GaussianBlur(original_image, (0, 0), 5), -0.5, 0)

        # Step 3: Convert the sharpened image to HSV color space
        hsv_image = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2HSV)

        # Step 4: Define color ranges for red and white in HSV
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        lower_white = np.array([0, 0, 200])
        upper_white = np.array([180, 30, 255])

        # Step 5: Create masks for red and white regions
        red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
        white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

        # Step 6: Find contours of the red and white regions
        red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        white_contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Step 7: Draw contours on the original image
        cv2.drawContours(original_image, red_contours, -1, (0, 0, 255), 2)  # Red color for contours
        cv2.drawContours(original_image, white_contours, -1, (102, 100, 74), 2)  # White color for contours


        # Step 8: Display the output
        cv2.imshow('Detected Red and White Regions in Blurry Region', original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

detect_red_and_white_regions(image)

image_=cv2.imread(image)
grayscale_image = cv2.cvtColor(image_, cv2.COLOR_BGR2GRAY)
image_array = np.array(grayscale_image)

def analyze_goat(image_array):


        min_val = np.min(image_array)
        max_val = np.max(image_array)

        print("Minimum pixel value:", min_val)
        print("Maximum pixel value:", max_val)

        average_value = np.mean(image_array)
        print("Average pixel value:", average_value)






        def create_binary_mask(image_path, threshold_value):
            # Read the image using OpenCV
            image = cv2.imread(image_path)

            # Convert the image to grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Apply global thresholding to create the binary mask
            _, binary_mask = cv2.threshold(grayscale_image, threshold_value, 255, cv2.THRESH_BINARY)

            return binary_mask


        threshold_value = 128  # Adjust this threshold value as needed
        binary_mask = create_binary_mask(image, threshold_value)

        # Count the number of non-zero (foreground) pixels in the binary mask
        num_non_zero_pixels = cv2.countNonZero(binary_mask)
        forgroungzeropixels =cv2.countNonZero(cv2.bitwise_not(binary_mask))
        print("Total number of non-zero (foreground) pixels:", num_non_zero_pixels)
        print("Total number of zero (Background) pixels:", forgroungzeropixels)

analyze_goat(image_array)