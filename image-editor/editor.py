from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = '/edited_images'

for filename in os.listdir(path):
    # Grab all of the images in the images folder
    img = Image.open(f"{path}/{filename}")

    # Apply the Sharpen filter to all imaged
    edit = img.filter(ImageFilter.SHARPEN)

    # Add a bit of contrast to the images
    factor = 1.2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # Rename all images
    clean_name = os.path.splitext(filename)[0]

    # Output edited image to the new folder
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')