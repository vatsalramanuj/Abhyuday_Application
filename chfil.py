import cv2
import numpy as np

def contraharmonic_mean_filter(image, kernel_size, Q):
    # Pad the image to handle border pixels
    padding = kernel_size // 2
    image_padded = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT)

    # Create an output image with the same dimensions as the input
    output_image = np.zeros_like(image)

    # Iterate through each pixel in the input image
    for y in range(padding, image.shape[0] + padding):
        for x in range(padding, image.shape[1] + padding):
            # Extract the neighborhood region
            neighborhood = image_padded[y - padding:y + padding + 1, x - padding:x + padding + 1]

            # Calculate the contraharmonic mean
            numerator = np.sum(neighborhood ** (Q + 1))
            denominator = np.sum(neighborhood ** Q)
            if denominator != 0:
                output_pixel = numerator / denominator
            else:
                output_pixel = 0  # Handle division by zero

            # Set the output pixel value
            output_image[y - padding, x - padding] = output_pixel

    return output_image

# Load an image
input_image = cv2.imread('imagefilter.tif')

# Convert the image to float for calculations
input_image = np.float32(input_image)

# Define kernel size and Q value
kernel_size = 9 # 3x3 window
Q = 1.5  # You can adjust this value based on your needs

# Apply the contraharmonic mean filter
output_image = contraharmonic_mean_filter(input_image, kernel_size, Q)

# Convert the output image back to uint8 format
output_image = np.uint8(output_image)

# Save the output image
cv2.imwrite("charmo9.png", output_image)

