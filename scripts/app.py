"""Script convert an image to a normalized NumPy array."""

import numpy as np
from PIL import Image

image_path = "image.jpg"
image = Image.open(image_path)
image_array = np.array(image)
image_array_normalized = image_array / 255.0
image_array_normalized = np.expand_dims(image_array_normalized, axis=0)

print("Shape of the normalized image array:", image_array_normalized.shape)
print("Data type of the normalized image array:", image_array_normalized.dtype)
