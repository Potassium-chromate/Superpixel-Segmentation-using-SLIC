# Superpixel-Segmentation-using-SLIC
This repository contains a Python implementation of the Simple Linear Iterative Clustering (SLIC) algorithm for superpixel segmentation.

## Prerequisites
Before running the code, make sure to install the following Python packages:
+ opencv-python `pip install opencv-python`
+ opencv-contrib-python `pip install opencv-contrib-python`  
These packages are required to import the cv2 module.

## Usage
The code provided performs superpixel segmentation using the SLIC algorithm on an input image. There are two functions for superpixel segmentation:
1. `SLIC(img, region_size, ruler, color_space, iteration_times)`: This function performs superpixel segmentation without averaging the color values of each superpixel.
2. 'SLIC_uniform(img, region_size, ruler, color_space, iteration_times)': This function performs superpixel segmentation and averages the color values of each superpixel.(note: SLIC_uniform is resource consuming. Do not set `region_size` to small `<50`)
To use these functions, modify the input image path in the code and run the script.  
```
  image = plt.imread('path/to/your/image.png')
```
The resulting segmented images will be displayed using `matplotlib.pyplot`

## Parameters
The functions accept the following parameters:
+ `img`: The input image.  
+ `region_size`: The average size of the superpixels (default is 10).
+ `ruler`: The smoothness parameter (default is 20).
+ `color_space`: The color space used for the algorithm, which can be one of the following: "rgb", "gray", "hsv", or "lab".
+ `iteration_times`: The number of iterations to perform for the SLIC algorithm.
For example:
```
  image_SLIC = SLIC(image, 50, 20, 'lab', 10)
```
## Output
The script displays the original image segmented using both the `SLI` and `SLIC_uniform` functions in two subplots. You can view the results by running the script.
