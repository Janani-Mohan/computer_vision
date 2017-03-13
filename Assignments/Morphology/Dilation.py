# import division support code
from __future__ import division
# import opencv
import cv2
import numpy as np
from matplotlib import pyplot as plt

# function to read the image as original and grayscale
def read_image():
    selfie = cv2.imread('./image.jpg')
    selfie = cv2.cvtColor(selfie, cv2.COLOR_BGR2RGB)
    gray = cv2.imread('./image.jpg', 0)
    return selfie, gray


# function to threshold the image to binary image
def threshold_image(gray):
    # Set threshold and maxValue
    thresh = 133
    maxValue = 255
    # Using threshold binary function, binarising the image
    BW = cv2.threshold(gray, thresh, maxValue, cv2.THRESH_BINARY)[1]
    return BW


# function to find the black and white pixels in the image
def find_image_parameters(img):
    height, width = img.shape
    print "height and width : ", height, width
    size = img.size
    print "size of the image in number of pixels", size
    count_nonzero = cv2.countNonZero(img)
    print "Non-zero pixels", count_nonzero
    calc = (count_nonzero / size) * 100
    print "Percentage of white pixels", calc
    print "Percentage of black pixels", (100 - calc)


def resize_image(img):
    new_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    return new_img


def dilate_your_image(img, kernel, anchor_point):
    dilated_image = cv2.dilate(img, dst=None, kernel=kernel, anchor=anchor_point)
    dilated_image = np.asarray(dilated_image)
    print 'The structuring element and its anchor point is '
    print kernel, anchor_point
    return dilated_image


def display_your_images_in_plot(images, titles):
    for i in xrange(0, 5):
        plt.subplot(3, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


# Main function execution
if __name__ == '__main__':
    original, grayscale = read_image()
    black_and_white = threshold_image(grayscale)
    selfie = resize_image(original)
    gray = resize_image(grayscale)
    BW = resize_image(black_and_white)
    find_image_parameters(BW)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    anchor1 = (1, -1)
    anchor2 = (0, -1)
    dilated_image1 = dilate_your_image(BW, kernel1, anchor1)
    dilated_image2 = dilate_your_image(BW, kernel2, anchor2)
    images = [selfie, gray, BW, dilated_image1, dilated_image2]
    titles = ['Original Image', 'Binary Thresholding', 'Black and White Image',
              'Dilated Image + S1', 'Dilated Image + S2']
    display_your_images_in_plot(images, titles)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
