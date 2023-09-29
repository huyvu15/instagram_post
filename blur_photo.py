from skimage.feature import Cascade
from skimage.filters import gaussian
from skimage import io, data
from skimage.color import rgb2gray
from skimage.feature import corner_peaks
from skimage import img_as_ubyte
import matplotlib.pyplot as plt
import matplotlib.patches as patches

trained_file = data.lbp_frontal_face_cascade_filename()
detector = Cascade(trained_file)

image = io.imread("resized.jpg")

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def getFace(d, image):
    ''' Extracts the face rectangle from the image using the
    coordinates of the detected.
    '''
    # X and Y starting points of the face rectangle
    x, y = d['r'], d['c']
    # The width and height of the face rectangle
    width, height = x + d['width'], y + d['height']
    # Extract the detected face
    face = image[x:width, y:height]
    return face

def mergeBlurryFace(original, d, gaussian_image):
    # X and Y starting points of the face rectangle
    x, y = d['r'], d['c']
    # The width and height of the face rectangle
    width, height = x + d['width'], y + d['height']

    # Ensure the blurred face has the same dtype as the original image
    gaussian_image = img_as_ubyte(gaussian_image)

    # Replace the corresponding region in the original image with the blurred face
    original[x:width, y:height] = gaussian_image
    return original

# Detect the faces
detected = detector.detect_multi_scale(img=rgb2gray(image),
                                       scale_factor=1.2, step_ratio=1,
                                       min_size=(10,10), max_size=(150, 150))

resulting_image = image
# For each detected face
for d in detected:
    # Obtain the face rectangle from detected coordinates
    face = getFace(d, image)

    # Apply gaussian filter to the extracted face (tùy chỉnh sigma độ mờ)
    blurred_face = gaussian(face, sigma=8)

    # Merge this blurry face to our final image
    resulting_image = mergeBlurryFace(image, d, blurred_face)

# Show the image with detected faces
show_image(resulting_image, "Blurred faces")

