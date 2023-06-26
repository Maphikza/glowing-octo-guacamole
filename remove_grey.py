from PIL import Image


def grey_scale_transparent():
    """
    Function that removes gray from grayscale images.
    :return: None
    """
    # Open the image file
    image = Image.open('modified_image.png')

    # Convert the image to RGBA mode
    image_rgba = image.convert('RGBA')

    # Define the threshold value to determine which pixels to make transparent
    threshold = 200

    # Create a new image with transparency
    transparent_image = Image.new('RGBA', image.size)

    # Iterate over each pixel in the image
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel_value = image_rgba.getpixel((x, y))

            # Calculate the average of RGB values
            average = sum(pixel_value[:3]) // 3

            # Check if the average value is below the threshold
            if average < threshold:
                # Make the pixel transparent
                transparent_image.putpixel((x, y), (0, 0, 0, 0))
            else:
                # Copy the pixel value from the original image
                transparent_image.putpixel((x, y), pixel_value)

    # Save the modified image with transparency
    transparent_image.save('final_image.png')
