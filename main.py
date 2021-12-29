import cv2
import numpy as np

def ImgCropped(img):
    h, w = img.shape[:2]
    if h == w:
        return img, h
    elif h < w:
        st = np.round((w-h)/2).astype(int)
        print(st)
        return img[0:h, st:st+h], h
    else:
        st = np.round((h-w)/2).astype(int)
        return img[st:st+w, 0:w], w



if __name__ == '__main__':

    _COUNT = 500

    img = cv2.imread('test.png', cv2.IMREAD_COLOR)

    imgCropped, s = ImgCropped(img)
    imgResize = cv2.resize(imgCropped, (_COUNT, _COUNT), interpolation=cv2.INTER_AREA)

    cv2.imshow('Cropped', imgCropped)
    cv2.imshow('Resize', imgResize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



