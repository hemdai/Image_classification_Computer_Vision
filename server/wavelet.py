import numpy as np
import pywt
import cv2


def w2d(img, mode='haar', level=1):
    imArray = img
    # for converting image to gray form RGB
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
    # convert to floating value
    imArray = np.float32(imArray)
    # normalize data
    imArray /= 255;
    # compute the coefficients
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    # process the Coefficients
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;

    # reconstruction
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)

    return imArray_H

