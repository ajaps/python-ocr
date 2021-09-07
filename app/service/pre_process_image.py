import argparse
import cv2
import numpy as np

import automatically_deskew_image as auto_deskew

# Binarization
def grayscale(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, im_bw = cv2.threshold(img, 210, 230, cv2.THRESH_BINARY)
    return im_bw

# Noise Removal
def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)
  
# Dilation and Erosion
def thin_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)

def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)
  
# Rotation / Deskewing
# fixed_image = auto_deskew.deskew(img)
# cv2.imwrite("temp/rotated_fixed.jpg", fixed_image)


# Removing Borders
def remove_then_add_borders(image):
    contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y+h, x:x+w]
    
    # add borders
    color = [255, 255, 255]
    top, bottom, left, right = [150]*4
    img = cv2.copyMakeBorder(crop, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return img

def process(img):
  processed_image = grayscale(img)
  processed_image = noise_removal(processed_image)
  processed_image = thin_font(processed_image)
  processed_image = thick_font(processed_image)
  processed_image = remove_then_add_borders(processed_image)

  return processed_image


