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

def getGrayColor(sr):
    count = 8
    start = np.round(255/count).astype(int)
    p = np.round(sr/start).astype(int)*start
    return p



def toGray(img):
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            img[i,j] = getGrayColor(sum(img[i,j])/3)
    return img

if __name__ == '__main__':

    _COUNT = 100

    imgOriginal = cv2.imread('test.png', cv2.IMREAD_COLOR)

    imgCropped, s = ImgCropped(imgOriginal)
    imgResize = cv2.resize(imgCropped, (_COUNT, _COUNT), interpolation=cv2.INTER_AREA)
    imgGray = toGray(imgResize)
    cv2.imshow('ResizeGray', imgGray)
    getGrayColor(156)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




