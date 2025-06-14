"""
Phase 1
----------------------------------------------------------
This exploration it to determine how a gaussian blurr is applied to a singmular pixel or an image.
A gaussian blurr is applied by selecting a singular pixel in an unblurred image and calculating a new pixel value based on the surrounding pixels.
The impact and infuence of the surrounding pixels is determined by a kernel.
A kernel is a weighted matrix; whos size determins the amount of surrounding pixels included, and whos values determin thier weights and impact in the calculation.
----------------------------------------------------------
"""

# Represents a simple 3x3 grayscale image.
# The values are pixel intensities, where 0 is black and 255 is white.
# This image depicts a black dot in the center surrounded by a white background.
sample_image = [
    [255, 255, 255],
    [255, 0,   255],
    [255, 255, 255]
]
# Print the original image matrix to the console.
print("Original Image Pixels:")
print(sample_image)

"""
weighted matrix of size 3x3 pixels
----------------------------------------------------------
This is matrix holds the weights of the surrounding pixels. This is also called a "kernel" or a "filter".
The values in this kernel are based on a Gaussian distribution, giving more weight to the center pixel.
The sum of all values in a typical Gaussian kernel is 1.
----------------------------------------------------------
"""
# This 3x3 matrix is the kernel that will be applied to the image.
# The center value (0.4) is the highest, meaning the center pixel's original value has the most influence.
# The surrounding pixel weights are smaller, decreasing with distance from the center.
weighted_matrix = [
    [0.05, 0.1, 0.05],
    [0.1,  0.4, 0.1],
    [0.05, 0.1, 0.05]
]
# Print the kernel matrix to the console.
print("\nWeighted Matrix (Kernel):")
print(weighted_matrix)


"""
Calculating the new pixel value of the center pixel
----------------------------------------------------------
To calculate the new pixel value, we perform an element-wise multiplication between the image section and the kernel.
Then, all the resulting values are summed up. This process is called convolution.
"""
# Initialize a new 3x3 matrix with all zeros.
# This matrix will store the result of the element-wise multiplication.
new_pixel_value_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Loop through each row of the image and kernel.
for i in range(3):
    # Loop through each column of the image and kernel.
    for j in range(3):
        # Multiply the corresponding pixel value from the image by the weight in the kernel.
        new_pixel_value_matrix[i][j] = sample_image[i][j] * weighted_matrix[i][j]

# Print the result of the element-wise multiplication.
print("\nResult of Element-wise Multiplication:")
print(new_pixel_value_matrix)


# Initialize a variable to hold the final new value for the center pixel.
new_center_pixel_value = 0

# Loop through the new matrix to sum up all the values.
for i in range(len(new_pixel_value_matrix)):
    for j in range(len(new_pixel_value_matrix[i])):
        # Add the current element's value to the total sum.
        new_center_pixel_value += new_pixel_value_matrix[i][j]

# The final sum is the new value for the center pixel of the blurred image.
# In this case, since the center was 0 and surrounded by 255, the new value is an average,
# heavily weighted by the surrounding white pixels.
print("\nNew Center Pixel Value (Blurred):")
print(new_center_pixel_value)