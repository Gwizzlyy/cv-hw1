import cv2
import numpy as np

# Loading Image into a variable 
image = cv2.imread("space.jpg", cv2.IMREAD_GRAYSCALE)


def noiser(image, mean = 0, div= 50):
    """ mean -> controls brightness (this case = 0 so default brightness)
        div is sigma -> Standard Diviation; how much noise strength varies
    """
    noise_value = np.random.normal(mean, div, image.shape)
    noisy_image = np.clip(image + noise_value, 0, 255) # lower and upper bound for valid grayscale range
    return noisy_image.astype(np.uint8)
    
# save return into variable for use
noised = noiser(image)
def display(img=image): # double check naming
    cv2.imshow("Current", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# N = 10 # Creating multiple?
# image_collection = [noiser(image) for i in range(N)]
