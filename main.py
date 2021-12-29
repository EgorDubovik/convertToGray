import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('test.png', cv2.IMREAD_COLOR)
    print(img[50, 50])
    cv2.imshow('Test', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



