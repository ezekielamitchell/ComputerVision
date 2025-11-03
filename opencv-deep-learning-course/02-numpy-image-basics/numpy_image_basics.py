"""
Section 2: NumPy and Image Basics

Topics covered:
- Introduction to Numpy and Image Section
- NumPy Arrays
- What is an image?
- Images and NumPy
- NumPy and Image Assessment Test
- NumPy and Image Assessment Test - Solutions
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# Topic 1: Introduction to Numpy and Image Section
# ============================================================================
# NumPy is the fundamental package for scientific computing in Python.
# It provides support for large, multi-dimensional arrays and matrices,
# along with mathematical functions to operate on these arrays.
# In computer vision, images are represented as NumPy arrays.

# ============================================================================
# Topic 2: NumPy Arrays
# ============================================================================
# NumPy arrays are the core data structure for numerical computing

# Creating arrays
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)

# Array properties
print("Shape:", arr_2d.shape)  # (rows, columns)
print("Data type:", arr_2d.dtype)
print("Dimensions:", arr_2d.ndim)
print("Size:", arr_2d.size)

# Creating special arrays
zeros = np.zeros((3, 3))  # 3x3 array of zeros
ones = np.ones((2, 4))    # 2x4 array of ones
random_arr = np.random.randint(0, 255, (3, 3))  # Random integers 0-255

# Array indexing and slicing
print("Element at [0, 1]:", arr_2d[0, 1])
print("First row:", arr_2d[0, :])
print("Second column:", arr_2d[:, 1])

# ============================================================================
# Topic 3: What is an image?
# ============================================================================
# An image is a 2D or 3D array of pixels (picture elements).
#
# Grayscale image: 2D array where each element represents pixel intensity
#   - Shape: (height, width)
#   - Values typically: 0 (black) to 255 (white)
#
# Color (RGB) image: 3D array with color channels
#   - Shape: (height, width, channels)
#   - Channels: Red, Green, Blue
#   - Each channel has values 0-255

# ============================================================================
# Topic 4: Images and NumPy
# ============================================================================

# Creating a simple grayscale image (5x5 pixels)
grayscale_img = np.array([
    [0, 50, 100, 150, 200],
    [50, 100, 150, 200, 250],
    [100, 150, 200, 250, 255],
    [150, 200, 250, 255, 200],
    [200, 250, 255, 200, 150]
], dtype=np.uint8)

print("\nGrayscale Image Shape:", grayscale_img.shape)
print("Grayscale Image:\n", grayscale_img)

# Creating a simple RGB image (5x5x3)
# Each pixel has 3 values: [R, G, B]
rgb_img = np.zeros((5, 5, 3), dtype=np.uint8)
rgb_img[:, :, 0] = 255  # Red channel = 255 (full red)
rgb_img[:, :, 1] = 0    # Green channel = 0
rgb_img[:, :, 2] = 0    # Blue channel = 0
# This creates a pure red image

print("\nRGB Image Shape:", rgb_img.shape)
print("RGB Image (first pixel):", rgb_img[0, 0])

# Image operations using NumPy
# Accessing a specific pixel
pixel_value = grayscale_img[2, 2]
print("\nPixel at (2, 2):", pixel_value)

# Modifying pixel values
grayscale_img_copy = grayscale_img.copy()
grayscale_img_copy[0, 0] = 255  # Set top-left pixel to white

# Slicing regions of interest (ROI)
roi = grayscale_img[1:4, 1:4]  # Extract 3x3 region
print("\nRegion of Interest (3x3):\n", roi)

# Image arithmetic
brightened = np.clip(grayscale_img + 50, 0, 255).astype(np.uint8)
darkened = np.clip(grayscale_img - 50, 0, 255).astype(np.uint8)

# Image statistics
print("\nImage Statistics:")
print("Mean intensity:", grayscale_img.mean())
print("Max intensity:", grayscale_img.max())
print("Min intensity:", grayscale_img.min())
print("Standard deviation:", grayscale_img.std())

# ============================================================================
# Topic 5: NumPy and Image Assessment Test
# ============================================================================

# Question 1: Create a 10x10 array of zeros
q1_answer = np.zeros((10, 10))

# Question 2: Create a 10x10 array with values ranging from 0 to 99
q2_answer = np.arange(100).reshape(10, 10)

# Question 3: Create a 8x8 checkerboard pattern (0s and 1s)
q3_answer = np.zeros((8, 8), dtype=int)
q3_answer[1::2, ::2] = 1
q3_answer[::2, 1::2] = 1

# Question 4: Normalize an array (scale values to 0-1 range)
sample_array = np.array([10, 20, 30, 40, 50])
q4_answer = (sample_array - sample_array.min()) / (sample_array.max() - sample_array.min())

# Question 5: Create a 5x5 identity matrix
q5_answer = np.eye(5)

# Question 6: Generate a random 3x3x3 array (like a tiny RGB image)
q6_answer = np.random.randint(0, 256, (3, 3, 3), dtype=np.uint8)

# Question 7: Extract all odd numbers from an array
sample_nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q7_answer = sample_nums[sample_nums % 2 == 1]

# Question 8: Replace all odd numbers with -1
q8_answer = sample_nums.copy()
q8_answer[q8_answer % 2 == 1] = -1

# Question 9: Get the common items between two arrays
arr_a = np.array([1, 2, 3, 4, 5])
arr_b = np.array([4, 5, 6, 7, 8])
q9_answer = np.intersect1d(arr_a, arr_b)

# Question 10: Stack two arrays vertically
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
q10_answer = np.vstack((arr1, arr2))

# ============================================================================
# Topic 6: NumPy and Image Assessment Test - Solutions
# ============================================================================

print("\n=== Assessment Solutions ===")
print("\nQ1 - 10x10 zeros:\n", q1_answer)
print("\nQ2 - 10x10 array (0-99):\n", q2_answer)
print("\nQ3 - Checkerboard pattern:\n", q3_answer)
print("\nQ4 - Normalized array:", q4_answer)
print("\nQ5 - Identity matrix:\n", q5_answer)
print("\nQ6 - Random RGB:\n", q6_answer)
print("\nQ7 - Odd numbers:", q7_answer)
print("\nQ8 - Odd replaced with -1:", q8_answer)
print("\nQ9 - Common items:", q9_answer)
print("\nQ10 - Vertically stacked:\n", q10_answer)
