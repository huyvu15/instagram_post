# from skimage import io, transform
# from PIL import Image
# # Load the image
# image = io.imread("with_Tep.jpg")

# # Get the dimensions (width and height) of the image
# height, width, channels = image.shape

# # Print the dimensions
# print("Width:", width)
# print("Height:", height)
# print("Number of Channels:", channels)  # Typically 3 for RGB images



# new_width = 191  # Adjust this to your desired width
# new_height = 295  # Adjust this to your desired height

# # Resize the image
# resized_image = transform.resize(image, (new_height, new_width), mode='constant')

# # Display the resized image
# io.imshow(resized_image)
# io.show()

# resized_image.save("repair.jpg")

from PIL import Image

# Open the image file
image = Image.open("with_Tep.jpg")

# Define the new size (width, height)
new_size = (191, 295)  # Change these values to your desired dimensions

# Resize the image
resized_image = image.resize(new_size)

# Save the resized image to a new file
resized_image.save("resized.jpg")
