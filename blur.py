import cv2
def detect_blur(file_path):
    #Read the image
    img = cv2.imread(file_path)
# Convert to greyscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the laplacian of this image and
# calculate the variance
    var = cv2.Laplacian(grey, cv2.CV_64F).var()
# if variance is less than the set threshold
# image is blurred otherwise not
    if var < 60 :
        return False
    else:
        return True
