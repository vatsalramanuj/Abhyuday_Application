import cv2
import numpy as np

def harmonic_mean_filter(image, kernel_size):
    filtered_image = np.zeros_like(image, dtype=np.float32)

    pad = kernel_size // 2

    # Iterate over each pixel in the image.
    for i in range(pad, image.shape[0] - pad):
        for j in range(pad, image.shape[1] - pad):
            # Extract the surrounding region.
            region = image[i - pad : i + pad + 1, j - pad : j + pad + 1]

            # Calculate the harmonic mean for each color channel.
            harmonic_means = 1.0 / np.mean(1.0 / (region.astype(np.float32) + 1e-6), axis=(0, 1))

            # Assign the harmonic mean values to the output image.
            filtered_image[i, j] = harmonic_means

    return np.uint8(filtered_image)

if __name__ == "__main__":
    input_image = cv2.imread("imagefilter.tif")

    # Define the kernel size for the surrounding region.
    kernel_size = 9

    # Apply the harmonic mean filter to the image.
    filtered_image = harmonic_mean_filter(input_image, kernel_size)

    # Display the original and filtered images.
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Filtered Image", filtered_image)
    
    # Saving the image
    cv2.imwrite("harmo9.png", filtered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
